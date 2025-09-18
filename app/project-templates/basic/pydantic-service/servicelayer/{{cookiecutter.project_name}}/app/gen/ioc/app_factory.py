try:
    from app.ext.aiapp import AiApp as ExtendedAiApp
    AIApp=ExtendedAiApp
except (ImportError,ModuleNotFoundError):
    from app.gen.aiapp import BaseAIApp
    AIApp = BaseAIApp