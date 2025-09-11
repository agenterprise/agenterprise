from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field

class MCPRequest(BaseModel):
    jsonrpc: str = "2.0"
    id: Optional[Union[str, int]] = None
    method: str
    params: Optional[Dict[str, Any]] = None
    user: Optional[str] = Field(None, description="Username of the requester")
    role: Optional[str] = Field(None, description="Role of the requester")  
    scopes: Optional[List[str]] = Field(None, description="Scopes of the requester")    


