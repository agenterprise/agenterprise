try:
    from app.ext.aimodel.registry import aimodelregistry as extendedAimodelregistry
    modelregistry=extendedAimodelregistry
except (ImportError,ModuleNotFoundError):
    from app.gen.aimodel.registry import baseAimodelregistry
    modelregistry = baseAimodelregistry