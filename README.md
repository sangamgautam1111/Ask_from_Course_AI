# 🎓 VectorPlex

A powerful RAG (Retrieval Augmented Generation) system that converts audio lectures to text and allows you to ask questions about your course materials using AI.

## 🌟 Features

- 🎤 **Audio to Text**: Transcribe audio lectures in Hindi/English using Whisper
- 🔍 **Smart Search**: Vector database powered semantic search
- 🤖 **AI Answers**: Get intelligent answers to questions about your courses
- 🆓 **100% Free**: Uses free AI models (Groq/Llama)
- 🌐 **Multilingual**: Supports both Hindi and English

---

## 📁 Project Structure

```
Ask_from_Course_AI/
├── data/                    # Place your audio files here
├── json_data/              # Transcribed text (auto-generated)
├── vector_db/              # Vector database (auto-generated)
├── rag/
│   └── rag_query.py        # Query your courses
├── transcribe/
│   └── transcribe_audio.py # Convert audio to text
├── vector_db/
│   └── create_vector_db.py # Create embeddings
├── .env                    # API keys (you create this)
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/sangamgautam1111/Ask_from_Course_AI.git
cd Ask_from_Course_AI
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Important:** If you get errors, install packages individually:

```bash
pip install openai-whisper
pip install chromadb
pip install sentence-transformers
pip install groq
pip install python-dotenv
```

### Step 3: Get Your FREE Groq API Key

1. Go to: [https://console.groq.com/](https://console.groq.com/)
2. Sign up (free, no credit card needed)
3. Navigate to: [API Keys](https://console.groq.com/keys)
4. Click "Create API Key"
5. Copy your API key

### Step 4: Create `.env` File

Create a file named `.env` in the **root folder** (not in any subfolder):

```
GROQ_API_KEY=your_api_key_here
```

**⚠️ CRITICAL:** 
- File name is `.env` (with the dot at the start)
- No spaces around the `=` sign
- No quotes around the API key

**Example:**
```
GROQ_API_KEY=gsk_abc123xyz456
```

### Step 5: Download Whisper Model

Download the Whisper base model:

```bash
# Python script to download model
python -c "import whisper; whisper.load_model('base')"
```

Or manually download from [OpenAI Whisper](https://github.com/openai/whisper) and place in your desired location.

### Step 6: Add Your Audio Files

Place your lecture audio files in the `data/` folder:

```
data/
├── lecture1.mp3
├── lecture2.wav
├── lecture3.m4a
└── ...
```

Supported formats: `.mp3`, `.wav`, `.m4a`, `.flac`

---

## 📝 Usage

### 1. Transcribe Audio Files

Update the model path in `transcribe/transcribe_audio.py` if needed, then run:

```bash
python transcribe/transcribe_audio.py
```

This will:
- Convert all audio files to text
- Save JSON files in `json_data/` folder
- Show progress for each file

**Output:**
```
Transcribing: lecture1.mp3
   ✓ Saved: lecture1.json
Transcribing: lecture2.mp3
   ✓ Saved: lecture2.json
...
Total transcriptions: 5
```

### 2. Create Vector Database

```bash
python vector_db/create_vector_db.py
```

This will:
- Load all transcriptions
- Generate embeddings
- Store in ChromaDB vector database

**Output:**
```
Processing transcriptions...
   ✓ Processed: lecture1.json
   ✓ Processed: lecture2.json
...
Successfully added 322 documents to vector database!
```

### 3. Ask Questions

```bash
python rag/rag_query.py
```

**Example Output:**
```
Ready! Ask your questions:

Q: What is the main topic of the lectures?
The key concepts discussed are Accuracy Score and F1 Score, which are explained in the context of Machine Learning...

----------------------------------------------------------------------

Q: मुख्य विषय क्या है?
मुख्य विषय Accuracy और F1 Score के बारे में है...
```

---

## 🛠️ Customization

### Change Questions

Edit `rag/rag_query.py`:

```python
queries = [
    "Your question here",
    "Another question",
    "अपना सवाल यहाँ लिखें"
]
```

### Adjust Number of Context Chunks

In `rag/rag_query.py`, change `n_results`:

```python
contexts = retrieve_relevant_context(query, n_results=5)  # Change 5 to your preference
```

### Use Different AI Model

In `rag/rag_query.py`, change the model:

```python
model="llama-3.3-70b-versatile",  # Try: "mixtral-8x7b-32768" or "llama-3.1-70b-versatile"
```

---

## ⚠️ Common Issues & Solutions

### Issue 1: `ModuleNotFoundError: No module named 'chromadb'`

**Solution:**
```bash
pip install chromadb
```

### Issue 2: `.env` file not found

**Solution:**
- Create `.env` file in the **root folder** (same level as README.md)
- Make sure it starts with a dot: `.env`
- Check the file location: `Ask_from_Course_AI/.env`

### Issue 3: `ValueError: Please set GROQ_API_KEY in .env file`

**Solution:**
- Open `.env` file
- Make sure format is: `GROQ_API_KEY=your_key` (no spaces, no quotes)
- Save the file

### Issue 4: Whisper model not found

**Solution:**
- Update model path in `transcribe_audio.py`:
```python
model_path = "path/to/your/whisper/model/base.pt"
# OR use auto-download:
model = whisper.load_model("base")
```

### Issue 5: Rate limit exceeded

**Solution:**
- Groq free tier: 30 requests/minute
- Wait 60 seconds between large batches
- Or upgrade to Groq paid plan (still very cheap)

### Issue 6: Vector database empty

**Solution:**
- Make sure you ran `transcribe_audio.py` first
- Check if `json_data/` folder has JSON files
- Then run `create_vector_db.py`

---

## 🔧 System Requirements

- **Python:** 3.8 or higher (3.10+ recommended)
- **RAM:** 4GB minimum (8GB recommended for large audio files)
- **Storage:** 2GB free space for models and data
- **OS:** Windows, Linux, or macOS

---



---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

---

## 📄 License

MIT License - feel free to use this project for learning and personal use.

---

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) - Audio transcription
- [ChromaDB](https://www.trychroma.com/) - Vector database
- [Groq](https://groq.com/) - Free AI inference
- [Sentence Transformers](https://www.sbert.net/) - Embeddings

---

## 📧 Contact

Created by [Sangam Gautam](https://github.com/sangamgautam1111)

For questions or support, please open an issue on GitHub.

---

## 🌟 Star this repo if you find it helpful!

Made with ❤️ for students who want to learn smarter, not harder.