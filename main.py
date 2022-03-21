import glob
import re
from collections import defaultdict
from pathlib import Path
from typing import Optional

import yaml

BASE_PATH = Path("./subtitles")
CLEAN_SUBS = Path("./subtitles/clean_subtitles")

EXCLUDE_SPEAKERS = ["\StageDir", "\direct"]


def get_timestamp_dict(text: str) -> dict[str, str]:
    # extracts from the text a dictionary of lines and the time at which they we spoken
    # key: timestamp, value: lines spoken
    timestamp_pattern = re.compile(
        "\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}"
    )
    # tstamp_lines = {
    #     l.split("\n")[0]: l.split("\n")[1] for l in text.split("\n\n") if len(l) > 1
    # }
    if not isinstance(text, list):
        text = text.split("\n")
    tstamp_lines: defaultdict[str, str] = defaultdict(lambda: "")
    current_ts = "beginning_info"
    for line in text:
        if re.match(timestamp_pattern, line):
            current_ts = re.findall("(\d{2}:\d{2}:\d{2}),\d{3} -->")[0]
        else:
            tstamp_lines[current_ts] += line

    return dict(tstamp_lines)


def get_speaker_dict(text: str):
    split_pattern = re.compile(
        "(\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n\\\\)"
    )
    splits = re.split(split_pattern, text)
    print("zoop")


def create_speaker_block(speaker: str, lines: list[str], timestamp: str, **kwargs):
    # the speaker should start with exactly one backslash
    if speaker.startswith(r"\\"):
        speaker = speaker.replace(r"\\\\", r"\\")
    if not speaker.startswith(r"\\"):
        speaker += r"\\"
    block_dict = {"speaker": speaker, "lines": lines, "timestamp": timestamp}
    for key, val in kwargs.items():
        block_dict[key] = val
    return block_dict


#! how to determine if a character is actually speaking, or if it's a \StageDir or \direct or something like that?
def get_lines_dict_v3(text: str, allowed_speakers: Optional[list[str]] = None):
    timestamp_pattern = re.compile(
        "\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}"
    )
    speaker_pattern = re.compile("\n(\\\\\w+")
    print("These are the speakers found: ", set(re.findall(speaker_pattern, text)))
    current_timestamp = "beginning_info"
    current_speaker = "beginning_info"
    current_lines: list[str] = []
    lines_dict: list[str] = []
    for line in text.split("\n"):
        line_info: dict[str, str] = {}
        line_speakers = re.findall(speaker_pattern, line)
        if len(line_speakers) > 0:
            speaker = line_speakers[0]
            if allowed_speakers is not None and speaker in allowed_speakers:
                current_speaker = speaker
            elif allowed_speakers is None:
                current_speaker = speaker
        else:
            current_lines.append(line)


def text_to_latex(timestamp_dict):
    # converts the formatted text to a latex file

    # cut off and store the episode information from the beginning of the file
    # pass to clean_formatted_text
    # transform to latex
    # save latex file
    out_file = ""
    # for timestamp, lines in timestamp_dict.items():
    pass


if __name__ == "__main__":
    paths = [Path(i) for i in glob.glob(str(BASE_PATH) + "/*.srt")]
    paths = [
        Path(
            r"C:\Users\Ryan.Mai\Documents\Other\cteam_transcriptions\subtitles\clean_subtitles\Acq Inc_ The _C_ Team Live - PAX South 2018 (1080p_60fps_H264-128kbit_AAC).English.srt"
        )
    ]
    for path in paths:
        with open(path) as f:
            text = f.read()

        # with open(CLEAN_SUBS / path.name, "w") as f:
        # f.write(text)

        tstamp_lines = get_speaker_dict(text)
        to_path = Path("./yaml_files") / (path.stem + ".yaml")
        # with open(to_path, "w") as f:
        #     yaml.dump(tstamp_lines, f)
