# 🌳 Árboles de Barcelona - Mapa Interactivo

Mapa web interactivo que visualiza los árboles urbanos de Barcelona usando datos abiertos del Ajuntament de Barcelona.

## 📊 Sobre Este Proyecto

Este proyecto está basado en la plantilla [madtrees](https://github.com/madtrees/madtrees) y muestra el inventario de árboles de Barcelona en un mapa interactivo.

- **Fuente de Datos**: [Open Data BCN](https://opendata-ajuntament.barcelona.cat/) - Ajuntament de Barcelona
- **Plantilla**: [madtrees](https://github.com/madtrees/madtrees)
- **Tecnología**: Leaflet.js, GitHub Pages

## 🚀 Inicio Rápido

### Ver en Línea

Visita el mapa en vivo: `https://TU_USUARIO.github.io/barcelonatrees/`

### Ejecutar Localmente

```powershell
python -m http.server 8000
```

Luego abre http://localhost:8000

## 📁 Scripts Específicos para Barcelona (/scripts)

- `merge-and-convert-bcn.py` - Procesa datos abiertos de Barcelona a GeoJSON
- `compress-main-trees.py` - Comprime trees.geojson
- `split-by-district.py` - Divide datos por distritos de Barcelona
- `compress-districts-bcn.py` - Optimiza archivos de distrito

## 📖 Documentación

Para instrucciones detalladas sobre personalización, procesamiento de datos y despliegue, consulta el [repositorio madtrees](https://github.com/madtrees/madtrees).

## 📄 Licencia

Código abierto. Datos de árboles Ajuntament de Barcelona ([Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)).
Datos: [Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/en/organization/medi-ambient)

---

**Otros idiomas**: [English](README.md) | [Català](README.ca.md)
