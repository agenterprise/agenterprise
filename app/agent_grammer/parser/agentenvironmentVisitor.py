# Generated from app/agent_grammer/parser/agentenvironment.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .agentenvironmentParser import agentenvironmentParser
else:
    from agentenvironmentParser import agentenvironmentParser

# This class defines a complete generic visitor for a parse tree produced by agentenvironmentParser.

class agentenvironmentVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by agentenvironmentParser#env.
    def visitEnv(self, ctx:agentenvironmentParser.EnvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by agentenvironmentParser#envDef.
    def visitEnvDef(self, ctx:agentenvironmentParser.EnvDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by agentenvironmentParser#environmentProperty.
    def visitEnvironmentProperty(self, ctx:agentenvironmentParser.EnvironmentPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by agentenvironmentParser#prog.
    def visitProg(self, ctx:agentenvironmentParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by agentenvironmentParser#agentDef.
    def visitAgentDef(self, ctx:agentenvironmentParser.AgentDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by agentenvironmentParser#systemPromptProperty.
    def visitSystemPromptProperty(self, ctx:agentenvironmentParser.SystemPromptPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by agentenvironmentParser#agentIdentity.
    def visitAgentIdentity(self, ctx:agentenvironmentParser.AgentIdentityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by agentenvironmentParser#agentNamespace.
    def visitAgentNamespace(self, ctx:agentenvironmentParser.AgentNamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by agentenvironmentParser#otherAgentProperty.
    def visitOtherAgentProperty(self, ctx:agentenvironmentParser.OtherAgentPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by agentenvironmentParser#agentProperty.
    def visitAgentProperty(self, ctx:agentenvironmentParser.AgentPropertyContext):
        return self.visitChildren(ctx)



del agentenvironmentParser