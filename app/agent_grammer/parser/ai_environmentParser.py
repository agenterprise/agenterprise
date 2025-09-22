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
        4,1,33,169,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,52,8,0,10,0,12,0,55,
        9,0,1,0,1,0,1,0,1,0,5,0,61,8,0,10,0,12,0,64,9,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,5,4,81,8,4,10,4,12,4,
        84,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,95,8,5,10,5,12,5,
        98,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,5,12,
        127,8,12,10,12,12,12,130,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,5,13,140,8,13,10,13,12,13,143,9,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,
        1,18,1,18,1,19,1,19,1,19,1,19,1,19,0,0,20,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,0,0,154,0,40,1,0,0,0,2,67,1,0,0,
        0,4,71,1,0,0,0,6,75,1,0,0,0,8,82,1,0,0,0,10,85,1,0,0,0,12,101,1,
        0,0,0,14,105,1,0,0,0,16,109,1,0,0,0,18,113,1,0,0,0,20,117,1,0,0,
        0,22,121,1,0,0,0,24,128,1,0,0,0,26,131,1,0,0,0,28,146,1,0,0,0,30,
        150,1,0,0,0,32,154,1,0,0,0,34,158,1,0,0,0,36,162,1,0,0,0,38,164,
        1,0,0,0,40,41,5,1,0,0,41,42,5,32,0,0,42,43,5,2,0,0,43,44,5,3,0,0,
        44,45,3,2,1,0,45,46,3,4,2,0,46,47,3,6,3,0,47,48,5,4,0,0,48,49,5,
        5,0,0,49,53,5,3,0,0,50,52,3,10,5,0,51,50,1,0,0,0,52,55,1,0,0,0,53,
        51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,0,56,57,5,4,0,
        0,57,58,5,6,0,0,58,62,5,3,0,0,59,61,3,26,13,0,60,59,1,0,0,0,61,64,
        1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,
        65,66,5,4,0,0,66,1,1,0,0,0,67,68,5,7,0,0,68,69,5,8,0,0,69,70,5,32,
        0,0,70,3,1,0,0,0,71,72,5,9,0,0,72,73,5,8,0,0,73,74,5,21,0,0,74,5,
        1,0,0,0,75,76,5,10,0,0,76,77,5,8,0,0,77,78,5,26,0,0,78,7,1,0,0,0,
        79,81,3,10,5,0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,
        0,0,0,83,9,1,0,0,0,84,82,1,0,0,0,85,86,5,11,0,0,86,87,5,32,0,0,87,
        88,5,3,0,0,88,89,3,12,6,0,89,90,3,14,7,0,90,91,3,16,8,0,91,92,3,
        18,9,0,92,96,3,20,10,0,93,95,3,22,11,0,94,93,1,0,0,0,95,98,1,0,0,
        0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,98,96,1,0,0,0,99,100,
        5,4,0,0,100,11,1,0,0,0,101,102,5,12,0,0,102,103,5,8,0,0,103,104,
        5,29,0,0,104,13,1,0,0,0,105,106,5,13,0,0,106,107,5,8,0,0,107,108,
        5,28,0,0,108,15,1,0,0,0,109,110,5,14,0,0,110,111,5,8,0,0,111,112,
        5,32,0,0,112,17,1,0,0,0,113,114,5,15,0,0,114,115,5,8,0,0,115,116,
        5,32,0,0,116,19,1,0,0,0,117,118,5,16,0,0,118,119,5,8,0,0,119,120,
        5,32,0,0,120,21,1,0,0,0,121,122,5,27,0,0,122,123,5,8,0,0,123,124,
        5,32,0,0,124,23,1,0,0,0,125,127,3,26,13,0,126,125,1,0,0,0,127,130,
        1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,25,1,0,0,0,130,128,1,
        0,0,0,131,132,5,17,0,0,132,133,5,32,0,0,133,134,5,3,0,0,134,135,
        3,30,15,0,135,136,3,32,16,0,136,137,3,28,14,0,137,141,3,34,17,0,
        138,140,3,36,18,0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,
        0,141,142,1,0,0,0,142,144,1,0,0,0,143,141,1,0,0,0,144,145,5,4,0,
        0,145,27,1,0,0,0,146,147,5,18,0,0,147,148,5,8,0,0,148,149,5,32,0,
        0,149,29,1,0,0,0,150,151,5,12,0,0,151,152,5,8,0,0,152,153,5,30,0,
        0,153,31,1,0,0,0,154,155,5,19,0,0,155,156,5,8,0,0,156,157,5,31,0,
        0,157,33,1,0,0,0,158,159,5,20,0,0,159,160,5,8,0,0,160,161,5,29,0,
        0,161,35,1,0,0,0,162,163,3,38,19,0,163,37,1,0,0,0,164,165,5,27,0,
        0,165,166,5,8,0,0,166,167,5,32,0,0,167,39,1,0,0,0,6,53,62,82,96,
        128,141
    ]

class ai_environmentParser ( Parser ):

    grammarFileName = "ai_environment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ai_environment'", "'architecture'", 
                     "'{'", "'}'", "'infrastructure'", "'functional'", "'envid'", 
                     "'='", "'app-pattern'", "'techstack'", "'llm'", "'uid'", 
                     "'provider'", "'model'", "'endpoint'", "'version'", 
                     "'agent'", "'systemprompt'", "'namespace'", "'llmref'", 
                     "<INVALID>", "'aiurn:app:microservice'", "'aiurn:app:swarm'", 
                     "'aiurn:app:mcpservice'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "APP", "APP_MICROSERVICE", "APP_SWARM", 
                      "APP_MCPSERVICE", "TECHSTACK_CATEGORY", "TECHSTACK_AIURN", 
                      "VAR", "LLMPROVIDER", "LLMID", "AGENTID", "NAMESPACE", 
                      "STRING", "WS" ]

    RULE_ai_envDef = 0
    RULE_envid = 1
    RULE_appPattern = 2
    RULE_techstack = 3
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
    RULE_otherAgentProperty = 18
    RULE_agentProperty = 19

    ruleNames =  [ "ai_envDef", "envid", "appPattern", "techstack", "llmSet", 
                   "llmDef", "llmIdProp", "llmProviderProp", "llmModelProp", 
                   "llmEndpointProp", "llmVersionProp", "llmOtherProperty", 
                   "prog", "agentDef", "systemPromptProperty", "agentIdentity", 
                   "agentNamespace", "llmRefProperty", "otherAgentProperty", 
                   "agentProperty" ]

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
    APP=21
    APP_MICROSERVICE=22
    APP_SWARM=23
    APP_MCPSERVICE=24
    TECHSTACK_CATEGORY=25
    TECHSTACK_AIURN=26
    VAR=27
    LLMPROVIDER=28
    LLMID=29
    AGENTID=30
    NAMESPACE=31
    STRING=32
    WS=33

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


        def appPattern(self):
            return self.getTypedRuleContext(ai_environmentParser.AppPatternContext,0)


        def techstack(self):
            return self.getTypedRuleContext(ai_environmentParser.TechstackContext,0)


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
            self.state = 40
            self.match(ai_environmentParser.T__0)
            self.state = 41
            self.match(ai_environmentParser.STRING)
            self.state = 42
            self.match(ai_environmentParser.T__1)
            self.state = 43
            self.match(ai_environmentParser.T__2)
            self.state = 44
            self.envid()
            self.state = 45
            self.appPattern()
            self.state = 46
            self.techstack()
            self.state = 47
            self.match(ai_environmentParser.T__3)
            self.state = 48
            self.match(ai_environmentParser.T__4)
            self.state = 49
            self.match(ai_environmentParser.T__2)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 50
                self.llmDef()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(ai_environmentParser.T__3)
            self.state = 57
            self.match(ai_environmentParser.T__5)
            self.state = 58
            self.match(ai_environmentParser.T__2)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 59
                self.agentDef()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
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
            self.state = 67
            self.match(ai_environmentParser.T__6)
            self.state = 68
            self.match(ai_environmentParser.T__7)
            self.state = 69
            self.match(ai_environmentParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AppPatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def APP(self):
            return self.getToken(ai_environmentParser.APP, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_appPattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAppPattern" ):
                listener.enterAppPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAppPattern" ):
                listener.exitAppPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAppPattern" ):
                return visitor.visitAppPattern(self)
            else:
                return visitor.visitChildren(self)




    def appPattern(self):

        localctx = ai_environmentParser.AppPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_appPattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(ai_environmentParser.T__8)
            self.state = 72
            self.match(ai_environmentParser.T__7)
            self.state = 73
            self.match(ai_environmentParser.APP)
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
        self.enterRule(localctx, 6, self.RULE_techstack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(ai_environmentParser.T__9)
            self.state = 76
            self.match(ai_environmentParser.T__7)
            self.state = 77
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
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 79
                self.llmDef()
                self.state = 84
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
            self.state = 85
            self.match(ai_environmentParser.T__10)
            self.state = 86
            self.match(ai_environmentParser.STRING)
            self.state = 87
            self.match(ai_environmentParser.T__2)
            self.state = 88
            self.llmIdProp()
            self.state = 89
            self.llmProviderProp()
            self.state = 90
            self.llmModelProp()
            self.state = 91
            self.llmEndpointProp()
            self.state = 92
            self.llmVersionProp()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 93
                self.llmOtherProperty()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
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
            self.state = 101
            self.match(ai_environmentParser.T__11)
            self.state = 102
            self.match(ai_environmentParser.T__7)
            self.state = 103
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
            self.state = 105
            self.match(ai_environmentParser.T__12)
            self.state = 106
            self.match(ai_environmentParser.T__7)
            self.state = 107
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
            self.state = 109
            self.match(ai_environmentParser.T__13)
            self.state = 110
            self.match(ai_environmentParser.T__7)
            self.state = 111
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
            self.state = 113
            self.match(ai_environmentParser.T__14)
            self.state = 114
            self.match(ai_environmentParser.T__7)
            self.state = 115
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
            self.state = 117
            self.match(ai_environmentParser.T__15)
            self.state = 118
            self.match(ai_environmentParser.T__7)
            self.state = 119
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
            self.state = 121
            self.match(ai_environmentParser.VAR)
            self.state = 122
            self.match(ai_environmentParser.T__7)
            self.state = 123
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
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 125
                self.agentDef()
                self.state = 130
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
        self.enterRule(localctx, 26, self.RULE_agentDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(ai_environmentParser.T__16)
            self.state = 132
            self.match(ai_environmentParser.STRING)
            self.state = 133
            self.match(ai_environmentParser.T__2)
            self.state = 134
            self.agentIdentity()
            self.state = 135
            self.agentNamespace()
            self.state = 136
            self.systemPromptProperty()
            self.state = 137
            self.llmRefProperty()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 138
                self.otherAgentProperty()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
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
            self.state = 146
            self.match(ai_environmentParser.T__17)
            self.state = 147
            self.match(ai_environmentParser.T__7)
            self.state = 148
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
            self.state = 150
            self.match(ai_environmentParser.T__11)
            self.state = 151
            self.match(ai_environmentParser.T__7)
            self.state = 152
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
        self.enterRule(localctx, 32, self.RULE_agentNamespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(ai_environmentParser.T__18)
            self.state = 155
            self.match(ai_environmentParser.T__7)
            self.state = 156
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
        self.enterRule(localctx, 34, self.RULE_llmRefProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(ai_environmentParser.T__19)
            self.state = 159
            self.match(ai_environmentParser.T__7)
            self.state = 160
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
        self.enterRule(localctx, 36, self.RULE_otherAgentProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
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
        self.enterRule(localctx, 38, self.RULE_agentProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(ai_environmentParser.VAR)
            self.state = 165
            self.match(ai_environmentParser.T__7)
            self.state = 166
            self.match(ai_environmentParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





