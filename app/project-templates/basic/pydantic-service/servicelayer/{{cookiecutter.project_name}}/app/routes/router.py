from fastapi import FastAPI, Request
from app.routes.health.handler import handle_health

class Router():
    def __init__(self, app: FastAPI):
        self.app = app
        self.define_routes()

    def define_routes(self):
        @self.app.get("/health")
        async def health(request: Request):
            return await handle_health(request)
        
        
        {% for key, agent in cookiecutter.agents.items() %}
        @self.app.get("/agent/{{agent.name | lower}}/ask/{question}")
        async def {{agent.uid | aiurnvar}}(request: Request, question):  
            from app.agents.{{agent.uid | aiurnpath}}.agent import BaseAgent
            return BaseAgent().ask(question)
        {% endfor %}
      