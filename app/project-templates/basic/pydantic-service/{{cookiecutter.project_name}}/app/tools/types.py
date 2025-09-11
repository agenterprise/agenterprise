from typing import Any, List
from pydantic import BaseModel

class ListResponse(BaseModel):
    responses: List[Any]