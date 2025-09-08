# Generated from app/agent_grammer/parser/agentenvironment.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .agentenvironmentParser import agentenvironmentParser
else:
    from agentenvironmentParser import agentenvironmentParser

# This class defines a complete listener for a parse tree produced by agentenvironmentParser.
class agentenvironmentListener(ParseTreeListener):

    # Enter a parse tree produced by agentenvironmentParser#env.
    def enterEnv(self, ctx:agentenvironmentParser.EnvContext):
        pass

    # Exit a parse tree produced by agentenvironmentParser#env.
    def exitEnv(self, ctx:agentenvironmentParser.EnvContext):
        pass


    # Enter a parse tree produced by agentenvironmentParser#envDef.
    def enterEnvDef(self, ctx:agentenvironmentParser.EnvDefContext):
        pass

    # Exit a parse tree produced by agentenvironmentParser#envDef.
    def exitEnvDef(self, ctx:agentenvironmentParser.EnvDefContext):
        pass


    # Enter a parse tree produced by agentenvironmentParser#environmentProperty.
    def enterEnvironmentProperty(self, ctx:agentenvironmentParser.EnvironmentPropertyContext):
        pass

    # Exit a parse tree produced by agentenvironmentParser#environmentProperty.
    def exitEnvironmentProperty(self, ctx:agentenvironmentParser.EnvironmentPropertyContext):
        pass


    # Enter a parse tree produced by agentenvironmentParser#prog.
    def enterProg(self, ctx:agentenvironmentParser.ProgContext):
        pass

    # Exit a parse tree produced by agentenvironmentParser#prog.
    def exitProg(self, ctx:agentenvironmentParser.ProgContext):
        pass


    # Enter a parse tree produced by agentenvironmentParser#agentDef.
    def enterAgentDef(self, ctx:agentenvironmentParser.AgentDefContext):
        pass

    # Exit a parse tree produced by agentenvironmentParser#agentDef.
    def exitAgentDef(self, ctx:agentenvironmentParser.AgentDefContext):
        pass


    # Enter a parse tree produced by agentenvironmentParser#systemPromptProperty.
    def enterSystemPromptProperty(self, ctx:agentenvironmentParser.SystemPromptPropertyContext):
        pass

    # Exit a parse tree produced by agentenvironmentParser#systemPromptProperty.
    def exitSystemPromptProperty(self, ctx:agentenvironmentParser.SystemPromptPropertyContext):
        pass


    # Enter a parse tree produced by agentenvironmentParser#agentIdentity.
    def enterAgentIdentity(self, ctx:agentenvironmentParser.AgentIdentityContext):
        pass

    # Exit a parse tree produced by agentenvironmentParser#agentIdentity.
    def exitAgentIdentity(self, ctx:agentenvironmentParser.AgentIdentityContext):
        pass


    # Enter a parse tree produced by agentenvironmentParser#agentNamespace.
    def enterAgentNamespace(self, ctx:agentenvironmentParser.AgentNamespaceContext):
        pass

    # Exit a parse tree produced by agentenvironmentParser#agentNamespace.
    def exitAgentNamespace(self, ctx:agentenvironmentParser.AgentNamespaceContext):
        pass


    # Enter a parse tree produced by agentenvironmentParser#otherAgentProperty.
    def enterOtherAgentProperty(self, ctx:agentenvironmentParser.OtherAgentPropertyContext):
        pass

    # Exit a parse tree produced by agentenvironmentParser#otherAgentProperty.
    def exitOtherAgentProperty(self, ctx:agentenvironmentParser.OtherAgentPropertyContext):
        pass


    # Enter a parse tree produced by agentenvironmentParser#agentProperty.
    def enterAgentProperty(self, ctx:agentenvironmentParser.AgentPropertyContext):
        pass

    # Exit a parse tree produced by agentenvironmentParser#agentProperty.
    def exitAgentProperty(self, ctx:agentenvironmentParser.AgentPropertyContext):
        pass



del agentenvironmentParser