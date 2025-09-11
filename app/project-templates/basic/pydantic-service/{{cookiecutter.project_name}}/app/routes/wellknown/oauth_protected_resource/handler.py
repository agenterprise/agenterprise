from contextvars import ContextVar
from typing import Final
from fastapi import Request
from fastapi.responses import JSONResponse
from app.auth.keymanager import KeyManager
from app.auth.tokenmanager import TokenManager
import os
KEYCLOAK_URL = os.getenv("KEYCLOAK_URL", "http://keycloak.localhost:8080")
KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM", "mcp-auth")    
auth_url = f"{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}"

async def handle_oauth_protected_resource(request: Request):
      """OAuth 2.0 Protected Resource Metadata (RFC 9728)."""
      return {
            "resource": f'{request.base_url}',
            "authorization_servers": [f'{auth_url}/.well-known/oauth-authorization-server'],
            "scopes_supported": ["mcp-scope"],
            "bearer_methods_supported": ["header"],
            "resource_documentation": f"{request.base_url}docs",
            "mcp_protocol_version": "2025-06-18",
            "resource_type": "mcp-server"
      }

async def handle_oauth_protected_resource_mcp(request: Request):
      """OAuth 2.0 Protected Resource Metadata (RFC 9728)."""
     
      wellknown_url = f"{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}/.well-known/oauth-authorization-server"
      return {
            "resource": f'{request.base_url}mcp',
            "authorization_servers": [f'{auth_url}'],
            "scopes_supported": ["mcp-scope"],
            "bearer_methods_supported": ["header"],
            "resource_documentation": f"{request.base_url}mcp/docs",
            "mcp_protocol_version": "2025-06-18",
            "resource_type": "mcp-server"
      }