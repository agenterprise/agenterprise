from agenterprise.agent_grammer.parser.ai_environmentListener import  ai_environmentListener
from agenterprise.model.data.ai_environment import Entity
from agenterprise.model.listener.AIURN import AIURN

class BaseAIEntityListener(ai_environmentListener):
    def __init__(self):
        super().__init__()
        self.entites = []
        self.current_entity = None
        self.current_element= None

    def enterEntityDef(self, ctx):
        super().enterEntityDef(ctx)
        self.current_entity = {
            "name": ctx.PROPERTYVALUE().getText(),
            "uid": None,
            "elements": []
        }
    def enterEntityElementProp(self, ctx):
        super().enterEntityElementProp(ctx)
        self.current_element = {
            "description" : "",
            "type": "",
            "ref" : "",
            "aiurn": AIURN(ctx.ENTITY_VAR().getText())
        }
    def enterEntityIdProp(self, ctx):
        super().enterEntityIdProp(ctx)
        self.current_entity["uid"]=ctx.ENTITY_ID().getText()

    def exitEntityElementProp(self, ctx):
        super().exitEntityElementProp(ctx)
       
        self.current_entity["elements"].append(self.current_element)

    def enterEntityElementDescription(self, ctx):
        super().enterEntityElementDescription(ctx)
        self.current_element['description'] = ctx.PROPERTYVALUE().getText()

    def enterEntityElementType(self, ctx):
        super().enterEntityElementType(ctx)
        if ctx.ENTITY_ID():
            self.current_element['ref'] = ctx.ENTITY_ID().getText()
        if ctx.ENTITY_TYPE():
            self.current_element['type'] = ctx.ENTITY_TYPE().getText()
    
    def exitEntityDef(self, ctx):
        super().exitEntityDef(ctx)
        entity = Entity(
            name=self.current_entity.get("name"),
            uid=AIURN(self.current_entity.get("uid")),
            elements=self.current_entity.get("elements")
        )
        self.entites.append(entity)
        self.current_entity = None

    