import torch
import torch.nn.functional as F

def rank_sections(sections, query_embed, embedder, top_k=5):
    texts = [s['text'] for s in sections]
    embeddings = embedder.encode(texts)
    scores = F.cosine_similarity(query_embed, embeddings).cpu().tolist()
    ranked = sorted(zip(sections, scores), key=lambda x: x[1], reverse=True)
    return ranked[:top_k]
