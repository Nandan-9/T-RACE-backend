from pgvector.django import CosineDistance
from ...models import ContextChunk
from .utils import embed_texts
from langchain_core.messages import SystemMessage, HumanMessage
from ..prompt import system_message
from ..llm_services import chat_llm
def retrieve_relevant_chunks(question: str, top_k=4, max_distance=0.35):
    query_embedding = embed_texts([question])[0]
    
    results = (
        ContextChunk.objects
        .annotate(distance=CosineDistance("embedding", query_embedding))
        .filter(distance__lt=max_distance)   # acts as your relevance threshold
        .order_by("distance")[:top_k]
    )
    return [r.content for r in results]



def rag_answer(question: str):
    chunks = retrieve_relevant_chunks(question)
    
    if not chunks:
        return None
    
    context_text = "\n\n---\n\n".join(chunks)
    
    messages = [
        SystemMessage(content=system_message.format(context=context_text)),
        HumanMessage(content=question)
    ]
    response = chat_llm.invoke(messages)
    print(response)
    # return response.content