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


    # Visit a parse tree produced by ai_environmentParser#deploymentPattern.
    def visitDeploymentPattern(self, ctx:ai_environmentParser.DeploymentPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#techstack.
    def visitTechstack(self, ctx:ai_environmentParser.TechstackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#llms.
    def visitLlms(self, ctx:ai_environmentParser.LlmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#llmDef.
    def visitLlmDef(self, ctx:ai_environmentParser.LlmDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#llmIdProp.
    def visitLlmIdProp(self, ctx:ai_environmentParser.LlmIdPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#providerProp.
    def visitProviderProp(self, ctx:ai_environmentParser.ProviderPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#modelProp.
    def visitModelProp(self, ctx:ai_environmentParser.ModelPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#endpointProp.
    def visitEndpointProp(self, ctx:ai_environmentParser.EndpointPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#versionProp.
    def visitVersionProp(self, ctx:ai_environmentParser.VersionPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#otherLLMProperty.
    def visitOtherLLMProperty(self, ctx:ai_environmentParser.OtherLLMPropertyContext):
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


    # Visit a parse tree produced by ai_environmentParser#otherAgentProperty.
    def visitOtherAgentProperty(self, ctx:ai_environmentParser.OtherAgentPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentProperty.
    def visitAgentProperty(self, ctx:ai_environmentParser.AgentPropertyContext):
        return self.visitChildren(ctx)



del ai_environmentParser