import os
import chromadb
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv

# Load .env from parent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
env_path = os.path.join(parent_dir, '.env')

load_dotenv(dotenv_path=env_path)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Please set GROQ_API_KEY in .env file")

# Configure Groq (100% FREE) - Silent initialization
client = Groq(api_key=GROQ_API_KEY)

# Load embedding model - Silent
embedding_model_path = r"D:\sangam\Models_for_course ai\embedding model"
embedding_model = SentenceTransformer(embedding_model_path)

# Connect to ChromaDB - Silent
chroma_client_path = r"D:\sangam\Sangam-Documents\Course Info\Ask_from_Course_AI\vector_db"
chroma_client = chromadb.PersistentClient(path=chroma_client_path)
collection = chroma_client.get_collection(name="course_transcriptions")


def retrieve_relevant_context(query, n_results=5):
    """Retrieve relevant documents from vector database"""
    query_embedding = embedding_model.encode([query])[0].tolist()
    
    # Search in ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    
    contexts = []
    for i, doc in enumerate(results['documents'][0]):
        metadata = results['metadatas'][0][i]
        contexts.append({
            'text': doc,
            'filename': metadata.get('filename', 'Unknown'),
            'type': metadata.get('type', 'unknown')
        })
    
    return contexts


def generate_answers(query, contexts):
    """Generate answer using Groq with retrieved context"""
    
    # Build context string
    context_text = "\n\n".join([
        f"[Source: {ctx['filename']}]\n{ctx['text']}"
        for ctx in contexts
    ])
    
    # Create prompt
    prompt = f"""You are a helpful AI assistant answering questions based on course transcripts.

Context from course materials:
{context_text}

User Question: {query}

Instructions:
- Answer the question based on the provided context
- If the context doesn't contain enough information, say so
- Be clear and concise
- Mention the source file if relevant
- Answer in the same language as the question (Hindi or English)

Answer:"""
    
    # Generate response with Groq (FREE & FAST!)
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",  # FREE, powerful model
            temperature=0.7,
            max_tokens=1024,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "rate_limit" in error_msg.lower():
            return "Rate limit exceeded. Please wait a moment and try again."
        return f"Error: {error_msg[:200]}"


def ask_question(query):
    """Main RAG function"""
    # Retrieve relevant context
    contexts = retrieve_relevant_context(query, n_results=5)
    
    # Generate answer
    answer = generate_answers(query, contexts)
    
    # Print only the answer
    print(answer)
    print()
    
    return answer, contexts


if __name__ == "__main__":
    # Remove loading messages for clean output
    print("Ready! Ask your questions:\n")
    
    # Test queries
    queries = [
        "What is the main topic of the lectures?",
        "Explain the key concepts discussed",
        "मुख्य विषय क्या है?"
    ]
    
    for query in queries:
        print(f"Q: {query}")
        ask_question(query)
        print("-" * 70)
        print()