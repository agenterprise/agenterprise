from fastapi import FastAPI 
from app.gen.ioc.IoCContainer import IoCContainer


class BaseAIApp(FastAPI):
    
    def __init__(self, iocContainer:IoCContainer, **extra):
        super().__init__(**extra)   
        self.gen_middleware = iocContainer
        self.gen_router= iocContainer.router
        self.gen_modelregistry = iocContainer.modelregistry
        self.gen_toolregistry = iocContainer.toolregistry
        self.gen_middleware = iocContainer.middleware

        self.gen_middleware.define_middleware(app=self)
        self.gen_router.define_routes(app=self, modelregistry=self.gen_modelregistry)

        


    