from pydantic import Field
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
class Entity:
    uid: AIURN
    name: str
    elements: Optional[List[Dict[str, AIURN|str]]] = None

@dataclass
class Agent:
    uid: AIURN
    namespace: AIURN
    name: str
    systemprompt: str
    llmref: AIURN
    toolrefs: List[AIURN]
    input: Optional[AIURN] = None
    output: Optional[AIURN] = None
    properties: Optional[Dict[AIURN, str]] = None


@dataclass
class Tool:
    uid: AIURN
    name: str
    endpoint: str
    type: str
    properties: Optional[Dict[AIURN, str]] = None
    input: Optional[AIURN] = None
    output: Optional[AIURN] = None
    description: str = Field("No description", description="A brief description of the tool's functionality"   )
    


@dataclass
class AIEnvironment:
    name: str
    envid: str
    ai_techlayer: AIURN
    service_techlayer: AIURN
    data_techlayer: AIURN
    agents: List[Agent]
    llms: List[LLM]


   




