#!/usr/bin/env python3
"""Show original properties from Barcelona tree datasets"""

import json

print("=" * 70)
print("BARCELONA STREET TREES (Arbrat Viari)")
print("=" * 70)

with open('data/trees-bcn/OD_Arbrat_Viari_BCN.json', 'r', encoding='utf-8') as f:
    viari_data = json.load(f)

print("\nSample record (first tree):")
print(json.dumps(viari_data[0], indent=2, ensure_ascii=False))

print("\n\nAvailable properties:")
for key in viari_data[0].keys():
    value = viari_data[0][key]
    value_type = type(value).__name__
    value_display = str(value)[:50] if value else "null"
    print(f"  • {key:25} ({value_type:8}) = {value_display}")

print("\n" + "=" * 70)
print("BARCELONA PARK TREES (Arbrat Parcs)")
print("=" * 70)

with open('data/trees-bcn/OD_Arbrat_Parcs_BCN.json', 'r', encoding='utf-8') as f:
    parcs_data = json.load(f)

print("\nSample record (first tree):")
print(json.dumps(parcs_data[0], indent=2, ensure_ascii=False))

print("\n\nAvailable properties:")
for key in parcs_data[0].keys():
    value = parcs_data[0][key]
    value_type = type(value).__name__
    value_display = str(value)[:50] if value else "null"
    print(f"  • {key:25} ({value_type:8}) = {value_display}")

# Show examples of different values for interesting fields
print("\n" + "=" * 70)
print("INTERESTING FIELDS - EXAMPLES")
print("=" * 70)

# Collect unique values for some fields
categories = set()
water_types = set()
irrigation_types = set()

for tree in viari_data[:1000]:  # Sample first 1000
    if tree.get('categoria_arbrat'):
        categories.add(tree['categoria_arbrat'])
    if tree.get('tipus_aigua'):
        water_types.add(tree['tipus_aigua'])
    if tree.get('tipus_reg'):
        irrigation_types.add(tree['tipus_reg'])

print("\nTree categories (categoria_arbrat):")
for cat in sorted(categories):
    print(f"  - {cat}")

print("\nWater types (tipus_aigua):")
for wt in sorted(water_types):
    print(f"  - {wt}")

print("\nIrrigation types (tipus_reg):")
for it in sorted(irrigation_types):
    print(f"  - {it}")

# Show planting date examples
print("\nPlanting date examples (data_plantacio):")
dates_found = 0
for tree in viari_data[:100]:
    if tree.get('data_plantacio'):
        print(f"  - {tree['data_plantacio']}")
        dates_found += 1
        if dates_found >= 5:
            break
if dates_found == 0:
    print("  (No planting dates found in first 100 trees)")
