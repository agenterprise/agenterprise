from pydantic import BaseModel
from pydantic_ai import Agent
from app.gen.domainmodel.agent import AbstractAgent
from app.gen.domainmodel.modelregistry import BaseModelregistry

class BaseAgent(AbstractAgent):

    modelregistry: BaseModelregistry
    systemprompt: str = "{{ cookiecutter.agent.systemprompt }}"
    {% for key, value in cookiecutter.agent.properties.items() %}
    {{ key | aiurnvar }}:str = "{{ value }}"
    {% endfor %}
    llmref:str = "{{ cookiecutter.agent.llmref }}"

    async def ask(self, query: str):
        agent = Agent(  
            model=self.modelregistry.registry[self.llmref],
            instructions=self.systemprompt,  
        )
        result = await agent.run(f"{query}")
        return result 