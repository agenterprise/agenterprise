from antlr4 import ParseTreeListener
from app.agent_grammer.parser.ai_environmentListener import ai_environmentListener
from app.agent_grammer.parser.ai_environmentParser import ai_environmentParser
from app.model.data.ai_environment import AIEnvironment


class NonFunctionalListener(ai_environmentListener):
    def __init__(self):
        self.deploymentpattern = None
        self.techstack = None
        self.environment = None
    
    def exitDeploymentPattern(self, ctx):
        self.deploymentpattern = ctx.DEPLOYMENT().getText().strip('"')

    def exitTechstack(self, ctx):
        self.techstack = ctx.TECHSTACK_AIURN().getText().strip('"')

    def exitAi_envDef(self, ctx):
        self.environment = AIEnvironment(
            name=ctx.STRING().getText().strip('"'),
            deployment=self.deploymentpattern,
            techstack=self.techstack,
            agents=[],
            llms=[]
        )
