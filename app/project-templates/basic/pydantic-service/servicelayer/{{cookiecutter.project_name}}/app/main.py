from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mcp.server import Server
from app.auth.keymanager import KeyManager
import uvicorn

from app.middleware.http import HttpMiddleware
from app.routes.router import Router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="MCP Echo Server", version="0.1.0")
server = Server("mcp-echo")
km = KeyManager(public_keyfile="public-key.pem")
km.generate_jwk()
middleware = HttpMiddleware(app, server)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
router = Router(app=app, mcpServer=server, keymanager=km)

def main():
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=9000, env_file=".env", log_level="info")

if __name__ == "__main__":
    main()