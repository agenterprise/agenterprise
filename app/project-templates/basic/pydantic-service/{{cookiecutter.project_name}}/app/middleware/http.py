from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mcp.server import Server


class HttpMiddleware():
    """Middleware to validate Origin header according to MCP specification.
    This prevents DNS rebinding attacks by ensuring requests come from trusted origins."""

    def __init__(self, app: FastAPI, mcpServer: Server):
        self.app = app
        self.mcpServer = mcpServer
        self.define_middleware()

    def define_middleware(self):
        @self.app.middleware("http")
        async def origin_validation_middleware(request: Request, call_next):
            """
            Middleware to validate Origin header according to MCP specification.
            This prevents DNS rebinding attacks by ensuring requests come from trusted origins.
            """
            # Skip validation for health check endpoint (optional)
            if request.url.path == "/health":
                response = await call_next(request)
                return response
            
            # Get the Origin header
            origin = request.headers.get("origin")
            
            if not origin:
                print("✅ No Origin header - allowing for MCP client")
                response = await call_next(request)
                return response
            # Validate the origin - allow localhost and 127.0.0.1 on any port
            if not origin or (not origin.startswith("http://localhost") and not origin.startswith("http://127.0.0.1")):
                return JSONResponse(
                    status_code=403,
                    content={"detail": f"Origin '{origin}' is not allowed. Only localhost and 127.0.0.1 are permitted."}
                )
            
            response = await call_next(request)
            return response


                