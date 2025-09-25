from pydantic.dataclasses import dataclass
from typing import List, Optional, Dict

from agenterprise.model.listener.AIURN import AIURN

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
    toolrefs: List[AIURN]
    properties: Optional[Dict[AIURN, str]] = None


@dataclass
class Tool:
    uid: AIURN
    name: str
    endpoint: str
    description: str
    type: str
    properties: Optional[Dict[AIURN, str]] = None


@dataclass
class AIEnvironment:
    name: str
    envid: str
    ai_techlayer: AIURN
    service_techlayer: AIURN
    agents: List[Agent]
    llms: List[LLM]


   




