import glob
import re

BASE_PATH = "/Users/Nic/Documents/Python Projects/cteam_transcriptions/subtitles"
paths = glob.glob(BASE_PATH+"/*.srt")

for path in paths:
	with open(path) as f:
		text = f.read()
	text = re.sub("\n|^\d+\n", "\n", text) # remove the lines containing only digits (a counter I guess)
	text = re.sub("<.*?>", "", text)
	breakpoint()
	with open(Path(path).stem()+".txt", "w") as f:
		f.write(text)