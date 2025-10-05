import zipfile
import os

INCLUDE = [
    ".git",
    "META-INF",
    "data",
    "addon",
    "assets",
    "pack.mcmeta",
    "fabric.mod.json"
]

BUILD_DIR = "build"
OUTPUT_ZIP = os.path.join(BUILD_DIR, "kc64.zip")

os.makedirs(BUILD_DIR, exist_ok=True)

with zipfile.ZipFile(OUTPUT_ZIP, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for item in INCLUDE:
        if os.path.isdir(item):
            for root, _, files in os.walk(item):
                for file in files:
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, '.')
                    zipf.write(full_path, arcname)
        elif os.path.isfile(item):
            arcname = os.path.basename(item)
            zipf.write(item, arcname)

print(f"Created zip at: {OUTPUT_ZIP}")
