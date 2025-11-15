# Transcribing audio
import os
import json
import whisper
from datetime import datetime

# Loading the model
model_path = r"D:\sangam\model_for_vocalix\base\base.pt"
model = whisper.load_model(model_path)    

audio_path = r"D:\sangam\Sangam-Documents\Course Info\Ask_from_Course_AI\data"
output_folder = r"D:\sangam\Sangam-Documents\Course Info\Ask_from_Course_AI\json_data"
audio_extensions = [".mp3", ".wav", ".m4a", ".flac"]

# If the folder does not exist, create it
os.makedirs(output_folder, exist_ok=True)

all_transcriptions = [] 
successful_count = 0
error_count = 0 

for filename in os.listdir(audio_path):
    if any(filename.lower().endswith(ext) for ext in audio_extensions):
        file_path = os.path.join(audio_path, filename)
        print(f"Transcribing: {filename}")
        
        try:
            
            result = model.transcribe(file_path, language='hi', task="translate", fp16=False)
            
            transcription_data = {
                "filename": filename, 
                "text": result["text"],
                "segments": [
                    {
                        "start": seg["start"],
                        "end": seg["end"],
                        "text": seg["text"]
                    }
                    for seg in result["segments"]
                ],
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),   
            }
            
            # Save individual file
            base_name = os.path.splitext(filename)[0]
            
            with open(os.path.join(output_folder, f"{base_name}.json"), "w", encoding="utf-8") as f:
                json.dump(transcription_data, f, ensure_ascii=False, indent=4)
            
            
            all_transcriptions.append(transcription_data)
            successful_count += 1
            
            
        except Exception as e:
            print(f"   Error with {filename}: {e}")
            error_count += 1


with open(os.path.join(output_folder, "all_transcriptions.json"), "w", encoding="utf-8") as f:
    json.dump(all_transcriptions, f, ensure_ascii=False, indent=4)
