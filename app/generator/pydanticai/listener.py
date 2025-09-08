from app.agent_grammer.parser.agentenvironmentListener import agentenvironmentListener
from app.datamodel.agent import Agent

class PydanticAIListener(agentenvironmentListener):
    def __init__(self):
        super().__init__()
        self.agents = []
        self.current_agent = None

    def enterAgentDef(self, ctx):
        super().enterAgentDef(ctx)
        self.current_agent = {
            "name": ctx.STRING().getText().strip('"'),
            "uid": None,
            "namespace": None,
            "systemprompt": None,
            "properties": {}
        }

    def exitAgentDef(self, ctx):
        super().exitAgentDef(ctx)
        agent = Agent(
            name=self.current_agent.get("name"),
            uid=self.current_agent.get("uid"),
            namespace=self.current_agent.get("namespace"),
            systemprompt=self.current_agent.get("systemprompt"),
            properties=self.current_agent.get("properties", {})
        )
        self.agents.append(agent)
        self.current_agent = None

    def enterAgentIdentity(self, ctx):
        super().enterAgentIdentity(ctx)
        if self.current_agent is not None and ctx.ID():
            self.current_agent["uid"] = ctx.ID().getText()

    def enterAgentNamespace(self, ctx):
        super().enterAgentNamespace(ctx)
        if self.current_agent is not None and ctx.ID():
            self.current_agent["namespace"] = ctx.ID().getText()

    def enterSystemPromptProperty(self, ctx):
        super().enterSystemPromptProperty(ctx)
        if self.current_agent is not None:
            self.current_agent["systemprompt"] = ctx.STRING().getText().strip('"')

    def enterAgentProperty(self, ctx):
        super().enterAgentProperty(ctx)
        if self.current_agent is not None and ctx.ID():
            key = ctx.ID().getText()
            value = ctx.STRING().getText().strip('"')
            self.current_agent["properties"][key] = value
        elif ctx.getChild(0).getText() == "prompt":
            value = ctx.STRING().getText().strip('"')
            self.current_agent["properties"]["prompt"] = value
        elif ctx.getChild(0).getText() == "systemprompt":
            value = ctx.STRING().getText().strip('"')
            self.current_agent["properties"]["systemprompt"] = value
