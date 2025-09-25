# Generated from app/agent_grammer/parser/ai_environment.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ai_environmentParser import ai_environmentParser
else:
    from ai_environmentParser import ai_environmentParser

# This class defines a complete generic visitor for a parse tree produced by ai_environmentParser.

class ai_environmentVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ai_environmentParser#ai_envDef.
    def visitAi_envDef(self, ctx:ai_environmentParser.Ai_envDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#envid.
    def visitEnvid(self, ctx:ai_environmentParser.EnvidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#serviceStack.
    def visitServiceStack(self, ctx:ai_environmentParser.ServiceStackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#aiStack.
    def visitAiStack(self, ctx:ai_environmentParser.AiStackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#llmSet.
    def visitLlmSet(self, ctx:ai_environmentParser.LlmSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#llmDef.
    def visitLlmDef(self, ctx:ai_environmentParser.LlmDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#llmIdProp.
    def visitLlmIdProp(self, ctx:ai_environmentParser.LlmIdPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#llmProviderProp.
    def visitLlmProviderProp(self, ctx:ai_environmentParser.LlmProviderPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#llmModelProp.
    def visitLlmModelProp(self, ctx:ai_environmentParser.LlmModelPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#llmEndpointProp.
    def visitLlmEndpointProp(self, ctx:ai_environmentParser.LlmEndpointPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#llmVersionProp.
    def visitLlmVersionProp(self, ctx:ai_environmentParser.LlmVersionPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#llmOtherProperty.
    def visitLlmOtherProperty(self, ctx:ai_environmentParser.LlmOtherPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#prog.
    def visitProg(self, ctx:ai_environmentParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentDef.
    def visitAgentDef(self, ctx:ai_environmentParser.AgentDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#systemPromptProperty.
    def visitSystemPromptProperty(self, ctx:ai_environmentParser.SystemPromptPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentIdentity.
    def visitAgentIdentity(self, ctx:ai_environmentParser.AgentIdentityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentNamespace.
    def visitAgentNamespace(self, ctx:ai_environmentParser.AgentNamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#llmRefProperty.
    def visitLlmRefProperty(self, ctx:ai_environmentParser.LlmRefPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolRefProperty.
    def visitToolRefProperty(self, ctx:ai_environmentParser.ToolRefPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#otherAgentProperty.
    def visitOtherAgentProperty(self, ctx:ai_environmentParser.OtherAgentPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentProperty.
    def visitAgentProperty(self, ctx:ai_environmentParser.AgentPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolSet.
    def visitToolSet(self, ctx:ai_environmentParser.ToolSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolDef.
    def visitToolDef(self, ctx:ai_environmentParser.ToolDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolIdProp.
    def visitToolIdProp(self, ctx:ai_environmentParser.ToolIdPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolEndpointProp.
    def visitToolEndpointProp(self, ctx:ai_environmentParser.ToolEndpointPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolDescription.
    def visitToolDescription(self, ctx:ai_environmentParser.ToolDescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolTypeProp.
    def visitToolTypeProp(self, ctx:ai_environmentParser.ToolTypePropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolOtherProperty.
    def visitToolOtherProperty(self, ctx:ai_environmentParser.ToolOtherPropertyContext):
        return self.visitChildren(ctx)



del ai_environmentParser