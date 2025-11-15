#creating vector database for text
import os
import json
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
#instalize embedding model
model_path = r"D:\sangam\Models_for_course ai\embedding model"
embedding_model = SentenceTransformer(model_path)

#using chromadb for the vector database
chorma_client = chromadb.PersistentClient(path=r"D:\sangam\Sangam-Documents\Course Info\Ask_from_Course_AI\vector_db")
#create or get collection if any collection  existed then else create 
collection_name = "course_transcriptions"
try:
    collection = chorma_client.get_collection(name=collection_name)
except:
    collection = chorma_client.create_collection(name= collection_name)
json_folder = r"D:\sangam\Sangam-Documents\Course Info\Ask_from_Course_AI\json_data"
documents = []
metadatas = []
unique_identifiers = []
for filename in os.listdir(json_folder):
    if filename.endswith(".json") and filename != "all_transcriptions.json":
        file_path = os.path.join(json_folder , filename)
        with open(file_path , "r" , encoding= "utf-8") as f:
            data = json.load(f)
            full_text = data.get('text' , "")
            if full_text:
                doc_id = f"{data['filename']}_full"
                documents.append(full_text)
                metadatas.append({
                    "filename" : data["filename"],
                    "type" : "full_transcript",
                    "timestamp" : data.get("timestamp" , "")
                })
                unique_identifiers.append(doc_id)
            #adding segements
            for idx , segment in enumerate(data.get('segments' , [])):
                seg_text = segment.get('text' , "").strip()
                if seg_text:
                    seg_id  = f"{data['filename']}_seg_{idx}"
                    documents.append(seg_text)
                    metadatas.append({
                        "filename" : data["filename"],
                        "type" : "segment",
                        "start" : segment.get("start" , 0),
                        "end" : segment.get("end" , 0),
                        "timestamp" : data.get("timestamp" , "")
                    })
                    unique_identifiers.append(seg_id)
#add documents to chroma db 
if documents:
    #generate embeddings
    embeddings = embedding_model.encode(documents , show_progress_bar=True).tolist()
    #adding to collection
    collection.add(
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=unique_identifiers
    )
else:
    print("No Document Found")
                            
                
                
                
            

