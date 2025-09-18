from pydantic.dataclasses import dataclass
from typing import Dict, Optional


@dataclass(config=dict(arbitrary_types_allowed=True))
class BaseModelregistry:
    registry: Optional[Dict[str, any]] = None