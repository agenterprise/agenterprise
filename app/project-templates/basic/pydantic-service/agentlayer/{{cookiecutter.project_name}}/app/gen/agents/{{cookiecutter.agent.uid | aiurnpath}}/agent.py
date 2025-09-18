from pydantic import BaseModel
from pydantic_ai import Agent
from app.gen.aimodel.modelregistry import BaseModelregistry

class BaseAgent(BaseModel):

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