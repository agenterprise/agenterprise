from contextvars import ContextVar
from typing import Final
from fastapi import Request
from fastapi.responses import JSONResponse
from app.auth.keymanager import KeyManager

async def handle_jwks(request: Request):
   """JSON Web Key Set endpoint."""

   km = KeyManager()
   if km:
         return {"keys": km.public_key_jwk}
   else:
         return JSONResponse(
            status_code=503,
            content={"error": "JWKS not available - no public key loaded"}
         )