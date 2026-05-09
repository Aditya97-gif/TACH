import json
import re
import os
import whisper

model = whisper.load_model("large-v2")

audios = os.listdir("aud")

for audio in audios:
    print(audio)
    match = re.search(r'\d+', audio)
    if match:
        number = int(match.group())
    title = "Lecture"
    print(number, title)
    result = model.transcribe(audio = f"aud/{audio}",
                              language="en",
                              task = "transcribe",
                              word_timestamps=False)
    chunks = []
    for segment in result["segments"]:
        chunks.append({"number": number,"title": title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})
    chunks_with_metdata = {"chunks": chunks , "text":result["text"]}
    with open(f"jsons/{audio}.json", "w") as f:        
        json.dump(chunks_with_metdata, f)