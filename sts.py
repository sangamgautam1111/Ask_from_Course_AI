#using whisper to translate  mp3 to text embeddings
import whisper
model_path = r"D:\sangam\model_for_vocalix\base"
model = whisper.load_model(model_path)
def extract_text_from_audio(audio_path):
    result = model.transcribe(audio_path , fp16 = False)
    return  result['text']

audio_path = r"D:\sangam\Sangam-Documents\Course Info\Ask_from_Course_AI\data"
text = extract_text_from_audio(audio_path)