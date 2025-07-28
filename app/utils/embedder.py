from sentence_transformers import SentenceTransformer
import os

class Embedder:
    def __init__(self, model_path="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_path)

    def encode(self, texts):
        return self.model.encode(texts, convert_to_tensor=True)
