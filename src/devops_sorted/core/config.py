from pathlib import Path
import yaml
from pydantic import BaseModel, ValidationError


class ModelSettings(BaseModel):
    provider: str
    name: str
    host: str


class GenerationSettings(BaseModel):
    temperature: float


class KnowledgeSettings(BaseModel):
    path: Path


class LoggingSettings(BaseModel):
    level: str


class Settings(BaseModel):
    model: ModelSettings
    generation: GenerationSettings
    knowledge: KnowledgeSettings
    logging: LoggingSettings


CONFIG_PATH = (
    Path.home()
    / ".config"
    / "devops-sorted"
    / "config.yaml"
)


def load_settings() -> Settings:
    """Load application settings from the YAML configuration file."""

    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {CONFIG_PATH}"
        )

    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    try:
        settings = Settings.model_validate(config)
    except ValidationError as exc:
        raise RuntimeError(
            f"Invalid configuration file: {CONFIG_PATH}"
        ) from exc

    # Expand "~" if present in paths
    settings.knowledge.path = settings.knowledge.path.expanduser()

    return settings


settings = load_settings()



# print(settings.model.provider)
# print(settings.model.name)
# print(settings.model.host)
# print(settings.generation.temperature)
# print(settings.knowledge.path)
# print(settings.logging.level)