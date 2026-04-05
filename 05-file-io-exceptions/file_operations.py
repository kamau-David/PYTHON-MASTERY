"""Reading and writing text and JSON files."""

import json
from pathlib import Path

data_dir = Path(__file__).parent / "data"
data_dir.mkdir(exist_ok=True)

# --- Plain text ---
text_file = data_dir / "notes.txt"
with open(text_file, "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

with open(text_file, "r") as f:
    for line in f:
        print("read:", line.strip())

# --- Appending ---
with open(text_file, "a") as f:
    f.write("Line 3 (appended)\n")

# --- JSON ---
json_file = data_dir / "profile.json"
profile = {"name": "Davian", "skills": ["python", "flutter", "sql"]}

with open(json_file, "w") as f:
    json.dump(profile, f, indent=2)

with open(json_file, "r") as f:
    loaded = json.load(f)
print("loaded json:", loaded)

# Path objects are generally nicer than raw strings for path manipulation
print("exists:", text_file.exists())
print("file size (bytes):", text_file.stat().st_size)
