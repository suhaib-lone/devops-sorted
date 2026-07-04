class EmbeddingModel:
    """Placeholder embedding model interface for RAG."""

    def __init__(self, model_name: str = "default"):
        self.model_name = model_name

    def embed(self, text: str):
        return {"model": self.model_name, "text": text}
