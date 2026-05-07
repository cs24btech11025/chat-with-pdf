import fitz
import os
import requests
import dotenv
dotenv.load_dotenv()
def extract_text_from_pdf(pdf):
    doc=fitz.open(pdf)
    text="" 
    for page in doc:
        text+=page.get_text()
    return text
def chunk_text(text,chunk_size=500):
    words=text.split()
    chunks=[]
    for i in range(0,len(words),chunk_size):
        chunk=" ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks
def get_chunk(query,chunks):
    query_words=query.lower().split()
    best_chunk=chunks[0]
    max_same=0
    for chunk in chunks:
        chunk_words=chunk.lower().split()
        same_words=set(query_words)&set(chunk_words)
        if len(same_words)>max_same:
            max_same=len(same_words)
            best_chunk=chunk
    return best_chunk
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
def ask_gemini(query,chunk):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={GEMINI_API_KEY}"
    body={
        "contents":[{"parts":[{
            "text":f"Answer this question based on the following text: {chunk}. Question: {query}"
        }]}]
    }
    response=requests.post(url,json=body)
    results=response.json()
    return results["candidates"][0]["content"]["parts"][0]["text"]
if __name__=="__main__":
    pdf=input("enter pdf path..")
    text=extract_text_from_pdf(pdf)
    chunks=chunk_text(text)
    query=input("ask anything...")
    chunk=get_chunk(query,chunks)
    answer=ask_gemini(query,chunk)
    print(answer)
