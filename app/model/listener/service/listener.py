from antlr4 import ParseTreeListener
from app.agent_grammer.parser.ai_environmentListener import ai_environmentListener
from app.agent_grammer.parser.ai_environmentParser import ai_environmentParser
from app.model.data.ai_environment import AIEnvironment


class BasicServiceListener(ai_environmentListener):
    def __init__(self):
        self.app_pattern = None
        self.techstack = None
        self.environment = None
    
    def exitAppPattern(self, ctx):
        self.app_pattern = ctx.APP().getText().strip('"')
    
    def exitTechstack(self, ctx):
        self.techstack = ctx.TECHSTACK_AIURN().getText().strip('"')

    def exitEnvid(self, ctx):
        self.envid = ctx.STRING().getText().strip('"')

    def exitAi_envDef(self, ctx):
        self.environment = AIEnvironment(
            name=ctx.STRING().getText().strip('"'),
            app_pattern=self.app_pattern,
            techstack=self.techstack,
            envid=self.envid,
            agents=[],
            llms=[]
        )

