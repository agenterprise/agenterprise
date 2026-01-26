# Generated from agenterprise/agent_grammer/parser/ai_environment.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by ai_environmentParser#envId.
    def enterEnvId(self, ctx:ai_environmentParser.EnvIdContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#envId.
    def exitEnvId(self, ctx:ai_environmentParser.EnvIdContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#architectureServiceStack.
    def enterArchitectureServiceStack(self, ctx:ai_environmentParser.ArchitectureServiceStackContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#architectureServiceStack.
    def exitArchitectureServiceStack(self, ctx:ai_environmentParser.ArchitectureServiceStackContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#architectureAiStack.
    def enterArchitectureAiStack(self, ctx:ai_environmentParser.ArchitectureAiStackContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#architectureAiStack.
    def exitArchitectureAiStack(self, ctx:ai_environmentParser.ArchitectureAiStackContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#architectureDataStack.
    def enterArchitectureDataStack(self, ctx:ai_environmentParser.ArchitectureDataStackContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#architectureDataStack.
    def exitArchitectureDataStack(self, ctx:ai_environmentParser.ArchitectureDataStackContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#architectureAgenticMiddlewareStack.
    def enterArchitectureAgenticMiddlewareStack(self, ctx:ai_environmentParser.ArchitectureAgenticMiddlewareStackContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#architectureAgenticMiddlewareStack.
    def exitArchitectureAgenticMiddlewareStack(self, ctx:ai_environmentParser.ArchitectureAgenticMiddlewareStackContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#entityDef.
    def enterEntityDef(self, ctx:ai_environmentParser.EntityDefContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#entityDef.
    def exitEntityDef(self, ctx:ai_environmentParser.EntityDefContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#entityProp.
    def enterEntityProp(self, ctx:ai_environmentParser.EntityPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#entityProp.
    def exitEntityProp(self, ctx:ai_environmentParser.EntityPropContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#entityIdProp.
    def enterEntityIdProp(self, ctx:ai_environmentParser.EntityIdPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#entityIdProp.
    def exitEntityIdProp(self, ctx:ai_environmentParser.EntityIdPropContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#entityElementProp.
    def enterEntityElementProp(self, ctx:ai_environmentParser.EntityElementPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#entityElementProp.
    def exitEntityElementProp(self, ctx:ai_environmentParser.EntityElementPropContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#entityElementType.
    def enterEntityElementType(self, ctx:ai_environmentParser.EntityElementTypeContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#entityElementType.
    def exitEntityElementType(self, ctx:ai_environmentParser.EntityElementTypeContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#entityElementDescription.
    def enterEntityElementDescription(self, ctx:ai_environmentParser.EntityElementDescriptionContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#entityElementDescription.
    def exitEntityElementDescription(self, ctx:ai_environmentParser.EntityElementDescriptionContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#agentDef.
    def enterAgentDef(self, ctx:ai_environmentParser.AgentDefContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentDef.
    def exitAgentDef(self, ctx:ai_environmentParser.AgentDefContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#agentProperty.
    def enterAgentProperty(self, ctx:ai_environmentParser.AgentPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentProperty.
    def exitAgentProperty(self, ctx:ai_environmentParser.AgentPropertyContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#agentSystemPromptProperty.
    def enterAgentSystemPromptProperty(self, ctx:ai_environmentParser.AgentSystemPromptPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentSystemPromptProperty.
    def exitAgentSystemPromptProperty(self, ctx:ai_environmentParser.AgentSystemPromptPropertyContext):
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


    # Enter a parse tree produced by ai_environmentParser#agentLLMRefProperty.
    def enterAgentLLMRefProperty(self, ctx:ai_environmentParser.AgentLLMRefPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentLLMRefProperty.
    def exitAgentLLMRefProperty(self, ctx:ai_environmentParser.AgentLLMRefPropertyContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#agentToolRefProperty.
    def enterAgentToolRefProperty(self, ctx:ai_environmentParser.AgentToolRefPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentToolRefProperty.
    def exitAgentToolRefProperty(self, ctx:ai_environmentParser.AgentToolRefPropertyContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#agentInputProperty.
    def enterAgentInputProperty(self, ctx:ai_environmentParser.AgentInputPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentInputProperty.
    def exitAgentInputProperty(self, ctx:ai_environmentParser.AgentInputPropertyContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#agentOutputProperty.
    def enterAgentOutputProperty(self, ctx:ai_environmentParser.AgentOutputPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentOutputProperty.
    def exitAgentOutputProperty(self, ctx:ai_environmentParser.AgentOutputPropertyContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#agentDescriptionProp.
    def enterAgentDescriptionProp(self, ctx:ai_environmentParser.AgentDescriptionPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentDescriptionProp.
    def exitAgentDescriptionProp(self, ctx:ai_environmentParser.AgentDescriptionPropContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#agentExampleProp.
    def enterAgentExampleProp(self, ctx:ai_environmentParser.AgentExamplePropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentExampleProp.
    def exitAgentExampleProp(self, ctx:ai_environmentParser.AgentExamplePropContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#agentTagsProp.
    def enterAgentTagsProp(self, ctx:ai_environmentParser.AgentTagsPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentTagsProp.
    def exitAgentTagsProp(self, ctx:ai_environmentParser.AgentTagsPropContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#agentCustomProperty.
    def enterAgentCustomProperty(self, ctx:ai_environmentParser.AgentCustomPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#agentCustomProperty.
    def exitAgentCustomProperty(self, ctx:ai_environmentParser.AgentCustomPropertyContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#llmDef.
    def enterLlmDef(self, ctx:ai_environmentParser.LlmDefContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#llmDef.
    def exitLlmDef(self, ctx:ai_environmentParser.LlmDefContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#llmProp.
    def enterLlmProp(self, ctx:ai_environmentParser.LlmPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#llmProp.
    def exitLlmProp(self, ctx:ai_environmentParser.LlmPropContext):
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


    # Enter a parse tree produced by ai_environmentParser#toolDef.
    def enterToolDef(self, ctx:ai_environmentParser.ToolDefContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#toolDef.
    def exitToolDef(self, ctx:ai_environmentParser.ToolDefContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#toolProp.
    def enterToolProp(self, ctx:ai_environmentParser.ToolPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#toolProp.
    def exitToolProp(self, ctx:ai_environmentParser.ToolPropContext):
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


    # Enter a parse tree produced by ai_environmentParser#toolInputProperty.
    def enterToolInputProperty(self, ctx:ai_environmentParser.ToolInputPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#toolInputProperty.
    def exitToolInputProperty(self, ctx:ai_environmentParser.ToolInputPropertyContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#toolOutputProperty.
    def enterToolOutputProperty(self, ctx:ai_environmentParser.ToolOutputPropertyContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#toolOutputProperty.
    def exitToolOutputProperty(self, ctx:ai_environmentParser.ToolOutputPropertyContext):
        pass


    # Enter a parse tree produced by ai_environmentParser#toolDescriptionProp.
    def enterToolDescriptionProp(self, ctx:ai_environmentParser.ToolDescriptionPropContext):
        pass

    # Exit a parse tree produced by ai_environmentParser#toolDescriptionProp.
    def exitToolDescriptionProp(self, ctx:ai_environmentParser.ToolDescriptionPropContext):
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