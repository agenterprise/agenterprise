from antlr4 import ParseTreeListener
from app.agent_grammer.parser.ai_environmentListener import ai_environmentListener
from app.agent_grammer.parser.ai_environmentParser import ai_environmentParser
from app.model.data.ai_environment import AIEnvironment
from app.model.listener.AIURN import AIURN


class BasicServiceListener(ai_environmentListener):
    def __init__(self):
        self.app_pattern = None
        self.techstack = None
        self.environment = None
    
    def enterAiStack(self, ctx):
        self.ai_techstack = ctx.TECHSTACK_AIURN().getText()

    def enterServiceStack(self, ctx):
        self.service_techstack = ctx.TECHSTACK_AIURN().getText()
 
    def exitEnvid(self, ctx):
        self.envid = ctx.STRING().getText().strip('"')


    def exitAi_envDef(self, ctx):
        self.environment = AIEnvironment(
            name=ctx.STRING().getText().strip('"'),
            ai_techstack=AIURN(self.ai_techstack),
            service_techstack=AIURN(self.service_techstack),
            envid=self.envid,
            agents=[],
            llms=[]
        )

