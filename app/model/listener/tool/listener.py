from app.agent_grammer.parser.ai_environmentListener import  ai_environmentListener
from app.model.data.ai_environment import Agent, Tool
from app.model.listener.AIURN import AIURN

class BaseAIToolListener(ai_environmentListener):
    def __init__(self):
        super().__init__()
        self.tools = []
        self.current_tool = None

    def enterToolDef(self, ctx):
         self.current_tool = {
            "name": ctx.STRING().getText().strip('"'),
            "uid": "",
            "endpoint": "",
            "type": "",
            "description" : "",
            "properties": {}
        }
    def enterToolIdProp(self, ctx):
        super().enterToolIdProp(ctx)
        self.current_tool["uid"] = ctx.TOOLID().getText()

    def enterToolEndpointProp(self, ctx):
        super().enterToolEndpointProp(ctx)
        self.current_tool["endpoint"] = ctx.STRING().getText()

    def enterToolDescriptionProp(self, ctx):
        super().enterToolDescriptionProp(ctx)
        self.current_tool["description"] = ctx.STRING().getText()

    def enterToolTypeProp(self, ctx):
        super().enterToolEndpointProp(ctx)
        self.current_tool["type"] = ctx.TOOL_TYPE().getText()
    

    def exitToolDef(self, ctx):
        super().exitToolDef(ctx)
 
        tool = Tool(
            name=self.current_tool.get("name"),
            uid=AIURN(self.current_tool.get("uid")),
            description=self.current_tool.get("description"),
            toolrefs=self.current_tool.get("toolrefs"),
            endpoint=self.current_tool.get("endpoint"),
            type = self.current_tool.get("type"),
            properties=self.current_tool.get("properties", {})
        )
        self.tools.append(tool)
        self.tool = None

   
