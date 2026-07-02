
import voyageai
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from ...models import ContextChunk



vo = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))

def embed_texts(texts: list[str]) -> list[list[float]]:
    result = vo.embed(texts, model="voyage-3.5", input_type="document", output_dimension=1024)
    return result.embeddings

def chunk_text(text: str, chunk_size=800, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    return splitter.split_text(text)



def ingest_context(full_text: str):
    chunks = chunk_text(full_text)
    embeddings = embed_texts(chunks)

    objs = [
        ContextChunk(content=chunk, embedding=emb)
        for chunk, emb in zip(chunks, embeddings)
    ]
    ContextChunk.objects.bulk_create(objs)