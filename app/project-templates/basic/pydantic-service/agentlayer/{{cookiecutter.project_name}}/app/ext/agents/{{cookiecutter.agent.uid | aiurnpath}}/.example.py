from pydantic import BaseModel
from pydantic_ai import Agent
from app.model.models import Modelregistry
from app.gen.agents.{{cookiecutter.agent.uid | aiurnpath}} import BaseAgent
class CustomAgent(BaseAgent):
   
    async def ask(self, query: str):
        # do my stuff here
        result = await super.ask(f"{query}")
        return result 