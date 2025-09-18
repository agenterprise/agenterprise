try:
    from app.ext.routes.health.handler import health as extendedHealth
    health=extendedHealth
except (ImportError,ModuleNotFoundError):
    from app.gen.routes.health.handler import handle_health
    health = handle_health