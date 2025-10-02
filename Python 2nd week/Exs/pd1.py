import os
import glob
import json

BASE = r"C:\Users\User\Desktop\AndmeTarkusGit\andmeTarkus-1\elektrihind"
pattern = os.path.join(BASE, "output_*2024*.json")             # nt output_elering_price_2025_01.json

files = glob.glob(pattern)
print("Leitud failid:", files)

el_data = []
for filename in files:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        el_data.extend(data.get("data", []))  # ohutu võtme lugemine

# salvesta koond
out_file = os.path.join(BASE, "el1_data_2024.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump({"data": el_data}, f, ensure_ascii=False, indent=2)

print(f"Koond salvestatud: {out_file} | kirjeid: {len(el_data)}")
# print(json.dumps(el_data, ensure_ascii=False, indent=2))