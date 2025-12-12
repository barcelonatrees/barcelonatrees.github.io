# 🌳 Arbres de Barcelona - Mapa Interactiu

Mapa web interactiu que visualitza els arbres urbans de Barcelona utilitzant dades obertes de l'Ajuntament de Barcelona.

## 📊 Sobre Aquest Projecte

Aquest projecte està basat en la plantilla [madtrees](https://github.com/madtrees/madtrees) i mostra l'inventari d'arbres de Barcelona en un mapa interactiu.

- **Font de Dades**: [Open Data BCN](https://opendata-ajuntament.barcelona.cat/) - Ajuntament de Barcelona
- **Plantilla**: [madtrees](https://github.com/madtrees/madtrees)
- **Tecnologia**: Leaflet.js, GitHub Pages

## 🚀 Inici Ràpid

### Veure en Línia

Visita el mapa en viu: `https://barcelonatrees.github.io/barcelonatrees/`

### Executar Localment

```powershell
python -m http.server 8000
```

Després obre http://localhost:8000

## 📁 Scripts Específics per a Barcelona (/scripts)

- `merge-and-convert-bcn.py` - Processa dades obertes de Barcelona a GeoJSON
- `compress-main-trees.py` - Comprimeix trees.geojson
- `split-by-district.py` - Divideix dades per districtes de Barcelona
- `compress-districts-bcn.py` - Optimitza fitxers de districte

## 📖 Documentació

Per a instruccions detallades sobre personalització, processament de dades i desplegament, consulta el [repositori madtrees](https://github.com/madtrees/madtrees).

## 📄 Llicència

Codi obert. Dades d'arbres Ajuntament de Barcelona ([Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)).
Dades: [Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/en/organization/medi-ambient)

---

**Altres idiomes**: [English](README.md) | [Español](README.es.md)
