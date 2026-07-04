class IndexStore:
    """Placeholder index store for RAG."""

    def __init__(self):
        self.documents = []

    def add(self, document: str):
        self.documents.append(document)

    def list(self):
        return list(self.documents)
