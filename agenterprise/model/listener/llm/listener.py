from agenterprise.agent_grammer.parser.ai_environmentListener import  ai_environmentListener
from agenterprise.model.data.ai_environment import Agent
from agenterprise.model.data.ai_environment import LLM
from agenterprise.model.listener.AIURN import AIURN

class BaseAILLMListener(ai_environmentListener):
    def __init__(self):
        super().__init__()
        self.llms = []
        self.current_llm = None

    def enterLlmDef(self, ctx):
        super().enterLlmDef(ctx)
        self.current_llm = {
            "name": ctx.PROPERTYVALUE().getText(),
            "properties" : {
               
            }
        
        }

    def enterLlmIdProp(self, ctx):
        super().enterLlmIdProp(ctx)
        self.current_llm["uid"] = ctx.LLMID().getText()
    def enterLlmEndpointProp(self, ctx):
        super().enterLlmEndpointProp(ctx)
        self.current_llm["endpoint"] = ctx.PROPERTYVALUE().getText()

    def enterLlmModelProp(self, ctx):
        super().enterLlmModelProp(ctx)
        self.current_llm["model"] = ctx.PROPERTYVALUE().getText()

    def enterLlmVersionProp(self, ctx):
        super().enterLlmVersionProp(ctx)   
        self.current_llm["version"] = ctx.PROPERTYVALUE().getText()

    def enterLlmProviderProp(self, ctx):
        super().enterLlmProviderProp(ctx) 
        self.current_llm["provider"] = ctx.LLMPROVIDER().getText() 

    def enterLlmOtherProperty(self, ctx):
        super().enterLlmOtherProperty(ctx)
        var_name = ctx.VAR().getText()
        var_value = ctx.PROPERTYVALUE().getText() 
        
        self.current_llm["properties"][AIURN(var_name)] = var_value
    

    def exitLlmDef(self, ctx):
        super().exitLlmDef(ctx)
        llm = LLM(
            name=self.current_llm.get("name"),
            uid=AIURN(self.current_llm.get("uid")),
            provider=AIURN(self.current_llm.get("provider")),
            model=self.current_llm.get("model"),
            endpoint=self.current_llm.get("endpoint"),
            version=self.current_llm.get("version"),
            properties=self.current_llm.get("properties")
        )
        self.llms.append(llm)
        self.current_llm = None

  