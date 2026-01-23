from agenterprise.agent_grammer.parser.ai_environmentListener import  ai_environmentListener
from agenterprise.model.data.ai_environment import Agent
from agenterprise.model.listener.AIURN import AIURN

class BaseAIAgentListener(ai_environmentListener):
    def __init__(self):
        super().__init__()
        self.agents = []
        self.current_agent = None

    def enterAgentDef(self, ctx):
        super().enterAgentDef(ctx)
        self.current_agent = {
            "name": ctx.PROPERTYVALUE().getText(),
            "uid": None,
            "namespace": None,
            "systemprompt": None,
            "description": None,
            "examples": [],
            "tags": [],
            "toolrefs": [],
            "inputproperties": {},
            "outputproperties": {},
            "properties": {}
        }
    def enterAgentToolRefProperty(self, ctx):
        self.current_agent["toolrefs"].append(ctx.TOOLID().getText())
    def exitAgentDef(self, ctx):
        super().exitAgentDef(ctx)
        agent = Agent(
            name=self.current_agent.get("name"),
            uid=AIURN(self.current_agent.get("uid")),
            namespace=AIURN(self.current_agent.get("namespace")),
            systemprompt=self.current_agent.get("systemprompt"),
            description=self.current_agent.get("description", "No description"),
            tags=self.current_agent.get("tags", []),
            examples=self.current_agent.get("examples", []),
            llmref=AIURN(self.current_agent.get("llmref")),
            toolrefs=[ AIURN(x) for x in self.current_agent["toolrefs"]],
            properties=self.current_agent.get("properties", {}),
            output=self.current_agent.get("output"),
            input=self.current_agent.get("input")
        )
        self.agents.append(agent)
        self.current_agent = None

    def enterAgentIdentity(self, ctx):
        super().enterAgentIdentity(ctx)
        if self.current_agent is not None and ctx.AGENTID():
            self.current_agent["uid"] = ctx.AGENTID().getText()

    def enterAgentExampleProp(self, ctx):
        self.current_agent["examples"].append(ctx.PROPERTYVALUE().getText().strip('"'))
    
    def enterAgentTagsProp(self, ctx):
        self.current_agent["tags"].append(ctx.PROPERTYVALUE().getText().strip('"'))

    def enterAgentDescriptionProp(self, ctx):
        super().enterAgentDescriptionProp(ctx)
        if self.current_agent is not None:
            self.current_agent["description"] = ctx.PROPERTYVALUE().getText().strip('"')

    def enterAgentNamespace(self, ctx):
        super().enterAgentNamespace(ctx)
        if self.current_agent is not None and ctx.AGENTNAMESPACE():
            self.current_agent["namespace"] = ctx.AGENTNAMESPACE().getText()

    def enterAgentLLMRefProperty(self, ctx):
        super().enterAgentLLMRefProperty(ctx)
        if self.current_agent is not None and ctx.LLMID():
            self.current_agent["llmref"] = ctx.LLMID().getText()
   
    def enterAgentSystemPromptProperty(self, ctx):
        super().enterAgentSystemPromptProperty(ctx)
        if self.current_agent is not None:
            self.current_agent["systemprompt"] = ctx.PROPERTYVALUE().getText().strip('"')  

    def enterAgentInputProperty(self, ctx):
        super().enterAgentInputProperty(ctx)
        var = ctx.ENTITY_ID().getText()
        self.current_agent["input"]= AIURN(var)

    def enterAgentOutputProperty(self, ctx):
        super().enterAgentOutputProperty(ctx)
        var = ctx.ENTITY_ID().getText()
        self.current_agent["output"] = AIURN(var)

    def enterAgentCustomProperty(self, ctx):
        super().enterAgentCustomProperty(ctx)
        if self.current_agent is not None and ctx.VAR():
            key = AIURN(ctx.VAR().getText())
            value = ctx.PROPERTYVALUE().getText()
            self.current_agent["properties"][key] = value