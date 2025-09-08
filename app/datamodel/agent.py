from pydantic.dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class Agent:
    uid: str
    namespace: str
    name: str
    systemprompt: str
    properties: Optional[Dict[str, str]] = None