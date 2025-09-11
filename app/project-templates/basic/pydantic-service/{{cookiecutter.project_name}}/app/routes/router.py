from pydantic import BaseModel
from mcp.server import Server

from typing import Any, Dict, List, Optional
from fastapi import Depends, FastAPI, Request
from mcp.types import Tool, Prompt, PromptArgument, TextContent, PromptMessage, GetPromptResult
from app.auth.keymanager import KeyManager
from app.routes.mcp.handler import handle_mcp, tool_inventory, execute_tool
from app.routes.health.handler import handle_health
from app.routes.wellknown.jwks.handler import handle_jwks   
from app.routes.wellknown.oauth_protected_resource.handler import handle_oauth_protected_resource, handle_oauth_protected_resource_mcp 
from app.routes.wellknown.oauth_authorization_server.handler import handle_oauth_authorization_server   
from app.auth.tokenmanager import TokenManager
class Router():


    def __init__(self, app: FastAPI, mcpServer: Server, keymanager: KeyManager = None):
        self.app = app
        self.mcpServer = mcpServer
        self.tokenManager = TokenManager(keymanager.public_key)
        self.define_routes()

    def define_routes(self):
        
        @self.app.get("/health")
        async def health(request: Request):
            return await handle_health(request)
        
        @self.app.get("/.well-known/jwks.json")
        async def jwks(request: Request):
            return await handle_jwks(request)
        
        @self.app.get("/.well-known/oauth-protected-resource")
        @self.app.options("/.well-known/oauth-protected-resource")
        async def oauth_protected_resource(request: Request):
            return await handle_oauth_protected_resource(request)
        
        @self.app.options("/.well-known/oauth-protected-resource/mcp")
        @self.app.get("/.well-known/oauth-protected-resource/mcp")
        async def oauth_protected_resource_mcp(request: Request):
            return await handle_oauth_protected_resource_mcp(request)
        
        '''
        @self.app.options("/.well-known/oauth-authorization-server")
        @self.app.get("/.well-known/oauth-authorization-server")
        @self.app.options("/.well-known/oauth-authorization-server/mcp")
        @self.app.get("/.well-known/oauth-authorization-server/mcp")
        @self.app.options("/.well-known/openid-configuration")
        @self.app.get("/.well-known/openid-configuration")
        @self.app.options("/.well-known/openid-configuration/mcp")
        @self.app.get("/.well-known/openid-configuration/mcp")
        async def oauth_authorization_server(request: Request):
            return await handle_oauth_authorization_server(request)
        '''
        @self.app.post("/mcp")
        async def handle_mcp_request(request: Request,token_info: Dict[str, Any] = Depends(self.tokenManager.verify_token)):
            return await handle_mcp(request,  token_info=token_info)
        
        
    def define_mcp(self):
        @self.server.list_tools()
        async def list_tools() -> List[Tool]:
            return await tool_inventory()

        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
            return await execute_tool(name,arguments)

        @self.server.list_prompts()
        async def list_prompts() -> List[Prompt]:
            return [Prompt(name="echo_prompt", description="Echo prompt", arguments=[
                PromptArgument(name="message", description="Message", required=True)])]

        @self.server.get_prompt()
        async def get_prompt(name: str, arguments: Optional[Dict[str, str]]) -> GetPromptResult:
            msg = arguments.get("message", "Hello") if arguments else "Hello"
            return GetPromptResult(messages=[
                PromptMessage(role="user", content=[TextContent(type="text", text=f"Please echo: {msg}")])
            ])
    