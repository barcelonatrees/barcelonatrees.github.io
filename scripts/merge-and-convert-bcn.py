#!/usr/bin/env python3
"""
Script para fusionar los datasets de árboles de Barcelona (parques y viario),
convertirlos a GeoJSON con el formato de barcelonatrees y dividirlos por distritos.
"""

import json
import os
import sys
from collections import defaultdict

def convert_to_geojson(input_files, output_file='trees.geojson'):
    """
    Fusiona múltiples archivos JSON de Barcelona y convierte a GeoJSON con formato barcelonatrees.
    
    Args:
        input_files: Lista de archivos JSON de entrada
        output_file: Archivo GeoJSON de salida
    """
    print(f"🌳 Procesando archivos de Barcelona...")
    
    all_features = []
    total_records = 0
    
    for input_file in input_files:
        if not os.path.exists(input_file):
            print(f"❌ Error: No se encuentra el archivo {input_file}")
            continue
            
        print(f"\n📖 Leyendo {os.path.basename(input_file)}...")
        
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"❌ Error al leer el archivo: {e}")
            continue
        
        if not isinstance(data, list):
            print(f"❌ Error: El archivo no contiene una lista de registros")
            continue
        
        print(f"📊 Registros encontrados: {len(data):,}")
        total_records += len(data)
        
        # Convertir cada registro a Feature de GeoJSON (formato barcelonatrees)
        for record in data:
            # Extraer coordenadas (latitud, longitud)
            try:
                lat = float(record.get('latitud', 0))
                lon = float(record.get('longitud', 0))
            except (ValueError, TypeError):
                continue  # Saltar registros sin coordenadas válidas
            
            # Crear el Feature con la estructura exacta de barcelonatrees
            feature = {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [lon, lat]  # GeoJSON usa [longitud, latitud]
                },
                'properties': {
                    'species': record.get('cat_nom_cientific') or 'Unknown',
                    'common_name': record.get('cat_nom_castella') or record.get('cat_nom_catala') or '',
                    'NBRE_DTO': record.get('nom_districte', ''),
                    'NBRE_BARRI': record.get('nom_barri', ''),
                    'CODIGO_ESP': record.get('cat_especie_id', '')
                }
            }
            
            all_features.append(feature)
    
    print(f"\n✅ Total de árboles procesados: {len(all_features):,} de {total_records:,}")
    
    # Crear el GeoJSON
    geojson = {
        'type': 'FeatureCollection',
        'features': all_features
    }
    
    # Guardar el archivo
    print(f"\n💾 Guardando {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(geojson, f, ensure_ascii=False, separators=(',', ':'))
    
    file_size = os.path.getsize(output_file) / (1024 * 1024)
    print(f"📦 Tamaño del archivo: {file_size:.2f} MB")
    print(f"✅ GeoJSON creado exitosamente: {output_file}")
    
    return output_file

def split_by_district(input_file, output_dir='data/districts'):
    """
    Divide el GeoJSON por distritos de Barcelona.
    
    Args:
        input_file: Ruta al archivo GeoJSON original
        output_dir: Directorio donde guardar los archivos por distrito
    """
    print(f"\n📖 Leyendo {input_file} para dividir por distritos...")
    
    if not os.path.exists(input_file):
        print(f"❌ Error: No se encuentra el archivo {input_file}")
        return False
    
    # Mostrar tamaño original
    original_size = os.path.getsize(input_file) / (1024 * 1024)
    print(f"📦 Tamaño original: {original_size:.2f} MB")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return False
    
    if 'features' not in data or not isinstance(data['features'], list):
        print("❌ Error: Formato de GeoJSON inválido")
        return False
    
    total_trees = len(data['features'])
    print(f"🌳 Total de árboles: {total_trees:,}")
    
    # Agrupar por distrito
    print("\n📊 Agrupando árboles por distrito...")
    districts = defaultdict(list)
    no_district = []
    
    for feature in data['features']:
        props = feature.get('properties', {})
        district_name = (props.get('NBRE_DTO') or '').strip()
        
        if district_name:
            districts[district_name].append(feature)
        else:
            no_district.append(feature)
    
    # Crear directorio de salida
    os.makedirs(output_dir, exist_ok=True)
    print(f"📁 Creando archivos en: {output_dir}/")
    
    # Guardar cada distrito en un archivo separado
    district_info = []
    total_saved = 0
    
    for idx, (district_name, features) in enumerate(sorted(districts.items()), start=1):
        district_code = str(idx).zfill(2)
        
        # Crear GeoJSON para este distrito
        district_geojson = {
            'type': 'FeatureCollection',
            'properties': {
                'district_code': district_code,
                'district_name': district_name,
                'tree_count': len(features)
            },
            'features': features
        }
        
        # Nombre de archivo seguro
        safe_name = district_name.replace(' ', '_').replace('/', '_').replace("'", '')
        filename = f"district_{district_code}_{safe_name}.geojson"
        filepath = os.path.join(output_dir, filename)
        
        # Guardar archivo
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(district_geojson, f, ensure_ascii=False, separators=(',', ':'))
        
        file_size = os.path.getsize(filepath) / (1024 * 1024)
        total_saved += len(features)
        
        district_info.append({
            'code': district_code,
            'name': district_name,
            'filename': filename,
            'tree_count': len(features),
            'size_mb': file_size
        })
        
        print(f"  ✅ {district_code} - {district_name}: {len(features):,} árboles ({file_size:.2f} MB)")
    
    # Guardar árboles sin distrito (si hay)
    if no_district:
        district_geojson = {
            'type': 'FeatureCollection',
            'properties': {
                'district_code': '00',
                'district_name': 'Sin distrito',
                'tree_count': len(no_district)
            },
            'features': no_district
        }
        
        filepath = os.path.join(output_dir, 'district_00_sin_distrito.geojson')
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(district_geojson, f, ensure_ascii=False, separators=(',', ':'))
        
        file_size = os.path.getsize(filepath) / (1024 * 1024)
        total_saved += len(no_district)
        
        district_info.append({
            'code': '00',
            'name': 'Sin distrito',
            'filename': 'district_00_sin_distrito.geojson',
            'tree_count': len(no_district),
            'size_mb': file_size
        })
        
        print(f"  ⚠️  00 - Sin distrito: {len(no_district):,} árboles ({file_size:.2f} MB)")
    
    # Crear archivo de índice con metadatos
    index_file = os.path.join(output_dir, 'districts_index.json')
    index_data = {
        'total_trees': total_trees,
        'total_districts': len(districts),
        'districts': district_info
    }
    
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ División completada!")
    print(f"📂 Archivos creados: {len(district_info)}")
    print(f"🌳 Árboles guardados: {total_saved:,} de {total_trees:,}")
    print(f"📋 Índice creado: {index_file}")
    
    # Calcular tamaño total
    total_size = sum(info['size_mb'] for info in district_info)
    print(f"📦 Tamaño total de archivos: {total_size:.2f} MB")
    if district_info:
        print(f"📉 Tamaño promedio por distrito: {total_size/len(district_info):.2f} MB")
    
    # Mostrar estadísticas
    if district_info:
        print("\n📊 Estadísticas:")
        max_district = max(district_info, key=lambda x: x['tree_count'])
        min_district = min(district_info, key=lambda x: x['tree_count'])
        print(f"  🏆 Distrito con más árboles: {max_district['name']} ({max_district['tree_count']:,})")
        print(f"  📍 Distrito con menos árboles: {min_district['name']} ({min_district['tree_count']:,})")
    
    return True

def main():
    # Archivos de entrada de Barcelona
    input_files = [
        'data/trees-bcn/OD_Arbrat_Parcs_BCN.json',
        'data/trees-bcn/OD_Arbrat_Viari_BCN.json'
    ]
    
    output_geojson = 'trees.geojson'
    output_dir = 'data/districts'
    
    # Procesar argumentos
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '--output-dir' and i + 1 < len(args):
            output_dir = args[i + 1]
            i += 2
        elif args[i] in ['--help', '-h']:
            print_help()
            return
        else:
            print(f"❌ Argumento desconocido: {args[i]}")
            print_help()
            return
    
    print("=" * 60)
    print("🌳 Procesador de Árboles de Barcelona")
    print("=" * 60)
    
    # Paso 1: Fusionar y convertir a GeoJSON
    print("\n🔄 PASO 1: Fusionar datasets y convertir a GeoJSON")
    print("-" * 60)
    geojson_file = convert_to_geojson(input_files, output_geojson)
    
    if not geojson_file or not os.path.exists(geojson_file):
        print("\n❌ Error: No se pudo crear el archivo GeoJSON")
        return
    
    # Paso 2: Dividir por distritos
    print("\n🔄 PASO 2: Dividir por distritos")
    print("-" * 60)
    success = split_by_district(geojson_file, output_dir)
    
    if success:
        print("\n" + "=" * 60)
        print("✅ ¡Proceso completado exitosamente!")
        print("=" * 60)
        print(f"\n📁 Archivos generados:")
        print(f"  - {output_geojson}")
        print(f"  - {output_dir}/district_*.geojson")
        print(f"  - {output_dir}/districts_index.json")
    else:
        print("\n❌ Error al dividir por distritos")

def print_help():
    print("""
🌳 Procesador de Árboles de Barcelona

Uso:
    python merge-and-convert-bcn.py [opciones]

Opciones:
    --output-dir <directorio> Directorio de salida para distritos (default: data/districts)
    --help, -h                Mostrar esta ayuda

Descripción:
    Este script realiza las siguientes operaciones:
    1. Lee los archivos JSON de árboles de Barcelona (parques y viario)
    2. Los fusiona y convierte a formato GeoJSON compatible con barcelonatrees
    3. Divide el resultado por distritos para carga dinámica

Archivos de entrada esperados:
    - data/trees-bcn/OD_Arbrat_Parcs_BCN.json
    - data/trees-bcn/OD_Arbrat_Viari_BCN.json

Archivos de salida:
    - trees.geojson (archivo fusionado)
    - data/districts/district_*.geojson (uno por distrito)
    - data/districts/districts_index.json (índice con metadatos)

Ejemplo:
    python merge-and-convert-bcn.py
    python merge-and-convert-bcn.py --output-dir data/districts
    """)

if __name__ == '__main__':
    main()
