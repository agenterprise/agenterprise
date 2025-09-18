try:
    from app.ext.routes.router import Router as ExtendedRouter
    Router=ExtendedRouter
except (ImportError,ModuleNotFoundError):
    from app.gen.routes.router import BaseRouter
    Router = BaseRouter