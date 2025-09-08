# Generated from app/agent_grammer/parser/agentenvironment.g4 by ANTLR 4.13.2
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
        4,1,15,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,1,1,
        1,1,1,1,1,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,1,1,1,1,2,1,2,1,2,1,
        2,3,2,43,8,2,1,3,5,3,46,8,3,10,3,12,3,49,9,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,5,4,58,8,4,10,4,12,4,61,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,3,9,88,8,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,0,86,0,
        23,1,0,0,0,2,26,1,0,0,0,4,42,1,0,0,0,6,47,1,0,0,0,8,50,1,0,0,0,10,
        64,1,0,0,0,12,68,1,0,0,0,14,72,1,0,0,0,16,76,1,0,0,0,18,87,1,0,0,
        0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,
        1,0,0,0,24,1,1,0,0,0,25,23,1,0,0,0,26,27,5,1,0,0,27,28,5,13,0,0,
        28,29,5,2,0,0,29,33,3,4,2,0,30,32,3,8,4,0,31,30,1,0,0,0,32,35,1,
        0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,36,1,0,0,0,35,33,1,0,0,0,36,
        37,5,3,0,0,37,3,1,0,0,0,38,39,5,4,0,0,39,40,5,5,0,0,40,43,5,11,0,
        0,41,43,5,12,0,0,42,38,1,0,0,0,42,41,1,0,0,0,43,5,1,0,0,0,44,46,
        3,8,4,0,45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,
        48,7,1,0,0,0,49,47,1,0,0,0,50,51,5,6,0,0,51,52,5,13,0,0,52,53,5,
        2,0,0,53,54,3,12,6,0,54,55,3,14,7,0,55,59,3,10,5,0,56,58,3,16,8,
        0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,
        1,0,0,0,61,59,1,0,0,0,62,63,5,3,0,0,63,9,1,0,0,0,64,65,5,7,0,0,65,
        66,5,5,0,0,66,67,5,13,0,0,67,11,1,0,0,0,68,69,5,8,0,0,69,70,5,5,
        0,0,70,71,5,14,0,0,71,13,1,0,0,0,72,73,5,9,0,0,73,74,5,5,0,0,74,
        75,5,14,0,0,75,15,1,0,0,0,76,77,3,18,9,0,77,17,1,0,0,0,78,79,5,7,
        0,0,79,80,5,5,0,0,80,88,5,13,0,0,81,82,5,14,0,0,82,83,5,5,0,0,83,
        88,5,13,0,0,84,85,5,10,0,0,85,86,5,5,0,0,86,88,5,13,0,0,87,78,1,
        0,0,0,87,81,1,0,0,0,87,84,1,0,0,0,88,19,1,0,0,0,6,23,33,42,47,59,
        87
    ]

class agentenvironmentParser ( Parser ):

    grammarFileName = "agentenvironment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'agentenvironment'", "'{'", "'}'", "'runtime'", 
                     "'='", "'agent'", "'systemprompt'", "'uid'", "'namespace'", 
                     "'prompt'", "'KUBE'", "'FLOWISE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "KUBE", "FLOWISE", 
                      "STRING", "ID", "WS" ]

    RULE_env = 0
    RULE_envDef = 1
    RULE_environmentProperty = 2
    RULE_prog = 3
    RULE_agentDef = 4
    RULE_systemPromptProperty = 5
    RULE_agentIdentity = 6
    RULE_agentNamespace = 7
    RULE_otherAgentProperty = 8
    RULE_agentProperty = 9

    ruleNames =  [ "env", "envDef", "environmentProperty", "prog", "agentDef", 
                   "systemPromptProperty", "agentIdentity", "agentNamespace", 
                   "otherAgentProperty", "agentProperty" ]

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
    KUBE=11
    FLOWISE=12
    STRING=13
    ID=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class EnvContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def envDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(agentenvironmentParser.EnvDefContext)
            else:
                return self.getTypedRuleContext(agentenvironmentParser.EnvDefContext,i)


        def getRuleIndex(self):
            return agentenvironmentParser.RULE_env

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnv" ):
                listener.enterEnv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnv" ):
                listener.exitEnv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnv" ):
                return visitor.visitEnv(self)
            else:
                return visitor.visitChildren(self)




    def env(self):

        localctx = agentenvironmentParser.EnvContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_env)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 20
                self.envDef()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnvDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(agentenvironmentParser.STRING, 0)

        def environmentProperty(self):
            return self.getTypedRuleContext(agentenvironmentParser.EnvironmentPropertyContext,0)


        def agentDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(agentenvironmentParser.AgentDefContext)
            else:
                return self.getTypedRuleContext(agentenvironmentParser.AgentDefContext,i)


        def getRuleIndex(self):
            return agentenvironmentParser.RULE_envDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvDef" ):
                listener.enterEnvDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvDef" ):
                listener.exitEnvDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnvDef" ):
                return visitor.visitEnvDef(self)
            else:
                return visitor.visitChildren(self)




    def envDef(self):

        localctx = agentenvironmentParser.EnvDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_envDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(agentenvironmentParser.T__0)
            self.state = 27
            self.match(agentenvironmentParser.STRING)
            self.state = 28
            self.match(agentenvironmentParser.T__1)
            self.state = 29
            self.environmentProperty()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 30
                self.agentDef()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(agentenvironmentParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnvironmentPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KUBE(self):
            return self.getToken(agentenvironmentParser.KUBE, 0)

        def FLOWISE(self):
            return self.getToken(agentenvironmentParser.FLOWISE, 0)

        def getRuleIndex(self):
            return agentenvironmentParser.RULE_environmentProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvironmentProperty" ):
                listener.enterEnvironmentProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvironmentProperty" ):
                listener.exitEnvironmentProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnvironmentProperty" ):
                return visitor.visitEnvironmentProperty(self)
            else:
                return visitor.visitChildren(self)




    def environmentProperty(self):

        localctx = agentenvironmentParser.EnvironmentPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_environmentProperty)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(agentenvironmentParser.T__3)
                self.state = 39
                self.match(agentenvironmentParser.T__4)
                self.state = 40
                self.match(agentenvironmentParser.KUBE)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(agentenvironmentParser.FLOWISE)
                pass
            else:
                raise NoViableAltException(self)

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
                return self.getTypedRuleContexts(agentenvironmentParser.AgentDefContext)
            else:
                return self.getTypedRuleContext(agentenvironmentParser.AgentDefContext,i)


        def getRuleIndex(self):
            return agentenvironmentParser.RULE_prog

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

        localctx = agentenvironmentParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 44
                self.agentDef()
                self.state = 49
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
            return self.getToken(agentenvironmentParser.STRING, 0)

        def agentIdentity(self):
            return self.getTypedRuleContext(agentenvironmentParser.AgentIdentityContext,0)


        def agentNamespace(self):
            return self.getTypedRuleContext(agentenvironmentParser.AgentNamespaceContext,0)


        def systemPromptProperty(self):
            return self.getTypedRuleContext(agentenvironmentParser.SystemPromptPropertyContext,0)


        def otherAgentProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(agentenvironmentParser.OtherAgentPropertyContext)
            else:
                return self.getTypedRuleContext(agentenvironmentParser.OtherAgentPropertyContext,i)


        def getRuleIndex(self):
            return agentenvironmentParser.RULE_agentDef

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

        localctx = agentenvironmentParser.AgentDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_agentDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(agentenvironmentParser.T__5)
            self.state = 51
            self.match(agentenvironmentParser.STRING)
            self.state = 52
            self.match(agentenvironmentParser.T__1)
            self.state = 53
            self.agentIdentity()
            self.state = 54
            self.agentNamespace()
            self.state = 55
            self.systemPromptProperty()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17536) != 0):
                self.state = 56
                self.otherAgentProperty()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(agentenvironmentParser.T__2)
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
            return self.getToken(agentenvironmentParser.STRING, 0)

        def getRuleIndex(self):
            return agentenvironmentParser.RULE_systemPromptProperty

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

        localctx = agentenvironmentParser.SystemPromptPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_systemPromptProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(agentenvironmentParser.T__6)
            self.state = 65
            self.match(agentenvironmentParser.T__4)
            self.state = 66
            self.match(agentenvironmentParser.STRING)
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

        def ID(self):
            return self.getToken(agentenvironmentParser.ID, 0)

        def getRuleIndex(self):
            return agentenvironmentParser.RULE_agentIdentity

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

        localctx = agentenvironmentParser.AgentIdentityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_agentIdentity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(agentenvironmentParser.T__7)
            self.state = 69
            self.match(agentenvironmentParser.T__4)
            self.state = 70
            self.match(agentenvironmentParser.ID)
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

        def ID(self):
            return self.getToken(agentenvironmentParser.ID, 0)

        def getRuleIndex(self):
            return agentenvironmentParser.RULE_agentNamespace

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

        localctx = agentenvironmentParser.AgentNamespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_agentNamespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(agentenvironmentParser.T__8)
            self.state = 73
            self.match(agentenvironmentParser.T__4)
            self.state = 74
            self.match(agentenvironmentParser.ID)
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
            return self.getTypedRuleContext(agentenvironmentParser.AgentPropertyContext,0)


        def getRuleIndex(self):
            return agentenvironmentParser.RULE_otherAgentProperty

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

        localctx = agentenvironmentParser.OtherAgentPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_otherAgentProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
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

        def STRING(self):
            return self.getToken(agentenvironmentParser.STRING, 0)

        def ID(self):
            return self.getToken(agentenvironmentParser.ID, 0)

        def getRuleIndex(self):
            return agentenvironmentParser.RULE_agentProperty

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

        localctx = agentenvironmentParser.AgentPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_agentProperty)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(agentenvironmentParser.T__6)
                self.state = 79
                self.match(agentenvironmentParser.T__4)
                self.state = 80
                self.match(agentenvironmentParser.STRING)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.match(agentenvironmentParser.ID)
                self.state = 82
                self.match(agentenvironmentParser.T__4)
                self.state = 83
                self.match(agentenvironmentParser.STRING)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.match(agentenvironmentParser.T__9)
                self.state = 85
                self.match(agentenvironmentParser.T__4)
                self.state = 86
                self.match(agentenvironmentParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





