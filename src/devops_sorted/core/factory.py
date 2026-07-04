from devops_sorted.clients.ollama import OllamaClient

def get_llm_client() -> OllamaClient:
    """Factory function to create an instance of the OllamaClient."""
    return OllamaClient()