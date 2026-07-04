class Retriever:
    """Placeholder retriever for RAG."""

    def __init__(self, index_store):
        self.index_store = index_store

    def retrieve(self, query: str):
        return [doc for doc in self.index_store.list() if query.lower() in doc.lower()]
