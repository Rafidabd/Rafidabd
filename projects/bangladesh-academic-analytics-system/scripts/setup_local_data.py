"""Create empty local JSON files without replacing existing records."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent

for filename, content in (
    ("data/students.json", {"students": []}),
    ("data/datasets.json", {"datasets": []}),
    ("data/admission_prep/topics.json", {"topics": []}),
    ("data/admission_prep/courses.json", {"courses": []}),
):
    path = ROOT / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(json.dumps(content, indent=2) + "\n", encoding="utf-8")
        print("Created", filename)
    else:
        print("Kept existing", filename)
