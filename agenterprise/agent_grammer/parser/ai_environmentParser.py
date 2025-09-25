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
        4,1,35,242,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,68,8,0,
        10,0,12,0,71,9,0,1,0,1,0,1,0,1,0,5,0,77,8,0,10,0,12,0,80,9,0,1,0,
        5,0,83,8,0,10,0,12,0,86,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,4,5,4,103,8,4,10,4,12,4,106,9,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,117,8,5,10,5,12,5,120,9,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,
        1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,5,12,149,8,12,10,12,
        12,12,152,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,162,
        8,13,10,13,12,13,165,9,13,1,13,5,13,168,8,13,10,13,12,13,171,9,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,
        1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,20,1,20,
        1,20,1,20,1,21,5,21,202,8,21,10,21,12,21,205,9,21,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,5,22,215,8,22,10,22,12,22,218,9,22,1,22,
        1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,
        1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,0,0,28,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        0,0,223,0,56,1,0,0,0,2,89,1,0,0,0,4,93,1,0,0,0,6,97,1,0,0,0,8,104,
        1,0,0,0,10,107,1,0,0,0,12,123,1,0,0,0,14,127,1,0,0,0,16,131,1,0,
        0,0,18,135,1,0,0,0,20,139,1,0,0,0,22,143,1,0,0,0,24,150,1,0,0,0,
        26,153,1,0,0,0,28,174,1,0,0,0,30,178,1,0,0,0,32,182,1,0,0,0,34,186,
        1,0,0,0,36,190,1,0,0,0,38,194,1,0,0,0,40,196,1,0,0,0,42,203,1,0,
        0,0,44,206,1,0,0,0,46,221,1,0,0,0,48,225,1,0,0,0,50,229,1,0,0,0,
        52,233,1,0,0,0,54,237,1,0,0,0,56,57,5,1,0,0,57,58,5,34,0,0,58,59,
        5,2,0,0,59,60,5,3,0,0,60,61,3,2,1,0,61,62,3,4,2,0,62,63,3,6,3,0,
        63,64,5,4,0,0,64,65,5,5,0,0,65,69,5,3,0,0,66,68,3,10,5,0,67,66,1,
        0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,
        69,1,0,0,0,72,73,5,4,0,0,73,74,5,6,0,0,74,78,5,3,0,0,75,77,3,26,
        13,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,
        84,1,0,0,0,80,78,1,0,0,0,81,83,3,44,22,0,82,81,1,0,0,0,83,86,1,0,
        0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,84,1,0,0,0,87,88,
        5,4,0,0,88,1,1,0,0,0,89,90,5,7,0,0,90,91,5,8,0,0,91,92,5,34,0,0,
        92,3,1,0,0,0,93,94,5,9,0,0,94,95,5,8,0,0,95,96,5,26,0,0,96,5,1,0,
        0,0,97,98,5,10,0,0,98,99,5,8,0,0,99,100,5,26,0,0,100,7,1,0,0,0,101,
        103,3,10,5,0,102,101,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,
        105,1,0,0,0,105,9,1,0,0,0,106,104,1,0,0,0,107,108,5,11,0,0,108,109,
        5,34,0,0,109,110,5,3,0,0,110,111,3,12,6,0,111,112,3,14,7,0,112,113,
        3,16,8,0,113,114,3,18,9,0,114,118,3,20,10,0,115,117,3,22,11,0,116,
        115,1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,
        121,1,0,0,0,120,118,1,0,0,0,121,122,5,4,0,0,122,11,1,0,0,0,123,124,
        5,12,0,0,124,125,5,8,0,0,125,126,5,29,0,0,126,13,1,0,0,0,127,128,
        5,13,0,0,128,129,5,8,0,0,129,130,5,28,0,0,130,15,1,0,0,0,131,132,
        5,14,0,0,132,133,5,8,0,0,133,134,5,34,0,0,134,17,1,0,0,0,135,136,
        5,15,0,0,136,137,5,8,0,0,137,138,5,34,0,0,138,19,1,0,0,0,139,140,
        5,16,0,0,140,141,5,8,0,0,141,142,5,34,0,0,142,21,1,0,0,0,143,144,
        5,27,0,0,144,145,5,8,0,0,145,146,5,34,0,0,146,23,1,0,0,0,147,149,
        3,26,13,0,148,147,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,
        1,0,0,0,151,25,1,0,0,0,152,150,1,0,0,0,153,154,5,17,0,0,154,155,
        5,34,0,0,155,156,5,3,0,0,156,157,3,30,15,0,157,158,3,32,16,0,158,
        159,3,28,14,0,159,163,3,34,17,0,160,162,3,36,18,0,161,160,1,0,0,
        0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,169,1,0,0,
        0,165,163,1,0,0,0,166,168,3,38,19,0,167,166,1,0,0,0,168,171,1,0,
        0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,172,1,0,0,0,171,169,1,0,
        0,0,172,173,5,4,0,0,173,27,1,0,0,0,174,175,5,18,0,0,175,176,5,8,
        0,0,176,177,5,34,0,0,177,29,1,0,0,0,178,179,5,12,0,0,179,180,5,8,
        0,0,180,181,5,32,0,0,181,31,1,0,0,0,182,183,5,19,0,0,183,184,5,8,
        0,0,184,185,5,33,0,0,185,33,1,0,0,0,186,187,5,20,0,0,187,188,5,8,
        0,0,188,189,5,29,0,0,189,35,1,0,0,0,190,191,5,21,0,0,191,192,5,8,
        0,0,192,193,5,30,0,0,193,37,1,0,0,0,194,195,3,40,20,0,195,39,1,0,
        0,0,196,197,5,27,0,0,197,198,5,8,0,0,198,199,5,34,0,0,199,41,1,0,
        0,0,200,202,3,44,22,0,201,200,1,0,0,0,202,205,1,0,0,0,203,201,1,
        0,0,0,203,204,1,0,0,0,204,43,1,0,0,0,205,203,1,0,0,0,206,207,5,22,
        0,0,207,208,5,34,0,0,208,209,5,3,0,0,209,210,3,46,23,0,210,211,3,
        48,24,0,211,212,3,52,26,0,212,216,3,50,25,0,213,215,3,54,27,0,214,
        213,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,
        219,1,0,0,0,218,216,1,0,0,0,219,220,5,4,0,0,220,45,1,0,0,0,221,222,
        5,12,0,0,222,223,5,8,0,0,223,224,5,30,0,0,224,47,1,0,0,0,225,226,
        5,15,0,0,226,227,5,8,0,0,227,228,5,34,0,0,228,49,1,0,0,0,229,230,
        5,23,0,0,230,231,5,8,0,0,231,232,5,34,0,0,232,51,1,0,0,0,233,234,
        5,24,0,0,234,235,5,8,0,0,235,236,5,31,0,0,236,53,1,0,0,0,237,238,
        5,27,0,0,238,239,5,8,0,0,239,240,5,34,0,0,240,55,1,0,0,0,10,69,78,
        84,104,118,150,163,169,203,216
    ]

class ai_environmentParser ( Parser ):

    grammarFileName = "ai_environment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ai_environment'", "'architecture'", 
                     "'{'", "'}'", "'infrastructure'", "'functional'", "'envid'", 
                     "'='", "'service-techstack'", "'ai-techstack'", "'llm'", 
                     "'uid'", "'provider'", "'model'", "'endpoint'", "'version'", 
                     "'agent'", "'systemprompt'", "'namespace'", "'llmref'", 
                     "'toolref'", "'tool'", "'description'", "'type'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TECHSTACK_RESSOURCE", "TECHSTACK_AIURN", 
                      "VAR", "LLMPROVIDER", "LLMID", "TOOLID", "TOOL_TYPE", 
                      "AGENTID", "AGENTNAMESPACE", "STRING", "WS" ]

    RULE_ai_envDef = 0
    RULE_envid = 1
    RULE_serviceStack = 2
    RULE_aiStack = 3
    RULE_llmSet = 4
    RULE_llmDef = 5
    RULE_llmIdProp = 6
    RULE_llmProviderProp = 7
    RULE_llmModelProp = 8
    RULE_llmEndpointProp = 9
    RULE_llmVersionProp = 10
    RULE_llmOtherProperty = 11
    RULE_prog = 12
    RULE_agentDef = 13
    RULE_systemPromptProperty = 14
    RULE_agentIdentity = 15
    RULE_agentNamespace = 16
    RULE_llmRefProperty = 17
    RULE_toolRefProperty = 18
    RULE_otherAgentProperty = 19
    RULE_agentProperty = 20
    RULE_toolSet = 21
    RULE_toolDef = 22
    RULE_toolIdProp = 23
    RULE_toolEndpointProp = 24
    RULE_toolDescription = 25
    RULE_toolTypeProp = 26
    RULE_toolOtherProperty = 27

    ruleNames =  [ "ai_envDef", "envid", "serviceStack", "aiStack", "llmSet", 
                   "llmDef", "llmIdProp", "llmProviderProp", "llmModelProp", 
                   "llmEndpointProp", "llmVersionProp", "llmOtherProperty", 
                   "prog", "agentDef", "systemPromptProperty", "agentIdentity", 
                   "agentNamespace", "llmRefProperty", "toolRefProperty", 
                   "otherAgentProperty", "agentProperty", "toolSet", "toolDef", 
                   "toolIdProp", "toolEndpointProp", "toolDescription", 
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
    TECHSTACK_RESSOURCE=25
    TECHSTACK_AIURN=26
    VAR=27
    LLMPROVIDER=28
    LLMID=29
    TOOLID=30
    TOOL_TYPE=31
    AGENTID=32
    AGENTNAMESPACE=33
    STRING=34
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

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

        def envid(self):
            return self.getTypedRuleContext(ai_environmentParser.EnvidContext,0)


        def serviceStack(self):
            return self.getTypedRuleContext(ai_environmentParser.ServiceStackContext,0)


        def aiStack(self):
            return self.getTypedRuleContext(ai_environmentParser.AiStackContext,0)


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
            self.match(ai_environmentParser.STRING)
            self.state = 58
            self.match(ai_environmentParser.T__1)
            self.state = 59
            self.match(ai_environmentParser.T__2)
            self.state = 60
            self.envid()
            self.state = 61
            self.serviceStack()
            self.state = 62
            self.aiStack()
            self.state = 63
            self.match(ai_environmentParser.T__3)
            self.state = 64
            self.match(ai_environmentParser.T__4)
            self.state = 65
            self.match(ai_environmentParser.T__2)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 66
                self.llmDef()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(ai_environmentParser.T__3)
            self.state = 73
            self.match(ai_environmentParser.T__5)
            self.state = 74
            self.match(ai_environmentParser.T__2)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 75
                self.agentDef()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 81
                self.toolDef()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self.match(ai_environmentParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnvidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_envid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvid" ):
                listener.enterEnvid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvid" ):
                listener.exitEnvid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnvid" ):
                return visitor.visitEnvid(self)
            else:
                return visitor.visitChildren(self)




    def envid(self):

        localctx = ai_environmentParser.EnvidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_envid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(ai_environmentParser.T__6)
            self.state = 90
            self.match(ai_environmentParser.T__7)
            self.state = 91
            self.match(ai_environmentParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServiceStackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TECHSTACK_AIURN(self):
            return self.getToken(ai_environmentParser.TECHSTACK_AIURN, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_serviceStack

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServiceStack" ):
                listener.enterServiceStack(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServiceStack" ):
                listener.exitServiceStack(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitServiceStack" ):
                return visitor.visitServiceStack(self)
            else:
                return visitor.visitChildren(self)




    def serviceStack(self):

        localctx = ai_environmentParser.ServiceStackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_serviceStack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(ai_environmentParser.T__8)
            self.state = 94
            self.match(ai_environmentParser.T__7)
            self.state = 95
            self.match(ai_environmentParser.TECHSTACK_AIURN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AiStackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TECHSTACK_AIURN(self):
            return self.getToken(ai_environmentParser.TECHSTACK_AIURN, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_aiStack

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAiStack" ):
                listener.enterAiStack(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAiStack" ):
                listener.exitAiStack(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAiStack" ):
                return visitor.visitAiStack(self)
            else:
                return visitor.visitChildren(self)




    def aiStack(self):

        localctx = ai_environmentParser.AiStackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_aiStack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(ai_environmentParser.T__9)
            self.state = 98
            self.match(ai_environmentParser.T__7)
            self.state = 99
            self.match(ai_environmentParser.TECHSTACK_AIURN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlmSetContext(ParserRuleContext):
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
            return ai_environmentParser.RULE_llmSet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlmSet" ):
                listener.enterLlmSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlmSet" ):
                listener.exitLlmSet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlmSet" ):
                return visitor.visitLlmSet(self)
            else:
                return visitor.visitChildren(self)




    def llmSet(self):

        localctx = ai_environmentParser.LlmSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_llmSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 101
                self.llmDef()
                self.state = 106
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
        self.enterRule(localctx, 10, self.RULE_llmDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(ai_environmentParser.T__10)
            self.state = 108
            self.match(ai_environmentParser.STRING)
            self.state = 109
            self.match(ai_environmentParser.T__2)
            self.state = 110
            self.llmIdProp()
            self.state = 111
            self.llmProviderProp()
            self.state = 112
            self.llmModelProp()
            self.state = 113
            self.llmEndpointProp()
            self.state = 114
            self.llmVersionProp()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 115
                self.llmOtherProperty()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
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
        self.enterRule(localctx, 12, self.RULE_llmIdProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(ai_environmentParser.T__11)
            self.state = 124
            self.match(ai_environmentParser.T__7)
            self.state = 125
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
        self.enterRule(localctx, 14, self.RULE_llmProviderProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(ai_environmentParser.T__12)
            self.state = 128
            self.match(ai_environmentParser.T__7)
            self.state = 129
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

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

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
        self.enterRule(localctx, 16, self.RULE_llmModelProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(ai_environmentParser.T__13)
            self.state = 132
            self.match(ai_environmentParser.T__7)
            self.state = 133
            self.match(ai_environmentParser.STRING)
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

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

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
        self.enterRule(localctx, 18, self.RULE_llmEndpointProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ai_environmentParser.T__14)
            self.state = 136
            self.match(ai_environmentParser.T__7)
            self.state = 137
            self.match(ai_environmentParser.STRING)
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

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

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
        self.enterRule(localctx, 20, self.RULE_llmVersionProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(ai_environmentParser.T__15)
            self.state = 140
            self.match(ai_environmentParser.T__7)
            self.state = 141
            self.match(ai_environmentParser.STRING)
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

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

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
        self.enterRule(localctx, 22, self.RULE_llmOtherProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(ai_environmentParser.VAR)
            self.state = 144
            self.match(ai_environmentParser.T__7)
            self.state = 145
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
        self.enterRule(localctx, 24, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 147
                self.agentDef()
                self.state = 152
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


        def toolRefProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.ToolRefPropertyContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.ToolRefPropertyContext,i)


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
        self.enterRule(localctx, 26, self.RULE_agentDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(ai_environmentParser.T__16)
            self.state = 154
            self.match(ai_environmentParser.STRING)
            self.state = 155
            self.match(ai_environmentParser.T__2)
            self.state = 156
            self.agentIdentity()
            self.state = 157
            self.agentNamespace()
            self.state = 158
            self.systemPromptProperty()
            self.state = 159
            self.llmRefProperty()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 160
                self.toolRefProperty()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 166
                self.otherAgentProperty()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
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
        self.enterRule(localctx, 28, self.RULE_systemPromptProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(ai_environmentParser.T__17)
            self.state = 175
            self.match(ai_environmentParser.T__7)
            self.state = 176
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
        self.enterRule(localctx, 30, self.RULE_agentIdentity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(ai_environmentParser.T__11)
            self.state = 179
            self.match(ai_environmentParser.T__7)
            self.state = 180
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
        self.enterRule(localctx, 32, self.RULE_agentNamespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(ai_environmentParser.T__18)
            self.state = 183
            self.match(ai_environmentParser.T__7)
            self.state = 184
            self.match(ai_environmentParser.AGENTNAMESPACE)
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
        self.enterRule(localctx, 34, self.RULE_llmRefProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(ai_environmentParser.T__19)
            self.state = 187
            self.match(ai_environmentParser.T__7)
            self.state = 188
            self.match(ai_environmentParser.LLMID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolRefPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOOLID(self):
            return self.getToken(ai_environmentParser.TOOLID, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_toolRefProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToolRefProperty" ):
                listener.enterToolRefProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToolRefProperty" ):
                listener.exitToolRefProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToolRefProperty" ):
                return visitor.visitToolRefProperty(self)
            else:
                return visitor.visitChildren(self)




    def toolRefProperty(self):

        localctx = ai_environmentParser.ToolRefPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_toolRefProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(ai_environmentParser.T__20)
            self.state = 191
            self.match(ai_environmentParser.T__7)
            self.state = 192
            self.match(ai_environmentParser.TOOLID)
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
        self.enterRule(localctx, 38, self.RULE_otherAgentProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
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
        self.enterRule(localctx, 40, self.RULE_agentProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(ai_environmentParser.VAR)
            self.state = 197
            self.match(ai_environmentParser.T__7)
            self.state = 198
            self.match(ai_environmentParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolSetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def toolDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.ToolDefContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.ToolDefContext,i)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_toolSet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToolSet" ):
                listener.enterToolSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToolSet" ):
                listener.exitToolSet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToolSet" ):
                return visitor.visitToolSet(self)
            else:
                return visitor.visitChildren(self)




    def toolSet(self):

        localctx = ai_environmentParser.ToolSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_toolSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 200
                self.toolDef()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

        def toolIdProp(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolIdPropContext,0)


        def toolEndpointProp(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolEndpointPropContext,0)


        def toolTypeProp(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolTypePropContext,0)


        def toolDescription(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolDescriptionContext,0)


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
        self.enterRule(localctx, 44, self.RULE_toolDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(ai_environmentParser.T__21)
            self.state = 207
            self.match(ai_environmentParser.STRING)
            self.state = 208
            self.match(ai_environmentParser.T__2)
            self.state = 209
            self.toolIdProp()
            self.state = 210
            self.toolEndpointProp()
            self.state = 211
            self.toolTypeProp()
            self.state = 212
            self.toolDescription()
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 213
                self.toolOtherProperty()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 219
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
        self.enterRule(localctx, 46, self.RULE_toolIdProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(ai_environmentParser.T__11)
            self.state = 222
            self.match(ai_environmentParser.T__7)
            self.state = 223
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

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

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
        self.enterRule(localctx, 48, self.RULE_toolEndpointProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(ai_environmentParser.T__14)
            self.state = 226
            self.match(ai_environmentParser.T__7)
            self.state = 227
            self.match(ai_environmentParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolDescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_toolDescription

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToolDescription" ):
                listener.enterToolDescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToolDescription" ):
                listener.exitToolDescription(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToolDescription" ):
                return visitor.visitToolDescription(self)
            else:
                return visitor.visitChildren(self)




    def toolDescription(self):

        localctx = ai_environmentParser.ToolDescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_toolDescription)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(ai_environmentParser.T__22)
            self.state = 230
            self.match(ai_environmentParser.T__7)
            self.state = 231
            self.match(ai_environmentParser.STRING)
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
            self.state = 233
            self.match(ai_environmentParser.T__23)
            self.state = 234
            self.match(ai_environmentParser.T__7)
            self.state = 235
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

        def STRING(self):
            return self.getToken(ai_environmentParser.STRING, 0)

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
            self.state = 237
            self.match(ai_environmentParser.VAR)
            self.state = 238
            self.match(ai_environmentParser.T__7)
            self.state = 239
            self.match(ai_environmentParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





