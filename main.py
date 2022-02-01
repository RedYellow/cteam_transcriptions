import glob
import re
from pathlib import Path

import yaml

BASE_PATH = Path("./subtitles")
CLEAN_SUBS = Path("./subtitles/clean_subtitles")
paths = [Path(i) for i in glob.glob(str(BASE_PATH) + "/*.srt")]

for path in paths:
    with open(path) as f:
        text = f.read()
    text = re.sub(
        "(\n|^)\d+\n", "\n", text
    )  # remove the lines containing only digits (a counter I guess)
    text = re.sub("<.*?>", "", text)

    text = re.sub("walnut.", "Walnut", text)

    mapping_dicts = {
        "coriander": "Coriander",
        "corriander": "Coriander",
        "dinar": "Donaar",
        "rosie": "Rosie",
        "oak": "Oak",
        " oke ": " Oak ",
        "brahma": "Brahma",
    }

    # test this
    # text = re.sub(r"walnut[^\n]+?(\n+[\d: ->,]+?\n+)?grass", r"Walnut Dankgrass\1", text, flags=re.DOTALL)

    with open(CLEAN_SUBS / path.name, "w") as f:
        f.write(text)
    breakpoint()
    tstamp_lines = {
        l.split("\n")[0]: l.split("\n")[1] for l in text.split("\n\n") if len(l) > 1
    }

    to_path = Path("./yaml_files") / (path.stem + ".yaml")
    with open(to_path, "w") as f:
        yaml.dump(tstamp_lines, f)
