import glob
import re
from pathlib import Path
import yaml

BASE_PATH = "./subtitles"
paths = [Path(i) for i in glob.glob(BASE_PATH + "/*.srt")]

for path in paths:
    with open(path) as f:
        text = f.read()
    text = re.sub(
        "(\n|^)\d+\n", "\n", text
    )  # remove the lines containing only digits (a counter I guess)
    text = re.sub("<.*?>", "", text)

    tstamp_lines = {
        l.split("\n")[0]: l.split("\n")[1] for l in text.split("\n\n") if len(l) > 1
    }

    breakpoint()
    to_path = Path("./yaml_files") / (path.stem + ".yaml")
    with open(to_path, "w") as f:
        yaml.dump(tstamp_lines, f)
