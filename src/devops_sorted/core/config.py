from dataclasses import dataclass


@dataclass
class Settings:
    model: str = "qwen3:0.6b"
    temperature: float = 0.2
    top_k: int = 5


settings = Settings()