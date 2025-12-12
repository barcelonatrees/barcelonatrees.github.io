#!/usr/bin/env python3
"""Compress the main trees.geojson file with Barcelona property mappings"""

import json

# Property name mapping
PROPERTY_MAP = {
    "species": "sn",
    "common_name": "cn", 
    "NBRE_DTO": "dt",
    "NBRE_BARRI": "nb",
    "CODIGO_ESP": None
}

def compress_props(props):
    compressed = {}
    for k, v in props.items():
        if v and v != "":
            new_key = PROPERTY_MAP.get(k, k)
            if new_key is not None:
                compressed[new_key] = v
    return compressed

print("Loading trees.geojson...")
with open('trees.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Processing {len(data['features'])} trees...")
for feature in data['features']:
    feature['properties'] = compress_props(feature['properties'])
    coords = feature['geometry']['coordinates']
    feature['geometry']['coordinates'] = [round(coords[0], 6), round(coords[1], 6)]

print("Saving compressed file...")
with open('trees.geojson', 'w', encoding='utf-8') as f:
    json.dump(data, f, separators=(',', ':'), ensure_ascii=False)

print("✅ trees.geojson compressed successfully!")
