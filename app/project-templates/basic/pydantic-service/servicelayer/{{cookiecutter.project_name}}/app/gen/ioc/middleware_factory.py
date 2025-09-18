try:
    from app.ext.middleware.http import HttpMiddleware as ExtendedHttpMiddleware
    HttpMiddleware=ExtendedHttpMiddleware
except (ImportError,ModuleNotFoundError):
    from app.gen.middleware.http import BaseHttpMiddleware
    HttpMiddleware = BaseHttpMiddleware