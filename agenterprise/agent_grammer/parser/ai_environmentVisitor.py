# Generated from agenterprise/agent_grammer/parser/ai_environment.g4 by ANTLR 4.13.2
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


    # Visit a parse tree produced by ai_environmentParser#envId.
    def visitEnvId(self, ctx:ai_environmentParser.EnvIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#architectureServiceStack.
    def visitArchitectureServiceStack(self, ctx:ai_environmentParser.ArchitectureServiceStackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#architectureAiStack.
    def visitArchitectureAiStack(self, ctx:ai_environmentParser.ArchitectureAiStackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#architectureDataStack.
    def visitArchitectureDataStack(self, ctx:ai_environmentParser.ArchitectureDataStackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#architectureAgenticMiddlewareStack.
    def visitArchitectureAgenticMiddlewareStack(self, ctx:ai_environmentParser.ArchitectureAgenticMiddlewareStackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#entityDef.
    def visitEntityDef(self, ctx:ai_environmentParser.EntityDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#entityProp.
    def visitEntityProp(self, ctx:ai_environmentParser.EntityPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#entityIdProp.
    def visitEntityIdProp(self, ctx:ai_environmentParser.EntityIdPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#entityElementProp.
    def visitEntityElementProp(self, ctx:ai_environmentParser.EntityElementPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#entityElementType.
    def visitEntityElementType(self, ctx:ai_environmentParser.EntityElementTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#entityElementDescription.
    def visitEntityElementDescription(self, ctx:ai_environmentParser.EntityElementDescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentDef.
    def visitAgentDef(self, ctx:ai_environmentParser.AgentDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentProperty.
    def visitAgentProperty(self, ctx:ai_environmentParser.AgentPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentSystemPromptProperty.
    def visitAgentSystemPromptProperty(self, ctx:ai_environmentParser.AgentSystemPromptPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentIdentity.
    def visitAgentIdentity(self, ctx:ai_environmentParser.AgentIdentityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentNamespace.
    def visitAgentNamespace(self, ctx:ai_environmentParser.AgentNamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentLLMRefProperty.
    def visitAgentLLMRefProperty(self, ctx:ai_environmentParser.AgentLLMRefPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentToolRefProperty.
    def visitAgentToolRefProperty(self, ctx:ai_environmentParser.AgentToolRefPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentInputProperty.
    def visitAgentInputProperty(self, ctx:ai_environmentParser.AgentInputPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentOutputProperty.
    def visitAgentOutputProperty(self, ctx:ai_environmentParser.AgentOutputPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentDescriptionProp.
    def visitAgentDescriptionProp(self, ctx:ai_environmentParser.AgentDescriptionPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentExampleProp.
    def visitAgentExampleProp(self, ctx:ai_environmentParser.AgentExamplePropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentTagsProp.
    def visitAgentTagsProp(self, ctx:ai_environmentParser.AgentTagsPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#agentCustomProperty.
    def visitAgentCustomProperty(self, ctx:ai_environmentParser.AgentCustomPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#llmDef.
    def visitLlmDef(self, ctx:ai_environmentParser.LlmDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#llmProp.
    def visitLlmProp(self, ctx:ai_environmentParser.LlmPropContext):
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


    # Visit a parse tree produced by ai_environmentParser#toolDef.
    def visitToolDef(self, ctx:ai_environmentParser.ToolDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolProp.
    def visitToolProp(self, ctx:ai_environmentParser.ToolPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolIdProp.
    def visitToolIdProp(self, ctx:ai_environmentParser.ToolIdPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolEndpointProp.
    def visitToolEndpointProp(self, ctx:ai_environmentParser.ToolEndpointPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolInputProperty.
    def visitToolInputProperty(self, ctx:ai_environmentParser.ToolInputPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolOutputProperty.
    def visitToolOutputProperty(self, ctx:ai_environmentParser.ToolOutputPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolDescriptionProp.
    def visitToolDescriptionProp(self, ctx:ai_environmentParser.ToolDescriptionPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolTypeProp.
    def visitToolTypeProp(self, ctx:ai_environmentParser.ToolTypePropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ai_environmentParser#toolOtherProperty.
    def visitToolOtherProperty(self, ctx:ai_environmentParser.ToolOtherPropertyContext):
        return self.visitChildren(ctx)



del ai_environmentParser