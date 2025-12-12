# 🌳 Barcelona Trees - Interactive Map

An interactive web map visualizing Barcelona's urban trees using open data from the Ajuntament de Barcelona.

## 📊 About This Project

This project is based on the [madtrees](https://github.com/madtrees/madtrees) template and displays Barcelona's tree inventory on an interactive map.

- **Data Source**: [Open Data BCN](https://opendata-ajuntament.barcelona.cat/) - Ajuntament de Barcelona
- **Template**: [madtrees](https://github.com/madtrees/madtrees)
- **Technology**: Leaflet.js, GitHub Pages

## 🚀 Quick Start

### View Online

Visit the live map: `https://barcelonatrees.github.io/barcelonatrees/`

### Run Locally

```powershell
python -m http.server 8000
```

Then open http://localhost:8000

## 📁 Barcelona-Specific Scripts (/scripts)

- `merge-and-convert-bcn.py` - Processes Barcelona open data to GeoJSON
- `compress-main-trees.py` - Compresses trees.geojson
- `split-by-district.py` - Splits data by Barcelona districts
- `compress-districts-bcn.py` - Optimizes district files

## 📖 Documentation

For detailed instructions on customization, data processing, and deployment, see the [madtrees repository](https://github.com/madtrees/madtrees).

## 📄 License

Open source. Tree data Ajuntament de Barcelona ([Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)).
Data: [Open Data BCN](https://opendata-ajuntament.barcelona.cat/data/en/organization/medi-ambient)

---

**Other languages**: [Español](README.es.md) | [Català](README.ca.md)
