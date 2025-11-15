from sentence_transformers import SentenceTransformer

# This will download and cache automatically (default cache: ~/.cache/torch/sentence_transformers/)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Save to your custom directory
model.save(r"D:\sangam\Models_for_course ai")

