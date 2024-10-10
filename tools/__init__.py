import json
import os
import re

import pandas as pd

BASE_DIR = "../jx3_exp_src"
SAVE_DIR = "assets"

JSON_STR_KEY_PATTERN = re.compile(r'"(-?\d+)":')


def read_tab(file):
    file_path = os.path.join(BASE_DIR, file)
    df = pd.read_csv(file_path, sep="\t", low_memory=False, encoding="utf-8", on_bad_lines="skip")
    return df


def save_code(prefix, code):
    code = json.dumps(code, indent=4, ensure_ascii=False)
    code = f"{prefix.upper()} = " + JSON_STR_KEY_PATTERN.sub(r'\1:', code) + "\n"
    with open(os.path.join(SAVE_DIR, f"{prefix.lower()}.py"), "w", encoding="utf-8") as f:
        f.write(code)
