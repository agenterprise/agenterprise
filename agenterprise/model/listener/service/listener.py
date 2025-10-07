from antlr4 import ParseTreeListener
from agenterprise.agent_grammer.parser.ai_environmentListener import ai_environmentListener
from agenterprise.agent_grammer.parser.ai_environmentParser import ai_environmentParser
from agenterprise.model.data.ai_environment import AIEnvironment
from agenterprise.model.listener.AIURN import AIURN


class BasicServiceListener(ai_environmentListener):
    def __init__(self):
        self.app_pattern = None
        self.service_techlayer = None
        self.data_techlayer=None
        self.ai_techlayer = None
        self.environment = None

    def enterArchitectureAiStack(self, ctx):
        super().enterArchitectureAiStack(ctx)
        self.ai_techlayer = ctx.TECHLAYER_AIURN().getText()

    def enterArchitectureServiceStack(self, ctx):
        super().enterArchitectureServiceStack(ctx)
        self.service_techlayer = ctx.TECHLAYER_AIURN().getText()
    
    def enterArchitectureDataStack(self, ctx):
        super().enterArchitectureDataStack(ctx)
        self.data_techlayer = ctx.TECHLAYER_AIURN().getText()
 
    def exitEnvId(self, ctx):
        super().exitEnvId(ctx)
        self.envId = ctx.PROPERTYVALUE().getText()

    
    def exitAi_envDef(self, ctx):
        super().exitAi_envDef(ctx)
        self.environment = AIEnvironment(
            name=ctx.PROPERTYVALUE().getText(),
            ai_techlayer=AIURN(self.ai_techlayer),
            service_techlayer=AIURN(self.service_techlayer),
            data_techlayer=AIURN(self.data_techlayer),
            envid=self.envId,
            agents=[],
            llms=[]
        )

