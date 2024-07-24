import json
import os
import re

BASE_DIR = "../JX3TABS"
SAVE_DIR = "assets"

JSON_STR_KEY_PATTERN = re.compile(r'"(\d+)":')


def save_code(prefix, code):
    code = json.dumps(code, indent=4, ensure_ascii=False)
    code = f"{prefix.upper()} = " + JSON_STR_KEY_PATTERN.sub(r'\1:', code) + "\n"
    with open(os.path.join(SAVE_DIR, f"{prefix.lower()}.py"), "w", encoding="utf-8") as f:
        f.write(code)
