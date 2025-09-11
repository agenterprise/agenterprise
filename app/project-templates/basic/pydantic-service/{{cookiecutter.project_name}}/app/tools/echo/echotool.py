from typing import Any, Final, List, Literal
from pydantic import BaseModel, Field

from mcp.types import Tool, Prompt, PromptArgument, TextContent, PromptMessage, GetPromptResult, ToolAnnotations

from tools.types import ListResponse


class EchoRequest(BaseModel):
    message: str = Field(..., description="Message to echo")
    repeat_count: int = Field(1, ge=-1, le=10)

class SingleEchoResponse(BaseModel):
    text: str = Field(..., description="The Echo")


class EchoResponse(ListResponse):
    responses: List[SingleEchoResponse]
      
class EchoTool(BaseModel):
    SCHEMA_IN: Final = EchoRequest
    SCHEMA_OUT: Final = EchoResponse
    NAME: Final = "echo"
    DESC: Final = "Echo a message"
    TITLE: Final = "Echo Service"
    ANNOTATIONS: Final = ToolAnnotations(title=TITLE, 
                                         readOnlyHint=True, 
                                         destructiveHint=False, 
                                         idempotentHint=True,
                                         openWorldHint=False)

    @staticmethod
    def execute(args):
        req = EchoRequest(**args)
        responses = []
        if req.repeat_count < 0:
            raise ValueError("Cant count backwards...")
        for _ in range(req.repeat_count):
            responses.append(SingleEchoResponse(text=req.message))
        return EchoResponse(responses=responses)
