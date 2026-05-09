import os
import subprocess
import re
files = os.listdir("vid")
for file in files:
    print(file)
    match = re.search(r'\d+', file)
    if match:
        lec_no = int(match.group())
    print(lec_no)
    subprocess.run(["ffmpeg", "-i", f"vid/{file}" , f"aud/Lecture{lec_no}.mp3"])