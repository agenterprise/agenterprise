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
        
        {% for key, agent in cookiecutter.agents.items() %}
        @self.app.get("/agent/{{agent.name | lower}}/info")
        async def {{agent.uid | aiurnvar}}(request: Request):  
            import app.agents.{{agent.uid | aiurnpath}}.agent as agent
            pass
        {% endfor %}
      