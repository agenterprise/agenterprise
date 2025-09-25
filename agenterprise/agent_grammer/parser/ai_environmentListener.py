# Generated from app/agent_grammer/parser/ai_environment.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ai_environmentParser import ai_environmentParser
else:
    from ai_environmentParser import ai_environmentParser

# This class defines a complete listener for a parse tree produced by ai_environmentParser.
class ai_environmentListener(ParseTreeListener):

    # Enter a parse tree produced by ai_environmentParser#ai_envDef.
    def enterAi_envDef(self, ctx:ai_environmentParser.Ai_envDefContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#ai_envDef.
    def exitAi_envDef(self, ctx:ai_environmentParser.Ai_envDefContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#envid.
    def enterEnvid(self, ctx:ai_environmentParser.EnvidContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#envid.
    def exitEnvid(self, ctx:ai_environmentParser.EnvidContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#serviceStack.
    def enterServiceStack(self, ctx:ai_environmentParser.ServiceStackContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#serviceStack.
    def exitServiceStack(self, ctx:ai_environmentParser.ServiceStackContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#aiStack.
    def enterAiStack(self, ctx:ai_environmentParser.AiStackContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#aiStack.
    def exitAiStack(self, ctx:ai_environmentParser.AiStackContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#llmSet.
    def enterLlmSet(self, ctx:ai_environmentParser.LlmSetContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#llmSet.
    def exitLlmSet(self, ctx:ai_environmentParser.LlmSetContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#llmDef.
    def enterLlmDef(self, ctx:ai_environmentParser.LlmDefContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#llmDef.
    def exitLlmDef(self, ctx:ai_environmentParser.LlmDefContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#llmIdProp.
    def enterLlmIdProp(self, ctx:ai_environmentParser.LlmIdPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#llmIdProp.
    def exitLlmIdProp(self, ctx:ai_environmentParser.LlmIdPropContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#llmProviderProp.
    def enterLlmProviderProp(self, ctx:ai_environmentParser.LlmProviderPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#llmProviderProp.
    def exitLlmProviderProp(self, ctx:ai_environmentParser.LlmProviderPropContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#llmModelProp.
    def enterLlmModelProp(self, ctx:ai_environmentParser.LlmModelPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#llmModelProp.
    def exitLlmModelProp(self, ctx:ai_environmentParser.LlmModelPropContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#llmEndpointProp.
    def enterLlmEndpointProp(self, ctx:ai_environmentParser.LlmEndpointPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#llmEndpointProp.
    def exitLlmEndpointProp(self, ctx:ai_environmentParser.LlmEndpointPropContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#llmVersionProp.
    def enterLlmVersionProp(self, ctx:ai_environmentParser.LlmVersionPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#llmVersionProp.
    def exitLlmVersionProp(self, ctx:ai_environmentParser.LlmVersionPropContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#llmOtherProperty.
    def enterLlmOtherProperty(self, ctx:ai_environmentParser.LlmOtherPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#llmOtherProperty.
    def exitLlmOtherProperty(self, ctx:ai_environmentParser.LlmOtherPropertyContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#prog.
    def enterProg(self, ctx:ai_environmentParser.ProgContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#prog.
    def exitProg(self, ctx:ai_environmentParser.ProgContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#agentDef.
    def enterAgentDef(self, ctx:ai_environmentParser.AgentDefContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentDef.
    def exitAgentDef(self, ctx:ai_environmentParser.AgentDefContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#systemPromptProperty.
    def enterSystemPromptProperty(self, ctx:ai_environmentParser.SystemPromptPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#systemPromptProperty.
    def exitSystemPromptProperty(self, ctx:ai_environmentParser.SystemPromptPropertyContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#agentIdentity.
    def enterAgentIdentity(self, ctx:ai_environmentParser.AgentIdentityContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentIdentity.
    def exitAgentIdentity(self, ctx:ai_environmentParser.AgentIdentityContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#agentNamespace.
    def enterAgentNamespace(self, ctx:ai_environmentParser.AgentNamespaceContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentNamespace.
    def exitAgentNamespace(self, ctx:ai_environmentParser.AgentNamespaceContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#llmRefProperty.
    def enterLlmRefProperty(self, ctx:ai_environmentParser.LlmRefPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#llmRefProperty.
    def exitLlmRefProperty(self, ctx:ai_environmentParser.LlmRefPropertyContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#toolRefProperty.
    def enterToolRefProperty(self, ctx:ai_environmentParser.ToolRefPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#toolRefProperty.
    def exitToolRefProperty(self, ctx:ai_environmentParser.ToolRefPropertyContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#otherAgentProperty.
    def enterOtherAgentProperty(self, ctx:ai_environmentParser.OtherAgentPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#otherAgentProperty.
    def exitOtherAgentProperty(self, ctx:ai_environmentParser.OtherAgentPropertyContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#agentProperty.
    def enterAgentProperty(self, ctx:ai_environmentParser.AgentPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentProperty.
    def exitAgentProperty(self, ctx:ai_environmentParser.AgentPropertyContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#toolSet.
    def enterToolSet(self, ctx:ai_environmentParser.ToolSetContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#toolSet.
    def exitToolSet(self, ctx:ai_environmentParser.ToolSetContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#toolDef.
    def enterToolDef(self, ctx:ai_environmentParser.ToolDefContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#toolDef.
    def exitToolDef(self, ctx:ai_environmentParser.ToolDefContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#toolIdProp.
    def enterToolIdProp(self, ctx:ai_environmentParser.ToolIdPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#toolIdProp.
    def exitToolIdProp(self, ctx:ai_environmentParser.ToolIdPropContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#toolEndpointProp.
    def enterToolEndpointProp(self, ctx:ai_environmentParser.ToolEndpointPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#toolEndpointProp.
    def exitToolEndpointProp(self, ctx:ai_environmentParser.ToolEndpointPropContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#toolDescription.
    def enterToolDescription(self, ctx:ai_environmentParser.ToolDescriptionContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#toolDescription.
    def exitToolDescription(self, ctx:ai_environmentParser.ToolDescriptionContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#toolTypeProp.
    def enterToolTypeProp(self, ctx:ai_environmentParser.ToolTypePropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#toolTypeProp.
    def exitToolTypeProp(self, ctx:ai_environmentParser.ToolTypePropContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#toolOtherProperty.
    def enterToolOtherProperty(self, ctx:ai_environmentParser.ToolOtherPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#toolOtherProperty.
    def exitToolOtherProperty(self, ctx:ai_environmentParser.ToolOtherPropertyContext):
        pass



del ai_environmentParser