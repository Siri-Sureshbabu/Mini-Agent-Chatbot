from pathlib import Path
from sentence_transformers import SentenceTransformer
import faiss

model=SentenceTransformer("all-MiniLM-L6-v2")
doc_path=Path("data/documents")
doc=[]
index=None

def load_doc():
    global doc
    doc=[]
    for file in doc_path.glob("*.txt"):
        with open(file,"r",encoding="utf-8") as f:
            doc.append(f.read())
    return doc

def faiss_index():
    global index
    if not doc:
        load_doc()
    embedding=model.encode(doc)
    dim=embedding.shape[1]
    index=faiss.IndexFlat(dim)
    index.add(embedding)

    return index

def search_doc(query:str, top_k:int=2):
    global index
    if index is None:
        faiss_index()

    query_emb=model.encode([query])
    distance,indices=index.search(query_emb, k=1)

    result=[]
    for i in indices[0]:
        if i<len(doc):
            result.append(doc[i])

    return result
