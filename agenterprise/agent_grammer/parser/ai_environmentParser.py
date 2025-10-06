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
        4,1,42,252,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,69,
        8,0,10,0,12,0,72,9,0,1,0,1,0,1,0,1,0,5,0,78,8,0,10,0,12,0,81,9,0,
        1,0,5,0,84,8,0,10,0,12,0,87,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,
        112,8,4,10,4,12,4,115,9,4,1,4,5,4,118,8,4,10,4,12,4,121,9,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,
        1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,5,11,158,8,11,10,11,12,11,161,9,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,
        1,18,1,18,1,18,5,18,194,8,18,10,18,12,18,197,9,18,1,18,5,18,200,
        8,18,10,18,12,18,203,9,18,1,18,1,18,1,18,1,18,5,18,209,8,18,10,18,
        12,18,212,9,18,1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,
        1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,
        1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,
        1,27,1,27,1,27,0,0,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,0,0,232,0,56,1,0,0,0,2,91,1,
        0,0,0,4,95,1,0,0,0,6,99,1,0,0,0,8,103,1,0,0,0,10,124,1,0,0,0,12,
        128,1,0,0,0,14,132,1,0,0,0,16,136,1,0,0,0,18,140,1,0,0,0,20,144,
        1,0,0,0,22,148,1,0,0,0,24,164,1,0,0,0,26,168,1,0,0,0,28,172,1,0,
        0,0,30,176,1,0,0,0,32,180,1,0,0,0,34,184,1,0,0,0,36,188,1,0,0,0,
        38,215,1,0,0,0,40,219,1,0,0,0,42,223,1,0,0,0,44,228,1,0,0,0,46,233,
        1,0,0,0,48,236,1,0,0,0,50,239,1,0,0,0,52,243,1,0,0,0,54,247,1,0,
        0,0,56,57,5,1,0,0,57,58,5,38,0,0,58,59,5,2,0,0,59,60,5,3,0,0,60,
        61,5,2,0,0,61,62,3,2,1,0,62,63,3,4,2,0,63,64,3,6,3,0,64,65,5,4,0,
        0,65,66,5,5,0,0,66,70,5,2,0,0,67,69,3,22,11,0,68,67,1,0,0,0,69,72,
        1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,70,1,0,0,0,
        73,74,5,4,0,0,74,75,5,6,0,0,75,79,5,2,0,0,76,78,3,8,4,0,77,76,1,
        0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,85,1,0,0,0,81,
        79,1,0,0,0,82,84,3,36,18,0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,
        0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,88,89,5,4,0,0,89,90,
        5,4,0,0,90,1,1,0,0,0,91,92,5,7,0,0,92,93,5,8,0,0,93,94,5,38,0,0,
        94,3,1,0,0,0,95,96,5,9,0,0,96,97,5,8,0,0,97,98,5,29,0,0,98,5,1,0,
        0,0,99,100,5,10,0,0,100,101,5,8,0,0,101,102,5,29,0,0,102,7,1,0,0,
        0,103,104,5,11,0,0,104,105,5,38,0,0,105,106,5,2,0,0,106,107,3,12,
        6,0,107,108,3,14,7,0,108,109,3,10,5,0,109,113,3,16,8,0,110,112,3,
        18,9,0,111,110,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,
        0,0,0,114,119,1,0,0,0,115,113,1,0,0,0,116,118,3,20,10,0,117,116,
        1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,122,
        1,0,0,0,121,119,1,0,0,0,122,123,5,4,0,0,123,9,1,0,0,0,124,125,5,
        12,0,0,125,126,5,8,0,0,126,127,5,38,0,0,127,11,1,0,0,0,128,129,5,
        13,0,0,129,130,5,8,0,0,130,131,5,36,0,0,131,13,1,0,0,0,132,133,5,
        14,0,0,133,134,5,8,0,0,134,135,5,37,0,0,135,15,1,0,0,0,136,137,5,
        15,0,0,137,138,5,8,0,0,138,139,5,32,0,0,139,17,1,0,0,0,140,141,5,
        16,0,0,141,142,5,8,0,0,142,143,5,34,0,0,143,19,1,0,0,0,144,145,5,
        30,0,0,145,146,5,8,0,0,146,147,5,38,0,0,147,21,1,0,0,0,148,149,5,
        17,0,0,149,150,5,38,0,0,150,151,5,2,0,0,151,152,3,24,12,0,152,153,
        3,26,13,0,153,154,3,28,14,0,154,155,3,30,15,0,155,159,3,32,16,0,
        156,158,3,34,17,0,157,156,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,
        0,159,160,1,0,0,0,160,162,1,0,0,0,161,159,1,0,0,0,162,163,5,4,0,
        0,163,23,1,0,0,0,164,165,5,13,0,0,165,166,5,8,0,0,166,167,5,32,0,
        0,167,25,1,0,0,0,168,169,5,18,0,0,169,170,5,8,0,0,170,171,5,31,0,
        0,171,27,1,0,0,0,172,173,5,19,0,0,173,174,5,8,0,0,174,175,5,38,0,
        0,175,29,1,0,0,0,176,177,5,20,0,0,177,178,5,8,0,0,178,179,5,38,0,
        0,179,31,1,0,0,0,180,181,5,21,0,0,181,182,5,8,0,0,182,183,5,38,0,
        0,183,33,1,0,0,0,184,185,5,30,0,0,185,186,5,8,0,0,186,187,5,38,0,
        0,187,35,1,0,0,0,188,189,5,22,0,0,189,190,5,38,0,0,190,191,5,2,0,
        0,191,195,3,38,19,0,192,194,3,42,21,0,193,192,1,0,0,0,194,197,1,
        0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,201,1,0,0,0,197,195,1,
        0,0,0,198,200,3,44,22,0,199,198,1,0,0,0,200,203,1,0,0,0,201,199,
        1,0,0,0,201,202,1,0,0,0,202,204,1,0,0,0,203,201,1,0,0,0,204,205,
        3,40,20,0,205,206,3,52,26,0,206,210,3,50,25,0,207,209,3,54,27,0,
        208,207,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,
        211,213,1,0,0,0,212,210,1,0,0,0,213,214,5,4,0,0,214,37,1,0,0,0,215,
        216,5,13,0,0,216,217,5,8,0,0,217,218,5,34,0,0,218,39,1,0,0,0,219,
        220,5,20,0,0,220,221,5,8,0,0,221,222,5,38,0,0,222,41,1,0,0,0,223,
        224,5,23,0,0,224,225,5,8,0,0,225,226,5,33,0,0,226,227,3,48,24,0,
        227,43,1,0,0,0,228,229,5,24,0,0,229,230,5,8,0,0,230,231,5,33,0,0,
        231,232,3,46,23,0,232,45,1,0,0,0,233,234,5,25,0,0,234,235,5,38,0,
        0,235,47,1,0,0,0,236,237,5,25,0,0,237,238,5,38,0,0,238,49,1,0,0,
        0,239,240,5,26,0,0,240,241,5,8,0,0,241,242,5,38,0,0,242,51,1,0,0,
        0,243,244,5,27,0,0,244,245,5,8,0,0,245,246,5,35,0,0,246,53,1,0,0,
        0,247,248,5,30,0,0,248,249,5,8,0,0,249,250,5,38,0,0,250,55,1,0,0,
        0,9,70,79,85,113,119,159,195,201,210
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
                     "'version'", "'tool'", "'in'", "'out'", "'#'", "'description'", 
                     "'type'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TECHLAYER_RESSOURCE", "TECHLAYER_AIURN", "VAR", "LLMPROVIDER", 
                      "LLMID", "TOOLVAR", "TOOLID", "TOOL_TYPE", "AGENTID", 
                      "AGENTNAMESPACE", "PROPERTYVALUE", "THINK", "WS", 
                      "COMMENT", "ML_COMMENT" ]

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
    RULE_toolInputProperty = 21
    RULE_toolOutputProperty = 22
    RULE_toolOutputPropertyDescription = 23
    RULE_toolInputPropertyDescription = 24
    RULE_toolDescriptionProp = 25
    RULE_toolTypeProp = 26
    RULE_toolOtherProperty = 27

    ruleNames =  [ "ai_envDef", "envId", "architectureServiceStack", "architectureAiStack", 
                   "agentDef", "agentSystemPromptProperty", "agentIdentity", 
                   "agentNamespace", "agentLLMRefProperty", "agentToolRefProperty", 
                   "agentCustomProperty", "llmDef", "llmIdProp", "llmProviderProp", 
                   "llmModelProp", "llmEndpointProp", "llmVersionProp", 
                   "llmOtherProperty", "toolDef", "toolIdProp", "toolEndpointProp", 
                   "toolInputProperty", "toolOutputProperty", "toolOutputPropertyDescription", 
                   "toolInputPropertyDescription", "toolDescriptionProp", 
                   "toolTypeProp", "toolOtherProperty" ]

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
    T__24=25
    T__25=26
    T__26=27
    TECHLAYER_RESSOURCE=28
    TECHLAYER_AIURN=29
    VAR=30
    LLMPROVIDER=31
    LLMID=32
    TOOLVAR=33
    TOOLID=34
    TOOL_TYPE=35
    AGENTID=36
    AGENTNAMESPACE=37
    PROPERTYVALUE=38
    THINK=39
    WS=40
    COMMENT=41
    ML_COMMENT=42

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
            self.state = 56
            self.match(ai_environmentParser.T__0)
            self.state = 57
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 58
            self.match(ai_environmentParser.T__1)
            self.state = 59
            self.match(ai_environmentParser.T__2)
            self.state = 60
            self.match(ai_environmentParser.T__1)
            self.state = 61
            self.envId()
            self.state = 62
            self.architectureServiceStack()
            self.state = 63
            self.architectureAiStack()
            self.state = 64
            self.match(ai_environmentParser.T__3)
            self.state = 65
            self.match(ai_environmentParser.T__4)
            self.state = 66
            self.match(ai_environmentParser.T__1)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 67
                self.llmDef()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self.match(ai_environmentParser.T__3)
            self.state = 74
            self.match(ai_environmentParser.T__5)
            self.state = 75
            self.match(ai_environmentParser.T__1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 76
                self.agentDef()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 82
                self.toolDef()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(ai_environmentParser.T__3)
            self.state = 89
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
            self.state = 91
            self.match(ai_environmentParser.T__6)
            self.state = 92
            self.match(ai_environmentParser.T__7)
            self.state = 93
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
            self.state = 95
            self.match(ai_environmentParser.T__8)
            self.state = 96
            self.match(ai_environmentParser.T__7)
            self.state = 97
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
            self.state = 99
            self.match(ai_environmentParser.T__9)
            self.state = 100
            self.match(ai_environmentParser.T__7)
            self.state = 101
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
            self.state = 103
            self.match(ai_environmentParser.T__10)
            self.state = 104
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 105
            self.match(ai_environmentParser.T__1)
            self.state = 106
            self.agentIdentity()
            self.state = 107
            self.agentNamespace()
            self.state = 108
            self.agentSystemPromptProperty()
            self.state = 109
            self.agentLLMRefProperty()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 110
                self.agentToolRefProperty()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 116
                self.agentCustomProperty()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
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
            self.state = 124
            self.match(ai_environmentParser.T__11)
            self.state = 125
            self.match(ai_environmentParser.T__7)
            self.state = 126
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
            self.state = 128
            self.match(ai_environmentParser.T__12)
            self.state = 129
            self.match(ai_environmentParser.T__7)
            self.state = 130
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
            self.state = 132
            self.match(ai_environmentParser.T__13)
            self.state = 133
            self.match(ai_environmentParser.T__7)
            self.state = 134
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
            self.state = 136
            self.match(ai_environmentParser.T__14)
            self.state = 137
            self.match(ai_environmentParser.T__7)
            self.state = 138
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
            self.state = 140
            self.match(ai_environmentParser.T__15)
            self.state = 141
            self.match(ai_environmentParser.T__7)
            self.state = 142
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
            self.state = 144
            self.match(ai_environmentParser.VAR)
            self.state = 145
            self.match(ai_environmentParser.T__7)
            self.state = 146
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
            self.state = 148
            self.match(ai_environmentParser.T__16)
            self.state = 149
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 150
            self.match(ai_environmentParser.T__1)
            self.state = 151
            self.llmIdProp()
            self.state = 152
            self.llmProviderProp()
            self.state = 153
            self.llmModelProp()
            self.state = 154
            self.llmEndpointProp()
            self.state = 155
            self.llmVersionProp()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 156
                self.llmOtherProperty()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
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
            self.state = 164
            self.match(ai_environmentParser.T__12)
            self.state = 165
            self.match(ai_environmentParser.T__7)
            self.state = 166
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
            self.state = 168
            self.match(ai_environmentParser.T__17)
            self.state = 169
            self.match(ai_environmentParser.T__7)
            self.state = 170
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
            self.state = 172
            self.match(ai_environmentParser.T__18)
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
            self.state = 176
            self.match(ai_environmentParser.T__19)
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
            self.state = 180
            self.match(ai_environmentParser.T__20)
            self.state = 181
            self.match(ai_environmentParser.T__7)
            self.state = 182
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
            self.state = 184
            self.match(ai_environmentParser.VAR)
            self.state = 185
            self.match(ai_environmentParser.T__7)
            self.state = 186
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


        def toolInputProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.ToolInputPropertyContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.ToolInputPropertyContext,i)


        def toolOutputProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.ToolOutputPropertyContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.ToolOutputPropertyContext,i)


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
            self.state = 188
            self.match(ai_environmentParser.T__21)
            self.state = 189
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 190
            self.match(ai_environmentParser.T__1)
            self.state = 191
            self.toolIdProp()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 192
                self.toolInputProperty()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 198
                self.toolOutputProperty()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
            self.toolEndpointProp()
            self.state = 205
            self.toolTypeProp()
            self.state = 206
            self.toolDescriptionProp()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 207
                self.toolOtherProperty()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 213
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
            self.state = 215
            self.match(ai_environmentParser.T__12)
            self.state = 216
            self.match(ai_environmentParser.T__7)
            self.state = 217
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
            self.state = 219
            self.match(ai_environmentParser.T__19)
            self.state = 220
            self.match(ai_environmentParser.T__7)
            self.state = 221
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolInputPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOOLVAR(self):
            return self.getToken(ai_environmentParser.TOOLVAR, 0)

        def toolInputPropertyDescription(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolInputPropertyDescriptionContext,0)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_toolInputProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToolInputProperty" ):
                listener.enterToolInputProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToolInputProperty" ):
                listener.exitToolInputProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToolInputProperty" ):
                return visitor.visitToolInputProperty(self)
            else:
                return visitor.visitChildren(self)




    def toolInputProperty(self):

        localctx = ai_environmentParser.ToolInputPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_toolInputProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(ai_environmentParser.T__22)
            self.state = 224
            self.match(ai_environmentParser.T__7)
            self.state = 225
            self.match(ai_environmentParser.TOOLVAR)
            self.state = 226
            self.toolInputPropertyDescription()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolOutputPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOOLVAR(self):
            return self.getToken(ai_environmentParser.TOOLVAR, 0)

        def toolOutputPropertyDescription(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolOutputPropertyDescriptionContext,0)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_toolOutputProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToolOutputProperty" ):
                listener.enterToolOutputProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToolOutputProperty" ):
                listener.exitToolOutputProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToolOutputProperty" ):
                return visitor.visitToolOutputProperty(self)
            else:
                return visitor.visitChildren(self)




    def toolOutputProperty(self):

        localctx = ai_environmentParser.ToolOutputPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_toolOutputProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(ai_environmentParser.T__23)
            self.state = 229
            self.match(ai_environmentParser.T__7)
            self.state = 230
            self.match(ai_environmentParser.TOOLVAR)
            self.state = 231
            self.toolOutputPropertyDescription()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolOutputPropertyDescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_toolOutputPropertyDescription

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToolOutputPropertyDescription" ):
                listener.enterToolOutputPropertyDescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToolOutputPropertyDescription" ):
                listener.exitToolOutputPropertyDescription(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToolOutputPropertyDescription" ):
                return visitor.visitToolOutputPropertyDescription(self)
            else:
                return visitor.visitChildren(self)




    def toolOutputPropertyDescription(self):

        localctx = ai_environmentParser.ToolOutputPropertyDescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_toolOutputPropertyDescription)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(ai_environmentParser.T__24)
            self.state = 234
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolInputPropertyDescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_toolInputPropertyDescription

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToolInputPropertyDescription" ):
                listener.enterToolInputPropertyDescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToolInputPropertyDescription" ):
                listener.exitToolInputPropertyDescription(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToolInputPropertyDescription" ):
                return visitor.visitToolInputPropertyDescription(self)
            else:
                return visitor.visitChildren(self)




    def toolInputPropertyDescription(self):

        localctx = ai_environmentParser.ToolInputPropertyDescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_toolInputPropertyDescription)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(ai_environmentParser.T__24)
            self.state = 237
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
        self.enterRule(localctx, 50, self.RULE_toolDescriptionProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ai_environmentParser.T__25)
            self.state = 240
            self.match(ai_environmentParser.T__7)
            self.state = 241
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
        self.enterRule(localctx, 52, self.RULE_toolTypeProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(ai_environmentParser.T__26)
            self.state = 244
            self.match(ai_environmentParser.T__7)
            self.state = 245
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
        self.enterRule(localctx, 54, self.RULE_toolOtherProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(ai_environmentParser.VAR)
            self.state = 248
            self.match(ai_environmentParser.T__7)
            self.state = 249
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





