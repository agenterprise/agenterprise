from pydantic.dataclasses import dataclass
from typing import List, Optional, Dict

from app.model.listener.AIURN import AIURN

@dataclass
class LLM:
    name: str
    uid: AIURN
    provider: AIURN
    model: str
    endpoint: str
    version: str
    properties: Optional[Dict[AIURN, str]] = None 

@dataclass
class Agent:
    uid: AIURN
    namespace: AIURN
    name: str
    systemprompt: str
    llmref: AIURN
    properties: Optional[Dict[AIURN, str]] = None


@dataclass
class AIEnvironment:
    name: str
    envid: str
    app_pattern: str
    techstack: AIURN
    agents: List[Agent]
    llms: List[LLM]


   




