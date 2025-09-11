# Generated from app/agent_grammer/parser/ai_environment.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,159,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,49,8,0,10,0,12,0,52,9,0,1,0,5,0,55,
        8,0,10,0,12,0,58,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,
        5,3,71,8,3,10,3,12,3,74,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        5,4,85,8,4,10,4,12,4,88,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,11,5,11,117,8,11,10,11,12,11,120,9,11,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,5,12,130,8,12,10,12,12,12,133,9,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,
        16,1,16,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,1,18,0,0,19,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,0,145,0,38,1,0,
        0,0,2,61,1,0,0,0,4,65,1,0,0,0,6,72,1,0,0,0,8,75,1,0,0,0,10,91,1,
        0,0,0,12,95,1,0,0,0,14,99,1,0,0,0,16,103,1,0,0,0,18,107,1,0,0,0,
        20,111,1,0,0,0,22,118,1,0,0,0,24,121,1,0,0,0,26,136,1,0,0,0,28,140,
        1,0,0,0,30,144,1,0,0,0,32,148,1,0,0,0,34,152,1,0,0,0,36,154,1,0,
        0,0,38,39,5,1,0,0,39,40,5,30,0,0,40,41,5,2,0,0,41,42,5,3,0,0,42,
        43,3,2,1,0,43,44,3,4,2,0,44,45,5,4,0,0,45,46,5,5,0,0,46,50,5,3,0,
        0,47,49,3,24,12,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,
        1,0,0,0,51,56,1,0,0,0,52,50,1,0,0,0,53,55,3,8,4,0,54,53,1,0,0,0,
        55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,56,1,
        0,0,0,59,60,5,4,0,0,60,1,1,0,0,0,61,62,5,6,0,0,62,63,5,7,0,0,63,
        64,5,19,0,0,64,3,1,0,0,0,65,66,5,8,0,0,66,67,5,7,0,0,67,68,5,24,
        0,0,68,5,1,0,0,0,69,71,3,8,4,0,70,69,1,0,0,0,71,74,1,0,0,0,72,70,
        1,0,0,0,72,73,1,0,0,0,73,7,1,0,0,0,74,72,1,0,0,0,75,76,5,9,0,0,76,
        77,5,30,0,0,77,78,5,3,0,0,78,79,3,10,5,0,79,80,3,12,6,0,80,81,3,
        14,7,0,81,82,3,16,8,0,82,86,3,18,9,0,83,85,3,20,10,0,84,83,1,0,0,
        0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,
        1,0,0,0,89,90,5,4,0,0,90,9,1,0,0,0,91,92,5,10,0,0,92,93,5,7,0,0,
        93,94,5,27,0,0,94,11,1,0,0,0,95,96,5,11,0,0,96,97,5,7,0,0,97,98,
        5,26,0,0,98,13,1,0,0,0,99,100,5,12,0,0,100,101,5,7,0,0,101,102,5,
        30,0,0,102,15,1,0,0,0,103,104,5,13,0,0,104,105,5,7,0,0,105,106,5,
        30,0,0,106,17,1,0,0,0,107,108,5,14,0,0,108,109,5,7,0,0,109,110,5,
        30,0,0,110,19,1,0,0,0,111,112,5,25,0,0,112,113,5,7,0,0,113,114,5,
        30,0,0,114,21,1,0,0,0,115,117,3,24,12,0,116,115,1,0,0,0,117,120,
        1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,23,1,0,0,0,120,118,1,
        0,0,0,121,122,5,15,0,0,122,123,5,30,0,0,123,124,5,3,0,0,124,125,
        3,28,14,0,125,126,3,30,15,0,126,127,3,26,13,0,127,131,3,32,16,0,
        128,130,3,34,17,0,129,128,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,
        0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,135,5,4,0,
        0,135,25,1,0,0,0,136,137,5,16,0,0,137,138,5,7,0,0,138,139,5,30,0,
        0,139,27,1,0,0,0,140,141,5,10,0,0,141,142,5,7,0,0,142,143,5,28,0,
        0,143,29,1,0,0,0,144,145,5,17,0,0,145,146,5,7,0,0,146,147,5,29,0,
        0,147,31,1,0,0,0,148,149,5,18,0,0,149,150,5,7,0,0,150,151,5,27,0,
        0,151,33,1,0,0,0,152,153,3,36,18,0,153,35,1,0,0,0,154,155,5,25,0,
        0,155,156,5,7,0,0,156,157,5,30,0,0,157,37,1,0,0,0,6,50,56,72,86,
        118,131
    ]

class ai_environmentParser ( Parser ):

    grammarFileName = "ai_environment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ai_environment'", "'@nonfunctional'", 
                     "'{'", "'}'", "'@functional'", "'deployment'", "'='", 
                     "'techstack'", "'llm'", "'uid'", "'provider'", "'model'", 
                     "'endpoint'", "'version'", "'agent'", "'systemprompt'", 
                     "'namespace'", "'llmref'", "<INVALID>", "'aiurn:deployment:microservice'", 
                     "'aiurn:deployment:swarm'", "'aiurn:deployment:mcpservice'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "DEPLOYMENT", 
                      "DEPLOYMENT_MICROSERVICE", "DEPLOYMENT_SWARM", "DEPLOYMENT_MCPSERVICE", 
                      "TECHSTACK_CATEGORY", "TECHSTACK_AIURN", "VAR", "LLMPROVIDER", 
                      "LLMID", "AGENTID", "NAMESPACE", "STRING", "WS" ]

    RULE_ai_envDef = 0
    RULE_deploymentPattern = 1
    RULE_techstack = 2
    RULE_llms = 3
    RULE_llmDef = 4
    RULE_llmIdProp = 5
    RULE_providerProp = 6
    RULE_modelProp = 7
    RULE_endpointProp = 8
    RULE_versionProp = 9
    RULE_otherLLMProperty = 10
    RULE_prog = 11
    RULE_agentDef = 12
    RULE_systemPromptProperty = 13
    RULE_agentIdentity = 14
    RULE_agentNamespace = 15
    RULE_llmRefProperty = 16
    RULE_otherAgentProperty = 17
    RULE_agentProperty = 18

    ruleNames =  [ "ai_envDef", "deploymentPattern", "techstack", "llms", 
                   "llmDef", "llmIdProp", "providerProp", "modelProp", "endpointProp", 
                   "versionProp", "otherLLMProperty", "prog", "agentDef", 
                   "systemPromptProperty", "agentIdentity", "agentNamespace", 
                   "llmRefProperty", "otherAgentProperty", "agentProperty" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    DEPLOYMENT=19
    DEPLOYMENT_MICROSERVICE=20
    DEPLOYMENT_SWARM=21
    DEPLOYMENT_MCPSERVICE=22
    TECHSTACK_CATEGORY=23
    TECHSTACK_AIURN=24
    VAR=25
    LLMPROVIDER=26
    LLMID=27
    AGENTID=28
    NAMESPACE=29
    STRING=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Ai_envDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

        def deploymentPattern(self):
            return self.getTypedRuleContext(ai_environmentParser.DeploymentPatternContext,0)


        def techstack(self):
            return self.getTypedRuleContext(ai_environmentParser.TechstackContext,0)


        def agentDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.AgentDefContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.AgentDefContext,i)


        def llmDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.LlmDefContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.LlmDefContext,i)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_ai_envDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAi_envDef" ):
                listener.enterAi_envDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAi_envDef" ):
                listener.exitAi_envDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAi_envDef" ):
                return visitor.visitAi_envDef(self)
            else:
                return visitor.visitChildren(self)




    def ai_envDef(self):

        localctx = ai_environmentParser.Ai_envDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ai_envDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ai_environmentParser.T__0)
            self.state = 39
            self.match(ai_environmentParser.STRING)
            self.state = 40
            self.match(ai_environmentParser.T__1)
            self.state = 41
            self.match(ai_environmentParser.T__2)
            self.state = 42
            self.deploymentPattern()
            self.state = 43
            self.techstack()
            self.state = 44
            self.match(ai_environmentParser.T__3)
            self.state = 45
            self.match(ai_environmentParser.T__4)
            self.state = 46
            self.match(ai_environmentParser.T__2)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 47
                self.agentDef()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 53
                self.llmDef()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(ai_environmentParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeploymentPatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEPLOYMENT(self):
            return self.getToken(ai_environmentParser.DEPLOYMENT, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_deploymentPattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeploymentPattern" ):
                listener.enterDeploymentPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeploymentPattern" ):
                listener.exitDeploymentPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeploymentPattern" ):
                return visitor.visitDeploymentPattern(self)
            else:
                return visitor.visitChildren(self)




    def deploymentPattern(self):

        localctx = ai_environmentParser.DeploymentPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_deploymentPattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(ai_environmentParser.T__5)
            self.state = 62
            self.match(ai_environmentParser.T__6)
            self.state = 63
            self.match(ai_environmentParser.DEPLOYMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TechstackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TECHSTACK_AIURN(self):
            return self.getToken(ai_environmentParser.TECHSTACK_AIURN, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_techstack

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTechstack" ):
                listener.enterTechstack(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTechstack" ):
                listener.exitTechstack(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTechstack" ):
                return visitor.visitTechstack(self)
            else:
                return visitor.visitChildren(self)




    def techstack(self):

        localctx = ai_environmentParser.TechstackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_techstack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(ai_environmentParser.T__7)
            self.state = 66
            self.match(ai_environmentParser.T__6)
            self.state = 67
            self.match(ai_environmentParser.TECHSTACK_AIURN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlmsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def llmDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.LlmDefContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.LlmDefContext,i)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_llms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlms" ):
                listener.enterLlms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlms" ):
                listener.exitLlms(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlms" ):
                return visitor.visitLlms(self)
            else:
                return visitor.visitChildren(self)




    def llms(self):

        localctx = ai_environmentParser.LlmsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_llms)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 69
                self.llmDef()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlmDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

        def llmIdProp(self):
            return self.getTypedRuleContext(ai_environmentParser.LlmIdPropContext,0)


        def providerProp(self):
            return self.getTypedRuleContext(ai_environmentParser.ProviderPropContext,0)


        def modelProp(self):
            return self.getTypedRuleContext(ai_environmentParser.ModelPropContext,0)


        def endpointProp(self):
            return self.getTypedRuleContext(ai_environmentParser.EndpointPropContext,0)


        def versionProp(self):
            return self.getTypedRuleContext(ai_environmentParser.VersionPropContext,0)


        def otherLLMProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.OtherLLMPropertyContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.OtherLLMPropertyContext,i)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_llmDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlmDef" ):
                listener.enterLlmDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlmDef" ):
                listener.exitLlmDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlmDef" ):
                return visitor.visitLlmDef(self)
            else:
                return visitor.visitChildren(self)




    def llmDef(self):

        localctx = ai_environmentParser.LlmDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_llmDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(ai_environmentParser.T__8)
            self.state = 76
            self.match(ai_environmentParser.STRING)
            self.state = 77
            self.match(ai_environmentParser.T__2)
            self.state = 78
            self.llmIdProp()
            self.state = 79
            self.providerProp()
            self.state = 80
            self.modelProp()
            self.state = 81
            self.endpointProp()
            self.state = 82
            self.versionProp()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 83
                self.otherLLMProperty()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(ai_environmentParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlmIdPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLMID(self):
            return self.getToken(ai_environmentParser.LLMID, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_llmIdProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlmIdProp" ):
                listener.enterLlmIdProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlmIdProp" ):
                listener.exitLlmIdProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlmIdProp" ):
                return visitor.visitLlmIdProp(self)
            else:
                return visitor.visitChildren(self)




    def llmIdProp(self):

        localctx = ai_environmentParser.LlmIdPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_llmIdProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(ai_environmentParser.T__9)
            self.state = 92
            self.match(ai_environmentParser.T__6)
            self.state = 93
            self.match(ai_environmentParser.LLMID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProviderPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLMPROVIDER(self):
            return self.getToken(ai_environmentParser.LLMPROVIDER, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_providerProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProviderProp" ):
                listener.enterProviderProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProviderProp" ):
                listener.exitProviderProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProviderProp" ):
                return visitor.visitProviderProp(self)
            else:
                return visitor.visitChildren(self)




    def providerProp(self):

        localctx = ai_environmentParser.ProviderPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_providerProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(ai_environmentParser.T__10)
            self.state = 96
            self.match(ai_environmentParser.T__6)
            self.state = 97
            self.match(ai_environmentParser.LLMPROVIDER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_modelProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelProp" ):
                listener.enterModelProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelProp" ):
                listener.exitModelProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelProp" ):
                return visitor.visitModelProp(self)
            else:
                return visitor.visitChildren(self)




    def modelProp(self):

        localctx = ai_environmentParser.ModelPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_modelProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(ai_environmentParser.T__11)
            self.state = 100
            self.match(ai_environmentParser.T__6)
            self.state = 101
            self.match(ai_environmentParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndpointPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_endpointProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndpointProp" ):
                listener.enterEndpointProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndpointProp" ):
                listener.exitEndpointProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndpointProp" ):
                return visitor.visitEndpointProp(self)
            else:
                return visitor.visitChildren(self)




    def endpointProp(self):

        localctx = ai_environmentParser.EndpointPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_endpointProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(ai_environmentParser.T__12)
            self.state = 104
            self.match(ai_environmentParser.T__6)
            self.state = 105
            self.match(ai_environmentParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VersionPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_versionProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVersionProp" ):
                listener.enterVersionProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVersionProp" ):
                listener.exitVersionProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVersionProp" ):
                return visitor.visitVersionProp(self)
            else:
                return visitor.visitChildren(self)




    def versionProp(self):

        localctx = ai_environmentParser.VersionPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_versionProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(ai_environmentParser.T__13)
            self.state = 108
            self.match(ai_environmentParser.T__6)
            self.state = 109
            self.match(ai_environmentParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtherLLMPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ai_environmentParser.VAR, 0)

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_otherLLMProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOtherLLMProperty" ):
                listener.enterOtherLLMProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOtherLLMProperty" ):
                listener.exitOtherLLMProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOtherLLMProperty" ):
                return visitor.visitOtherLLMProperty(self)
            else:
                return visitor.visitChildren(self)




    def otherLLMProperty(self):

        localctx = ai_environmentParser.OtherLLMPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_otherLLMProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(ai_environmentParser.VAR)
            self.state = 112
            self.match(ai_environmentParser.T__6)
            self.state = 113
            self.match(ai_environmentParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def agentDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.AgentDefContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.AgentDefContext,i)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ai_environmentParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 115
                self.agentDef()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

        def agentIdentity(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentIdentityContext,0)


        def agentNamespace(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentNamespaceContext,0)


        def systemPromptProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.SystemPromptPropertyContext,0)


        def llmRefProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.LlmRefPropertyContext,0)


        def otherAgentProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.OtherAgentPropertyContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.OtherAgentPropertyContext,i)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentDef" ):
                listener.enterAgentDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentDef" ):
                listener.exitAgentDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentDef" ):
                return visitor.visitAgentDef(self)
            else:
                return visitor.visitChildren(self)




    def agentDef(self):

        localctx = ai_environmentParser.AgentDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_agentDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(ai_environmentParser.T__14)
            self.state = 122
            self.match(ai_environmentParser.STRING)
            self.state = 123
            self.match(ai_environmentParser.T__2)
            self.state = 124
            self.agentIdentity()
            self.state = 125
            self.agentNamespace()
            self.state = 126
            self.systemPromptProperty()
            self.state = 127
            self.llmRefProperty()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 128
                self.otherAgentProperty()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self.match(ai_environmentParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SystemPromptPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_systemPromptProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSystemPromptProperty" ):
                listener.enterSystemPromptProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSystemPromptProperty" ):
                listener.exitSystemPromptProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSystemPromptProperty" ):
                return visitor.visitSystemPromptProperty(self)
            else:
                return visitor.visitChildren(self)




    def systemPromptProperty(self):

        localctx = ai_environmentParser.SystemPromptPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_systemPromptProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(ai_environmentParser.T__15)
            self.state = 137
            self.match(ai_environmentParser.T__6)
            self.state = 138
            self.match(ai_environmentParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentIdentityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGENTID(self):
            return self.getToken(ai_environmentParser.AGENTID, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentIdentity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentIdentity" ):
                listener.enterAgentIdentity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentIdentity" ):
                listener.exitAgentIdentity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentIdentity" ):
                return visitor.visitAgentIdentity(self)
            else:
                return visitor.visitChildren(self)




    def agentIdentity(self):

        localctx = ai_environmentParser.AgentIdentityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_agentIdentity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(ai_environmentParser.T__9)
            self.state = 141
            self.match(ai_environmentParser.T__6)
            self.state = 142
            self.match(ai_environmentParser.AGENTID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentNamespaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAMESPACE(self):
            return self.getToken(ai_environmentParser.NAMESPACE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentNamespace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentNamespace" ):
                listener.enterAgentNamespace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentNamespace" ):
                listener.exitAgentNamespace(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentNamespace" ):
                return visitor.visitAgentNamespace(self)
            else:
                return visitor.visitChildren(self)




    def agentNamespace(self):

        localctx = ai_environmentParser.AgentNamespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_agentNamespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(ai_environmentParser.T__16)
            self.state = 145
            self.match(ai_environmentParser.T__6)
            self.state = 146
            self.match(ai_environmentParser.NAMESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlmRefPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLMID(self):
            return self.getToken(ai_environmentParser.LLMID, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_llmRefProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlmRefProperty" ):
                listener.enterLlmRefProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlmRefProperty" ):
                listener.exitLlmRefProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlmRefProperty" ):
                return visitor.visitLlmRefProperty(self)
            else:
                return visitor.visitChildren(self)




    def llmRefProperty(self):

        localctx = ai_environmentParser.LlmRefPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_llmRefProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ai_environmentParser.T__17)
            self.state = 149
            self.match(ai_environmentParser.T__6)
            self.state = 150
            self.match(ai_environmentParser.LLMID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtherAgentPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def agentProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentPropertyContext,0)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_otherAgentProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOtherAgentProperty" ):
                listener.enterOtherAgentProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOtherAgentProperty" ):
                listener.exitOtherAgentProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOtherAgentProperty" ):
                return visitor.visitOtherAgentProperty(self)
            else:
                return visitor.visitChildren(self)




    def otherAgentProperty(self):

        localctx = ai_environmentParser.OtherAgentPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_otherAgentProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.agentProperty()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ai_environmentParser.VAR, 0)

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentProperty" ):
                listener.enterAgentProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentProperty" ):
                listener.exitAgentProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentProperty" ):
                return visitor.visitAgentProperty(self)
            else:
                return visitor.visitChildren(self)




    def agentProperty(self):

        localctx = ai_environmentParser.AgentPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_agentProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(ai_environmentParser.VAR)
            self.state = 155
            self.match(ai_environmentParser.T__6)
            self.state = 156
            self.match(ai_environmentParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





