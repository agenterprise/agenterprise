from antlr4 import ParseTreeListener
from agenterprise.agent_grammer.parser.ai_environmentListener import ai_environmentListener
from agenterprise.agent_grammer.parser.ai_environmentParser import ai_environmentParser
from agenterprise.model.data.ai_environment import AIEnvironment
from agenterprise.model.listener.AIURN import AIURN


class NonFunctionalListener(ai_environmentListener):
    def __init__(self):
        self.ai_techstack = None
        self.service_techstack = None
        self.project_techstack = None
        self.environment = None
        self.envid = None
    
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
