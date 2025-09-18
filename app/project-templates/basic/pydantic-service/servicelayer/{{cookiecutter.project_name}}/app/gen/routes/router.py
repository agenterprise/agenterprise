import logging
from app.gen.aiapp import BaseAIApp
from fastapi import Request
from app.gen.routes.health.handler import health
from app.gen.aimodel.modelregistry import BaseModelregistry

logger = logging.getLogger(__name__)

class BaseRouter():
   
    def define_routes(self, app:BaseAIApp, modelregistry: BaseModelregistry):
        @app.get("/health")
        async def health(request: Request):
            return await health(request)
        
        {% for key, agent in cookiecutter.agents.items() %}
        @app.get("/agent/{{agent.name | lower}}/ask/{question}")
        async def {{agent.uid | aiurnvar}}(request: Request, question):  
            from app.gen.agents.{{agent.uid | aiurnpath}}.agent import BaseAgent
            
            return await BaseAgent(modelregistry=modelregistry).ask(question)
        {% endfor %}
      