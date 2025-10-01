# Generated from agenterprise/agent_grammer/parser/ai_environment.g4 by ANTLR 4.13.2
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
        4,1,35,216,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,5,0,61,8,0,10,0,12,0,64,9,0,1,0,1,0,1,0,1,0,5,
        0,70,8,0,10,0,12,0,73,9,0,1,0,5,0,76,8,0,10,0,12,0,79,9,0,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,5,4,104,8,4,10,4,12,4,107,9,4,1,4,5,4,110,
        8,4,10,4,12,4,113,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,150,8,11,10,11,
        12,11,153,9,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,
        1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,189,
        8,18,10,18,12,18,192,9,18,1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,
        1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,
        1,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,0,0,198,0,48,1,0,0,0,2,83,1,0,0,0,4,87,1,0,0,0,
        6,91,1,0,0,0,8,95,1,0,0,0,10,116,1,0,0,0,12,120,1,0,0,0,14,124,1,
        0,0,0,16,128,1,0,0,0,18,132,1,0,0,0,20,136,1,0,0,0,22,140,1,0,0,
        0,24,156,1,0,0,0,26,160,1,0,0,0,28,164,1,0,0,0,30,168,1,0,0,0,32,
        172,1,0,0,0,34,176,1,0,0,0,36,180,1,0,0,0,38,195,1,0,0,0,40,199,
        1,0,0,0,42,203,1,0,0,0,44,207,1,0,0,0,46,211,1,0,0,0,48,49,5,1,0,
        0,49,50,5,34,0,0,50,51,5,2,0,0,51,52,5,3,0,0,52,53,5,2,0,0,53,54,
        3,2,1,0,54,55,3,4,2,0,55,56,3,6,3,0,56,57,5,4,0,0,57,58,5,5,0,0,
        58,62,5,2,0,0,59,61,3,22,11,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,
        1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,65,66,5,4,0,0,
        66,67,5,6,0,0,67,71,5,2,0,0,68,70,3,8,4,0,69,68,1,0,0,0,70,73,1,
        0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,77,1,0,0,0,73,71,1,0,0,0,74,
        76,3,36,18,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,
        0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,5,4,0,0,81,82,5,4,0,0,82,1,
        1,0,0,0,83,84,5,7,0,0,84,85,5,8,0,0,85,86,5,34,0,0,86,3,1,0,0,0,
        87,88,5,9,0,0,88,89,5,8,0,0,89,90,5,26,0,0,90,5,1,0,0,0,91,92,5,
        10,0,0,92,93,5,8,0,0,93,94,5,26,0,0,94,7,1,0,0,0,95,96,5,11,0,0,
        96,97,5,34,0,0,97,98,5,2,0,0,98,99,3,12,6,0,99,100,3,14,7,0,100,
        101,3,10,5,0,101,105,3,16,8,0,102,104,3,18,9,0,103,102,1,0,0,0,104,
        107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,111,1,0,0,0,107,
        105,1,0,0,0,108,110,3,20,10,0,109,108,1,0,0,0,110,113,1,0,0,0,111,
        109,1,0,0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,111,1,0,0,0,114,
        115,5,4,0,0,115,9,1,0,0,0,116,117,5,12,0,0,117,118,5,8,0,0,118,119,
        5,34,0,0,119,11,1,0,0,0,120,121,5,13,0,0,121,122,5,8,0,0,122,123,
        5,32,0,0,123,13,1,0,0,0,124,125,5,14,0,0,125,126,5,8,0,0,126,127,
        5,33,0,0,127,15,1,0,0,0,128,129,5,15,0,0,129,130,5,8,0,0,130,131,
        5,29,0,0,131,17,1,0,0,0,132,133,5,16,0,0,133,134,5,8,0,0,134,135,
        5,30,0,0,135,19,1,0,0,0,136,137,5,27,0,0,137,138,5,8,0,0,138,139,
        5,34,0,0,139,21,1,0,0,0,140,141,5,17,0,0,141,142,5,34,0,0,142,143,
        5,2,0,0,143,144,3,24,12,0,144,145,3,26,13,0,145,146,3,28,14,0,146,
        147,3,30,15,0,147,151,3,32,16,0,148,150,3,34,17,0,149,148,1,0,0,
        0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,154,1,0,0,
        0,153,151,1,0,0,0,154,155,5,4,0,0,155,23,1,0,0,0,156,157,5,13,0,
        0,157,158,5,8,0,0,158,159,5,29,0,0,159,25,1,0,0,0,160,161,5,18,0,
        0,161,162,5,8,0,0,162,163,5,28,0,0,163,27,1,0,0,0,164,165,5,19,0,
        0,165,166,5,8,0,0,166,167,5,34,0,0,167,29,1,0,0,0,168,169,5,20,0,
        0,169,170,5,8,0,0,170,171,5,34,0,0,171,31,1,0,0,0,172,173,5,21,0,
        0,173,174,5,8,0,0,174,175,5,34,0,0,175,33,1,0,0,0,176,177,5,27,0,
        0,177,178,5,8,0,0,178,179,5,34,0,0,179,35,1,0,0,0,180,181,5,22,0,
        0,181,182,5,34,0,0,182,183,5,2,0,0,183,184,3,38,19,0,184,185,3,40,
        20,0,185,186,3,44,22,0,186,190,3,42,21,0,187,189,3,46,23,0,188,187,
        1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,193,
        1,0,0,0,192,190,1,0,0,0,193,194,5,4,0,0,194,37,1,0,0,0,195,196,5,
        13,0,0,196,197,5,8,0,0,197,198,5,30,0,0,198,39,1,0,0,0,199,200,5,
        20,0,0,200,201,5,8,0,0,201,202,5,34,0,0,202,41,1,0,0,0,203,204,5,
        23,0,0,204,205,5,8,0,0,205,206,5,34,0,0,206,43,1,0,0,0,207,208,5,
        24,0,0,208,209,5,8,0,0,209,210,5,31,0,0,210,45,1,0,0,0,211,212,5,
        27,0,0,212,213,5,8,0,0,213,214,5,34,0,0,214,47,1,0,0,0,7,62,71,77,
        105,111,151,190
    ]

class ai_environmentParser ( Parser ):

    grammarFileName = "ai_environment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ai_environment'", "'{'", "'architecture'", 
                     "'}'", "'infrastructure'", "'functional'", "'envid'", 
                     "'='", "'service-techlayer'", "'ai-techlayer'", "'agent'", 
                     "'systemprompt'", "'uid'", "'namespace'", "'llmref'", 
                     "'toolref'", "'llm'", "'provider'", "'model'", "'endpoint'", 
                     "'version'", "'tool'", "'description'", "'type'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TECHLAYER_RESSOURCE", "TECHLAYER_AIURN", 
                      "VAR", "LLMPROVIDER", "LLMID", "TOOLID", "TOOL_TYPE", 
                      "AGENTID", "AGENTNAMESPACE", "PROPERTYVALUE", "WS" ]

    RULE_ai_envDef = 0
    RULE_envId = 1
    RULE_architectureServiceStack = 2
    RULE_architectureAiStack = 3
    RULE_agentDef = 4
    RULE_agentSystemPromptProperty = 5
    RULE_agentIdentity = 6
    RULE_agentNamespace = 7
    RULE_agentLLMRefProperty = 8
    RULE_agentToolRefProperty = 9
    RULE_agentCustomProperty = 10
    RULE_llmDef = 11
    RULE_llmIdProp = 12
    RULE_llmProviderProp = 13
    RULE_llmModelProp = 14
    RULE_llmEndpointProp = 15
    RULE_llmVersionProp = 16
    RULE_llmOtherProperty = 17
    RULE_toolDef = 18
    RULE_toolIdProp = 19
    RULE_toolEndpointProp = 20
    RULE_toolDescriptionProp = 21
    RULE_toolTypeProp = 22
    RULE_toolOtherProperty = 23

    ruleNames =  [ "ai_envDef", "envId", "architectureServiceStack", "architectureAiStack", 
                   "agentDef", "agentSystemPromptProperty", "agentIdentity", 
                   "agentNamespace", "agentLLMRefProperty", "agentToolRefProperty", 
                   "agentCustomProperty", "llmDef", "llmIdProp", "llmProviderProp", 
                   "llmModelProp", "llmEndpointProp", "llmVersionProp", 
                   "llmOtherProperty", "toolDef", "toolIdProp", "toolEndpointProp", 
                   "toolDescriptionProp", "toolTypeProp", "toolOtherProperty" ]

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
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    TECHLAYER_RESSOURCE=25
    TECHLAYER_AIURN=26
    VAR=27
    LLMPROVIDER=28
    LLMID=29
    TOOLID=30
    TOOL_TYPE=31
    AGENTID=32
    AGENTNAMESPACE=33
    PROPERTYVALUE=34
    WS=35

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

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def envId(self):
            return self.getTypedRuleContext(ai_environmentParser.EnvIdContext,0)


        def architectureServiceStack(self):
            return self.getTypedRuleContext(ai_environmentParser.ArchitectureServiceStackContext,0)


        def architectureAiStack(self):
            return self.getTypedRuleContext(ai_environmentParser.ArchitectureAiStackContext,0)


        def llmDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.LlmDefContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.LlmDefContext,i)


        def agentDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.AgentDefContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.AgentDefContext,i)


        def toolDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.ToolDefContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.ToolDefContext,i)


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
            self.state = 48
            self.match(ai_environmentParser.T__0)
            self.state = 49
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 50
            self.match(ai_environmentParser.T__1)
            self.state = 51
            self.match(ai_environmentParser.T__2)
            self.state = 52
            self.match(ai_environmentParser.T__1)
            self.state = 53
            self.envId()
            self.state = 54
            self.architectureServiceStack()
            self.state = 55
            self.architectureAiStack()
            self.state = 56
            self.match(ai_environmentParser.T__3)
            self.state = 57
            self.match(ai_environmentParser.T__4)
            self.state = 58
            self.match(ai_environmentParser.T__1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 59
                self.llmDef()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(ai_environmentParser.T__3)
            self.state = 66
            self.match(ai_environmentParser.T__5)
            self.state = 67
            self.match(ai_environmentParser.T__1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 68
                self.agentDef()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 74
                self.toolDef()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(ai_environmentParser.T__3)
            self.state = 81
            self.match(ai_environmentParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnvIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_envId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvId" ):
                listener.enterEnvId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvId" ):
                listener.exitEnvId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnvId" ):
                return visitor.visitEnvId(self)
            else:
                return visitor.visitChildren(self)




    def envId(self):

        localctx = ai_environmentParser.EnvIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_envId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(ai_environmentParser.T__6)
            self.state = 84
            self.match(ai_environmentParser.T__7)
            self.state = 85
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArchitectureServiceStackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TECHLAYER_AIURN(self):
            return self.getToken(ai_environmentParser.TECHLAYER_AIURN, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_architectureServiceStack

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArchitectureServiceStack" ):
                listener.enterArchitectureServiceStack(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArchitectureServiceStack" ):
                listener.exitArchitectureServiceStack(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArchitectureServiceStack" ):
                return visitor.visitArchitectureServiceStack(self)
            else:
                return visitor.visitChildren(self)




    def architectureServiceStack(self):

        localctx = ai_environmentParser.ArchitectureServiceStackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_architectureServiceStack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(ai_environmentParser.T__8)
            self.state = 88
            self.match(ai_environmentParser.T__7)
            self.state = 89
            self.match(ai_environmentParser.TECHLAYER_AIURN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArchitectureAiStackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TECHLAYER_AIURN(self):
            return self.getToken(ai_environmentParser.TECHLAYER_AIURN, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_architectureAiStack

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArchitectureAiStack" ):
                listener.enterArchitectureAiStack(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArchitectureAiStack" ):
                listener.exitArchitectureAiStack(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArchitectureAiStack" ):
                return visitor.visitArchitectureAiStack(self)
            else:
                return visitor.visitChildren(self)




    def architectureAiStack(self):

        localctx = ai_environmentParser.ArchitectureAiStackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_architectureAiStack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(ai_environmentParser.T__9)
            self.state = 92
            self.match(ai_environmentParser.T__7)
            self.state = 93
            self.match(ai_environmentParser.TECHLAYER_AIURN)
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

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def agentIdentity(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentIdentityContext,0)


        def agentNamespace(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentNamespaceContext,0)


        def agentSystemPromptProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentSystemPromptPropertyContext,0)


        def agentLLMRefProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentLLMRefPropertyContext,0)


        def agentToolRefProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.AgentToolRefPropertyContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.AgentToolRefPropertyContext,i)


        def agentCustomProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.AgentCustomPropertyContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.AgentCustomPropertyContext,i)


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
        self.enterRule(localctx, 8, self.RULE_agentDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(ai_environmentParser.T__10)
            self.state = 96
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 97
            self.match(ai_environmentParser.T__1)
            self.state = 98
            self.agentIdentity()
            self.state = 99
            self.agentNamespace()
            self.state = 100
            self.agentSystemPromptProperty()
            self.state = 101
            self.agentLLMRefProperty()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 102
                self.agentToolRefProperty()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 108
                self.agentCustomProperty()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(ai_environmentParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentSystemPromptPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentSystemPromptProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentSystemPromptProperty" ):
                listener.enterAgentSystemPromptProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentSystemPromptProperty" ):
                listener.exitAgentSystemPromptProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentSystemPromptProperty" ):
                return visitor.visitAgentSystemPromptProperty(self)
            else:
                return visitor.visitChildren(self)




    def agentSystemPromptProperty(self):

        localctx = ai_environmentParser.AgentSystemPromptPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_agentSystemPromptProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(ai_environmentParser.T__11)
            self.state = 117
            self.match(ai_environmentParser.T__7)
            self.state = 118
            self.match(ai_environmentParser.PROPERTYVALUE)
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
        self.enterRule(localctx, 12, self.RULE_agentIdentity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(ai_environmentParser.T__12)
            self.state = 121
            self.match(ai_environmentParser.T__7)
            self.state = 122
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

        def AGENTNAMESPACE(self):
            return self.getToken(ai_environmentParser.AGENTNAMESPACE, 0)

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
        self.enterRule(localctx, 14, self.RULE_agentNamespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(ai_environmentParser.T__13)
            self.state = 125
            self.match(ai_environmentParser.T__7)
            self.state = 126
            self.match(ai_environmentParser.AGENTNAMESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentLLMRefPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLMID(self):
            return self.getToken(ai_environmentParser.LLMID, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentLLMRefProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentLLMRefProperty" ):
                listener.enterAgentLLMRefProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentLLMRefProperty" ):
                listener.exitAgentLLMRefProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentLLMRefProperty" ):
                return visitor.visitAgentLLMRefProperty(self)
            else:
                return visitor.visitChildren(self)




    def agentLLMRefProperty(self):

        localctx = ai_environmentParser.AgentLLMRefPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_agentLLMRefProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(ai_environmentParser.T__14)
            self.state = 129
            self.match(ai_environmentParser.T__7)
            self.state = 130
            self.match(ai_environmentParser.LLMID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentToolRefPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOOLID(self):
            return self.getToken(ai_environmentParser.TOOLID, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentToolRefProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentToolRefProperty" ):
                listener.enterAgentToolRefProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentToolRefProperty" ):
                listener.exitAgentToolRefProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentToolRefProperty" ):
                return visitor.visitAgentToolRefProperty(self)
            else:
                return visitor.visitChildren(self)




    def agentToolRefProperty(self):

        localctx = ai_environmentParser.AgentToolRefPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_agentToolRefProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(ai_environmentParser.T__15)
            self.state = 133
            self.match(ai_environmentParser.T__7)
            self.state = 134
            self.match(ai_environmentParser.TOOLID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentCustomPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ai_environmentParser.VAR, 0)

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentCustomProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentCustomProperty" ):
                listener.enterAgentCustomProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentCustomProperty" ):
                listener.exitAgentCustomProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentCustomProperty" ):
                return visitor.visitAgentCustomProperty(self)
            else:
                return visitor.visitChildren(self)




    def agentCustomProperty(self):

        localctx = ai_environmentParser.AgentCustomPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_agentCustomProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(ai_environmentParser.VAR)
            self.state = 137
            self.match(ai_environmentParser.T__7)
            self.state = 138
            self.match(ai_environmentParser.PROPERTYVALUE)
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

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def llmIdProp(self):
            return self.getTypedRuleContext(ai_environmentParser.LlmIdPropContext,0)


        def llmProviderProp(self):
            return self.getTypedRuleContext(ai_environmentParser.LlmProviderPropContext,0)


        def llmModelProp(self):
            return self.getTypedRuleContext(ai_environmentParser.LlmModelPropContext,0)


        def llmEndpointProp(self):
            return self.getTypedRuleContext(ai_environmentParser.LlmEndpointPropContext,0)


        def llmVersionProp(self):
            return self.getTypedRuleContext(ai_environmentParser.LlmVersionPropContext,0)


        def llmOtherProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.LlmOtherPropertyContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.LlmOtherPropertyContext,i)


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
        self.enterRule(localctx, 22, self.RULE_llmDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(ai_environmentParser.T__16)
            self.state = 141
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 142
            self.match(ai_environmentParser.T__1)
            self.state = 143
            self.llmIdProp()
            self.state = 144
            self.llmProviderProp()
            self.state = 145
            self.llmModelProp()
            self.state = 146
            self.llmEndpointProp()
            self.state = 147
            self.llmVersionProp()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 148
                self.llmOtherProperty()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
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
        self.enterRule(localctx, 24, self.RULE_llmIdProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(ai_environmentParser.T__12)
            self.state = 157
            self.match(ai_environmentParser.T__7)
            self.state = 158
            self.match(ai_environmentParser.LLMID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlmProviderPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLMPROVIDER(self):
            return self.getToken(ai_environmentParser.LLMPROVIDER, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_llmProviderProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlmProviderProp" ):
                listener.enterLlmProviderProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlmProviderProp" ):
                listener.exitLlmProviderProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlmProviderProp" ):
                return visitor.visitLlmProviderProp(self)
            else:
                return visitor.visitChildren(self)




    def llmProviderProp(self):

        localctx = ai_environmentParser.LlmProviderPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_llmProviderProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(ai_environmentParser.T__17)
            self.state = 161
            self.match(ai_environmentParser.T__7)
            self.state = 162
            self.match(ai_environmentParser.LLMPROVIDER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlmModelPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_llmModelProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlmModelProp" ):
                listener.enterLlmModelProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlmModelProp" ):
                listener.exitLlmModelProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlmModelProp" ):
                return visitor.visitLlmModelProp(self)
            else:
                return visitor.visitChildren(self)




    def llmModelProp(self):

        localctx = ai_environmentParser.LlmModelPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_llmModelProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(ai_environmentParser.T__18)
            self.state = 165
            self.match(ai_environmentParser.T__7)
            self.state = 166
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlmEndpointPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_llmEndpointProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlmEndpointProp" ):
                listener.enterLlmEndpointProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlmEndpointProp" ):
                listener.exitLlmEndpointProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlmEndpointProp" ):
                return visitor.visitLlmEndpointProp(self)
            else:
                return visitor.visitChildren(self)




    def llmEndpointProp(self):

        localctx = ai_environmentParser.LlmEndpointPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_llmEndpointProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ai_environmentParser.T__19)
            self.state = 169
            self.match(ai_environmentParser.T__7)
            self.state = 170
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlmVersionPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_llmVersionProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlmVersionProp" ):
                listener.enterLlmVersionProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlmVersionProp" ):
                listener.exitLlmVersionProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlmVersionProp" ):
                return visitor.visitLlmVersionProp(self)
            else:
                return visitor.visitChildren(self)




    def llmVersionProp(self):

        localctx = ai_environmentParser.LlmVersionPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_llmVersionProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(ai_environmentParser.T__20)
            self.state = 173
            self.match(ai_environmentParser.T__7)
            self.state = 174
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlmOtherPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ai_environmentParser.VAR, 0)

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_llmOtherProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlmOtherProperty" ):
                listener.enterLlmOtherProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlmOtherProperty" ):
                listener.exitLlmOtherProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlmOtherProperty" ):
                return visitor.visitLlmOtherProperty(self)
            else:
                return visitor.visitChildren(self)




    def llmOtherProperty(self):

        localctx = ai_environmentParser.LlmOtherPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_llmOtherProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(ai_environmentParser.VAR)
            self.state = 177
            self.match(ai_environmentParser.T__7)
            self.state = 178
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def toolIdProp(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolIdPropContext,0)


        def toolEndpointProp(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolEndpointPropContext,0)


        def toolTypeProp(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolTypePropContext,0)


        def toolDescriptionProp(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolDescriptionPropContext,0)


        def toolOtherProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.ToolOtherPropertyContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.ToolOtherPropertyContext,i)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_toolDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToolDef" ):
                listener.enterToolDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToolDef" ):
                listener.exitToolDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToolDef" ):
                return visitor.visitToolDef(self)
            else:
                return visitor.visitChildren(self)




    def toolDef(self):

        localctx = ai_environmentParser.ToolDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_toolDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(ai_environmentParser.T__21)
            self.state = 181
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 182
            self.match(ai_environmentParser.T__1)
            self.state = 183
            self.toolIdProp()
            self.state = 184
            self.toolEndpointProp()
            self.state = 185
            self.toolTypeProp()
            self.state = 186
            self.toolDescriptionProp()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 187
                self.toolOtherProperty()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 193
            self.match(ai_environmentParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolIdPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOOLID(self):
            return self.getToken(ai_environmentParser.TOOLID, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_toolIdProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToolIdProp" ):
                listener.enterToolIdProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToolIdProp" ):
                listener.exitToolIdProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToolIdProp" ):
                return visitor.visitToolIdProp(self)
            else:
                return visitor.visitChildren(self)




    def toolIdProp(self):

        localctx = ai_environmentParser.ToolIdPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_toolIdProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(ai_environmentParser.T__12)
            self.state = 196
            self.match(ai_environmentParser.T__7)
            self.state = 197
            self.match(ai_environmentParser.TOOLID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolEndpointPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_toolEndpointProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToolEndpointProp" ):
                listener.enterToolEndpointProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToolEndpointProp" ):
                listener.exitToolEndpointProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToolEndpointProp" ):
                return visitor.visitToolEndpointProp(self)
            else:
                return visitor.visitChildren(self)




    def toolEndpointProp(self):

        localctx = ai_environmentParser.ToolEndpointPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_toolEndpointProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(ai_environmentParser.T__19)
            self.state = 200
            self.match(ai_environmentParser.T__7)
            self.state = 201
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolDescriptionPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_toolDescriptionProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToolDescriptionProp" ):
                listener.enterToolDescriptionProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToolDescriptionProp" ):
                listener.exitToolDescriptionProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToolDescriptionProp" ):
                return visitor.visitToolDescriptionProp(self)
            else:
                return visitor.visitChildren(self)




    def toolDescriptionProp(self):

        localctx = ai_environmentParser.ToolDescriptionPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_toolDescriptionProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(ai_environmentParser.T__22)
            self.state = 204
            self.match(ai_environmentParser.T__7)
            self.state = 205
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolTypePropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOOL_TYPE(self):
            return self.getToken(ai_environmentParser.TOOL_TYPE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_toolTypeProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToolTypeProp" ):
                listener.enterToolTypeProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToolTypeProp" ):
                listener.exitToolTypeProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToolTypeProp" ):
                return visitor.visitToolTypeProp(self)
            else:
                return visitor.visitChildren(self)




    def toolTypeProp(self):

        localctx = ai_environmentParser.ToolTypePropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_toolTypeProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(ai_environmentParser.T__23)
            self.state = 208
            self.match(ai_environmentParser.T__7)
            self.state = 209
            self.match(ai_environmentParser.TOOL_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolOtherPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ai_environmentParser.VAR, 0)

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_toolOtherProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToolOtherProperty" ):
                listener.enterToolOtherProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToolOtherProperty" ):
                listener.exitToolOtherProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToolOtherProperty" ):
                return visitor.visitToolOtherProperty(self)
            else:
                return visitor.visitChildren(self)




    def toolOtherProperty(self):

        localctx = ai_environmentParser.ToolOtherPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_toolOtherProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(ai_environmentParser.VAR)
            self.state = 212
            self.match(ai_environmentParser.T__7)
            self.state = 213
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





