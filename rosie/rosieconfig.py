#rosie/rosieconfig.py
from __future__ import annotations
from dataclasses import dataclass
import os
import tomllib
from pathlib import Path
from pyexpat import model

CONFIG_PATH = Path.home() / ".rosie" / "config.toml"

@dataclass
class CoreConfig:
    backend:str #ollama | llama.cpp | claude | openai

@dataclass
class OllamaConfig:
    url:str
    model:str

@dataclass
class LlamaCppConfig:
    url:str
    model:str

@dataclass
class ClaudeConfig:
    model:str
    api_key: str | None = None  # can come from .env var

@dataclass
class OpenAIConfig:
    model:str
    api_key: str | None = None

BackendConfig = OllamaConfig | LlamaCppConfig | ClaudeConfig | OpenAIConfig

@dataclass
class RosieConfig:
    core:CoreConfig
    ollama:OllamaConfig
    claude:ClaudeConfig
    openai:OpenAIConfig
    llamacpp:LlamaCppConfig

    @property
    def active_backend_config(self)->BackendConfig:
        match self.core.backend:

            case "ollama":
                return self.ollama
            case "claude":
                self._resolve_api_key(self.claude, "ROSIE_CLAUDE_API_KEY")
                return self.claude
            case "openai":
                self._resolve_api_key(self.openai, "ROSIE_OPENAI_API_KEY")
                return self.openai
            case "llamacpp":
                return self.llamacpp
            case _:
                raise ValueError(f"Unknown backend {self.core.backend}")
    def _resolve_api_key(self, cfg: ClaudeConfig|OpenAIConfig, key: str)->None:
        """env var takes priority over config file"""
        if os.environ.get(key):
            cfg.api_key = os.environ[key]
        if not cfg.api_key:
            raise ValueError(f"No API key provided for {self.core.backend}"
                             f"Set it in ~/.rosie/config.toml or via {key}")


def load()->RosieConfig:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"No config found. Run `rosie init` to get started"
        )
    with open(CONFIG_PATH, "rb") as f:
        raw=tomllib.load(f)
    return RosieConfig(
        core=CoreConfig(**raw["core"]),
        ollama=OllamaConfig(**raw.get("ollama",{"url":"http://localhost:11434","model":None})),
        llamacpp=LlamaCppConfig(**raw.get("llamacpp",{"url":"http://localhost:8080",model:None})),
        claude=ClaudeConfig(**raw.get("claude",{"model":None})),
        openai=OpenAIConfig(**raw.get("openai",{"model":None}))
    )