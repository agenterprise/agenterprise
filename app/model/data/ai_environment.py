from pydantic.dataclasses import dataclass
from typing import List, Optional, Dict

from app.model.listener.AIURN import AIURN

@dataclass
class LLM:
    uid: AIURN
    provider: str
    model: str
    endpoint: str
    version: str
    properties: Optional[Dict[str, str]] = None 

@dataclass
class Agent:
    uid: AIURN
    namespace: AIURN
    name: str
    systemprompt: str
    properties: Optional[Dict[AIURN, str]] = None


@dataclass
class AIEnvironment:
    name: str
    deployment: str
    techstack: AIURN
    agents: List[Agent]
    llms: List[LLM]


   




