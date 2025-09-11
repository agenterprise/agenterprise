import os
from fastapi import Request

async def handle_oauth_authorization_server(request: Request):
    """OAuth 2.0 Authorization Server Metadata. OpenID Connect Discovery 1.0"""

    KEYCLOAK_URL = os.getenv("KEYCLOAK_URL", "http://localhost:8080")
    KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM", "mcp-auth")    
    auth_url = f"{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}"
    return {
        "issuer": f"{auth_url}",
        "authorization_endpoint": f"{auth_url}/protocol/openid-connect/auth",
        "token_endpoint": f"{auth_url}/protocol/openid-connect/token",
        "introspection_endpoint": f"{auth_url}/protocol/openid-connect/token/introspect",

        "device_authorization_endpoint": f"{auth_url}/oauth/device/code",
        "mfa_challenge_endpoint": f"{auth_url}/mfa/challenge",
        "userinfo_endpoint": f"{auth_url}/userinfo",
        "jwks_uri": f"{auth_url}/.well-known/jwks.json",
        "registration_endpoint": f"{auth_url}/clients-registrations/openid-connect",
        "response_types_supported": ["code", "token", "id_token", "code token", "code id_token"],
        "subject_types_supported": ["public"],
        "id_token_signing_alg_values_supported": ["RS256"],
        "scopes_supported": ["openid", "profile", "email"],
        "claims_supported": ["sub", "iss", "aud", "exp", "iat", "name", "email"],
        "grant_types_supported": ["authorization_code", "implicit", "refresh_token", "client_credentials"],
        "revocation_endpoint": f"{auth_url}/oauth/revoke",
        "code_challenge_methods_supported": ["S256"]  # PKCE Unterstützung
    }

