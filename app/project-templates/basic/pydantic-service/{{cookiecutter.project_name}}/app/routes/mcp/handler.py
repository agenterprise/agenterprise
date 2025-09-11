
from typing import Any, Dict, Final, List
from fastapi import Request
from fastapi.responses import JSONResponse
from mcp import Tool
from pydantic import BaseModel
from app.routes.mcp.request import MCPRequest
from app.tools.echo.echotool import EchoTool
from mcp.types import Tool

from tools.types import ListResponse

async def handle_mcp(request: Request, token_info: Dict[str, Any] = None):
    body = await request.json()
    username = token_info.get("preferred_username", "unknown")
    scopes = token_info.get("scopes", [])
    roles = token_info.get("roles", [])
    mcp_request = MCPRequest(**body)
    if mcp_request.method == "ping":
        return {"jsonrpc": "2.0", "id": mcp_request.id, "result": {}}
    
    if mcp_request.id is None:
        return JSONResponse(status_code=202, content=None)
    
     
    
    try:
        if mcp_request.method == "initialize":
            result = {
                "protocolVersion": "2025-06-18",
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "mcp-echo", "version": "0.1.0"}
            }
        elif mcp_request.method == "tools/list":
            tools = await tool_inventory()
            result = {
                "tools": [tool.model_dump() for tool in tools]
            }
        elif mcp_request.method == "tools/call":
            if "superman" not in roles:  
                return JSONResponse(
                    status_code=403,
                    content={"jsonrpc": "2.0", "id": mcp_request.id, "error": {"code": -32601, "message": "Forbidden"}}
                ) 
            try:
                excution_result:ListResponse = await execute_tool(mcp_request.params["name"], mcp_request.params["arguments"])

                result = {
                    "content": [{"type" : "text", "text" :excution_result.model_dump_json()}],  
                    "isError": False,
                    "structuredContent": {
                        "responses": [item.model_dump() for item in excution_result.responses]
                    }  
                }
            except Exception as e:
                result = {
                    "content": [{"type" : "text", "text" : str(e)}],  
                    "isError": True,
                    
                }
        else:
            raise ValueError("Unsupported method")

        return JSONResponse(content={"jsonrpc": "2.0", "id": mcp_request.id, "result": result})

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"jsonrpc": "2.0", "id": mcp_request.id, "error": {"code": -32603, "message": str(e)}}
        )

async def tool_inventory():
    tool_list = [Tool(name=EchoTool.NAME, 
                      title=EchoTool.TITLE, 
                      outputSchema=EchoTool.SCHEMA_OUT.model_json_schema(),
                      description=EchoTool.DESC, 
                      inputSchema=EchoTool.SCHEMA_IN.model_json_schema(), 
                      annotations=EchoTool.ANNOTATIONS)]
    return  tool_list

async def execute_tool(name: str, arguments: Dict[str, Any]):
    if name == EchoTool.NAME:
        return EchoTool.execute(arguments)
    return "NOOP"
