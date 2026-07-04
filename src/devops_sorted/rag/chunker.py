class Chunker:
    """Simple text chunking utility for RAG workflows."""

    def __init__(self, chunk_size: int = 500):
        self.chunk_size = chunk_size

    def chunk(self, text: str):
        if not text:
            return []
        return [text[i : i + self.chunk_size] for i in range(0, len(text), self.chunk_size)]
