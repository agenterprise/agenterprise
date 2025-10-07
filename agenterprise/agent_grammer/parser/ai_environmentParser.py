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
        4,1,43,288,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,77,8,0,10,0,12,0,80,9,0,1,
        0,1,0,1,0,1,0,5,0,86,8,0,10,0,12,0,89,9,0,1,0,5,0,92,8,0,10,0,12,
        0,95,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,120,8,4,10,4,12,4,123,9,
        4,1,4,5,4,126,8,4,10,4,12,4,129,9,4,1,4,5,4,132,8,4,10,4,12,4,135,
        9,4,1,4,5,4,138,8,4,10,4,12,4,141,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,
        10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,
        13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,5,15,194,8,15,10,15,12,15,197,9,15,1,15,1,15,1,16,1,
        16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,
        19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,
        22,1,22,5,22,230,8,22,10,22,12,22,233,9,22,1,22,5,22,236,8,22,10,
        22,12,22,239,9,22,1,22,1,22,1,22,1,22,5,22,245,8,22,10,22,12,22,
        248,9,22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,
        1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,28,
        1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,
        1,31,1,31,0,0,32,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,0,0,266,0,64,1,0,0,0,2,
        99,1,0,0,0,4,103,1,0,0,0,6,107,1,0,0,0,8,111,1,0,0,0,10,144,1,0,
        0,0,12,148,1,0,0,0,14,152,1,0,0,0,16,156,1,0,0,0,18,160,1,0,0,0,
        20,164,1,0,0,0,22,169,1,0,0,0,24,174,1,0,0,0,26,177,1,0,0,0,28,180,
        1,0,0,0,30,184,1,0,0,0,32,200,1,0,0,0,34,204,1,0,0,0,36,208,1,0,
        0,0,38,212,1,0,0,0,40,216,1,0,0,0,42,220,1,0,0,0,44,224,1,0,0,0,
        46,251,1,0,0,0,48,255,1,0,0,0,50,259,1,0,0,0,52,264,1,0,0,0,54,269,
        1,0,0,0,56,272,1,0,0,0,58,275,1,0,0,0,60,279,1,0,0,0,62,283,1,0,
        0,0,64,65,5,1,0,0,65,66,5,39,0,0,66,67,5,2,0,0,67,68,5,3,0,0,68,
        69,5,2,0,0,69,70,3,2,1,0,70,71,3,4,2,0,71,72,3,6,3,0,72,73,5,4,0,
        0,73,74,5,5,0,0,74,78,5,2,0,0,75,77,3,30,15,0,76,75,1,0,0,0,77,80,
        1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,0,
        81,82,5,4,0,0,82,83,5,6,0,0,83,87,5,2,0,0,84,86,3,8,4,0,85,84,1,
        0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,93,1,0,0,0,89,
        87,1,0,0,0,90,92,3,44,22,0,91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,
        0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,93,1,0,0,0,96,97,5,4,0,0,97,98,
        5,4,0,0,98,1,1,0,0,0,99,100,5,7,0,0,100,101,5,8,0,0,101,102,5,39,
        0,0,102,3,1,0,0,0,103,104,5,9,0,0,104,105,5,8,0,0,105,106,5,29,0,
        0,106,5,1,0,0,0,107,108,5,10,0,0,108,109,5,8,0,0,109,110,5,29,0,
        0,110,7,1,0,0,0,111,112,5,11,0,0,112,113,5,39,0,0,113,114,5,2,0,
        0,114,115,3,12,6,0,115,116,3,14,7,0,116,117,3,10,5,0,117,121,3,16,
        8,0,118,120,3,18,9,0,119,118,1,0,0,0,120,123,1,0,0,0,121,119,1,0,
        0,0,121,122,1,0,0,0,122,127,1,0,0,0,123,121,1,0,0,0,124,126,3,20,
        10,0,125,124,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,
        0,0,128,133,1,0,0,0,129,127,1,0,0,0,130,132,3,22,11,0,131,130,1,
        0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,139,1,
        0,0,0,135,133,1,0,0,0,136,138,3,28,14,0,137,136,1,0,0,0,138,141,
        1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,139,
        1,0,0,0,142,143,5,4,0,0,143,9,1,0,0,0,144,145,5,12,0,0,145,146,5,
        8,0,0,146,147,5,39,0,0,147,11,1,0,0,0,148,149,5,13,0,0,149,150,5,
        8,0,0,150,151,5,36,0,0,151,13,1,0,0,0,152,153,5,14,0,0,153,154,5,
        8,0,0,154,155,5,37,0,0,155,15,1,0,0,0,156,157,5,15,0,0,157,158,5,
        8,0,0,158,159,5,32,0,0,159,17,1,0,0,0,160,161,5,16,0,0,161,162,5,
        8,0,0,162,163,5,34,0,0,163,19,1,0,0,0,164,165,5,17,0,0,165,166,5,
        8,0,0,166,167,5,38,0,0,167,168,3,26,13,0,168,21,1,0,0,0,169,170,
        5,18,0,0,170,171,5,8,0,0,171,172,5,38,0,0,172,173,3,24,12,0,173,
        23,1,0,0,0,174,175,5,19,0,0,175,176,5,39,0,0,176,25,1,0,0,0,177,
        178,5,19,0,0,178,179,5,39,0,0,179,27,1,0,0,0,180,181,5,30,0,0,181,
        182,5,8,0,0,182,183,5,39,0,0,183,29,1,0,0,0,184,185,5,20,0,0,185,
        186,5,39,0,0,186,187,5,2,0,0,187,188,3,32,16,0,188,189,3,34,17,0,
        189,190,3,36,18,0,190,191,3,38,19,0,191,195,3,40,20,0,192,194,3,
        42,21,0,193,192,1,0,0,0,194,197,1,0,0,0,195,193,1,0,0,0,195,196,
        1,0,0,0,196,198,1,0,0,0,197,195,1,0,0,0,198,199,5,4,0,0,199,31,1,
        0,0,0,200,201,5,13,0,0,201,202,5,8,0,0,202,203,5,32,0,0,203,33,1,
        0,0,0,204,205,5,21,0,0,205,206,5,8,0,0,206,207,5,31,0,0,207,35,1,
        0,0,0,208,209,5,22,0,0,209,210,5,8,0,0,210,211,5,39,0,0,211,37,1,
        0,0,0,212,213,5,23,0,0,213,214,5,8,0,0,214,215,5,39,0,0,215,39,1,
        0,0,0,216,217,5,24,0,0,217,218,5,8,0,0,218,219,5,39,0,0,219,41,1,
        0,0,0,220,221,5,30,0,0,221,222,5,8,0,0,222,223,5,39,0,0,223,43,1,
        0,0,0,224,225,5,25,0,0,225,226,5,39,0,0,226,227,5,2,0,0,227,231,
        3,46,23,0,228,230,3,50,25,0,229,228,1,0,0,0,230,233,1,0,0,0,231,
        229,1,0,0,0,231,232,1,0,0,0,232,237,1,0,0,0,233,231,1,0,0,0,234,
        236,3,52,26,0,235,234,1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,237,
        238,1,0,0,0,238,240,1,0,0,0,239,237,1,0,0,0,240,241,3,48,24,0,241,
        242,3,60,30,0,242,246,3,58,29,0,243,245,3,62,31,0,244,243,1,0,0,
        0,245,248,1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,247,249,1,0,0,
        0,248,246,1,0,0,0,249,250,5,4,0,0,250,45,1,0,0,0,251,252,5,13,0,
        0,252,253,5,8,0,0,253,254,5,34,0,0,254,47,1,0,0,0,255,256,5,23,0,
        0,256,257,5,8,0,0,257,258,5,39,0,0,258,49,1,0,0,0,259,260,5,17,0,
        0,260,261,5,8,0,0,261,262,5,33,0,0,262,263,3,56,28,0,263,51,1,0,
        0,0,264,265,5,18,0,0,265,266,5,8,0,0,266,267,5,33,0,0,267,268,3,
        54,27,0,268,53,1,0,0,0,269,270,5,19,0,0,270,271,5,39,0,0,271,55,
        1,0,0,0,272,273,5,19,0,0,273,274,5,39,0,0,274,57,1,0,0,0,275,276,
        5,26,0,0,276,277,5,8,0,0,277,278,5,39,0,0,278,59,1,0,0,0,279,280,
        5,27,0,0,280,281,5,8,0,0,281,282,5,35,0,0,282,61,1,0,0,0,283,284,
        5,30,0,0,284,285,5,8,0,0,285,286,5,39,0,0,286,63,1,0,0,0,11,78,87,
        93,121,127,133,139,195,231,237,246
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
                     "'toolref'", "'in'", "'out'", "'#'", "'llm'", "'provider'", 
                     "'model'", "'endpoint'", "'version'", "'tool'", "'description'", 
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
                      "AGENTNAMESPACE", "AGENTVAR", "PROPERTYVALUE", "THINK", 
                      "WS", "COMMENT", "ML_COMMENT" ]

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
    RULE_agentInputProperty = 10
    RULE_agentOutputProperty = 11
    RULE_agentOutputPropertyDescription = 12
    RULE_agentInputPropertyDescription = 13
    RULE_agentCustomProperty = 14
    RULE_llmDef = 15
    RULE_llmIdProp = 16
    RULE_llmProviderProp = 17
    RULE_llmModelProp = 18
    RULE_llmEndpointProp = 19
    RULE_llmVersionProp = 20
    RULE_llmOtherProperty = 21
    RULE_toolDef = 22
    RULE_toolIdProp = 23
    RULE_toolEndpointProp = 24
    RULE_toolInputProperty = 25
    RULE_toolOutputProperty = 26
    RULE_toolOutputPropertyDescription = 27
    RULE_toolInputPropertyDescription = 28
    RULE_toolDescriptionProp = 29
    RULE_toolTypeProp = 30
    RULE_toolOtherProperty = 31

    ruleNames =  [ "ai_envDef", "envId", "architectureServiceStack", "architectureAiStack", 
                   "agentDef", "agentSystemPromptProperty", "agentIdentity", 
                   "agentNamespace", "agentLLMRefProperty", "agentToolRefProperty", 
                   "agentInputProperty", "agentOutputProperty", "agentOutputPropertyDescription", 
                   "agentInputPropertyDescription", "agentCustomProperty", 
                   "llmDef", "llmIdProp", "llmProviderProp", "llmModelProp", 
                   "llmEndpointProp", "llmVersionProp", "llmOtherProperty", 
                   "toolDef", "toolIdProp", "toolEndpointProp", "toolInputProperty", 
                   "toolOutputProperty", "toolOutputPropertyDescription", 
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
    AGENTVAR=38
    PROPERTYVALUE=39
    THINK=40
    WS=41
    COMMENT=42
    ML_COMMENT=43

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
            self.state = 64
            self.match(ai_environmentParser.T__0)
            self.state = 65
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 66
            self.match(ai_environmentParser.T__1)
            self.state = 67
            self.match(ai_environmentParser.T__2)
            self.state = 68
            self.match(ai_environmentParser.T__1)
            self.state = 69
            self.envId()
            self.state = 70
            self.architectureServiceStack()
            self.state = 71
            self.architectureAiStack()
            self.state = 72
            self.match(ai_environmentParser.T__3)
            self.state = 73
            self.match(ai_environmentParser.T__4)
            self.state = 74
            self.match(ai_environmentParser.T__1)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 75
                self.llmDef()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(ai_environmentParser.T__3)
            self.state = 82
            self.match(ai_environmentParser.T__5)
            self.state = 83
            self.match(ai_environmentParser.T__1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 84
                self.agentDef()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 90
                self.toolDef()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(ai_environmentParser.T__3)
            self.state = 97
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
            self.state = 99
            self.match(ai_environmentParser.T__6)
            self.state = 100
            self.match(ai_environmentParser.T__7)
            self.state = 101
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
            self.state = 103
            self.match(ai_environmentParser.T__8)
            self.state = 104
            self.match(ai_environmentParser.T__7)
            self.state = 105
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
            self.state = 107
            self.match(ai_environmentParser.T__9)
            self.state = 108
            self.match(ai_environmentParser.T__7)
            self.state = 109
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


        def agentInputProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.AgentInputPropertyContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.AgentInputPropertyContext,i)


        def agentOutputProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.AgentOutputPropertyContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.AgentOutputPropertyContext,i)


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
            self.state = 111
            self.match(ai_environmentParser.T__10)
            self.state = 112
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 113
            self.match(ai_environmentParser.T__1)
            self.state = 114
            self.agentIdentity()
            self.state = 115
            self.agentNamespace()
            self.state = 116
            self.agentSystemPromptProperty()
            self.state = 117
            self.agentLLMRefProperty()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 118
                self.agentToolRefProperty()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 124
                self.agentInputProperty()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 130
                self.agentOutputProperty()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 136
                self.agentCustomProperty()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
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
            self.state = 144
            self.match(ai_environmentParser.T__11)
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
            self.state = 148
            self.match(ai_environmentParser.T__12)
            self.state = 149
            self.match(ai_environmentParser.T__7)
            self.state = 150
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
            self.state = 152
            self.match(ai_environmentParser.T__13)
            self.state = 153
            self.match(ai_environmentParser.T__7)
            self.state = 154
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
            self.state = 156
            self.match(ai_environmentParser.T__14)
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
            self.state = 160
            self.match(ai_environmentParser.T__15)
            self.state = 161
            self.match(ai_environmentParser.T__7)
            self.state = 162
            self.match(ai_environmentParser.TOOLID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentInputPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGENTVAR(self):
            return self.getToken(ai_environmentParser.AGENTVAR, 0)

        def agentInputPropertyDescription(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentInputPropertyDescriptionContext,0)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentInputProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentInputProperty" ):
                listener.enterAgentInputProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentInputProperty" ):
                listener.exitAgentInputProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentInputProperty" ):
                return visitor.visitAgentInputProperty(self)
            else:
                return visitor.visitChildren(self)




    def agentInputProperty(self):

        localctx = ai_environmentParser.AgentInputPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_agentInputProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(ai_environmentParser.T__16)
            self.state = 165
            self.match(ai_environmentParser.T__7)
            self.state = 166
            self.match(ai_environmentParser.AGENTVAR)
            self.state = 167
            self.agentInputPropertyDescription()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentOutputPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGENTVAR(self):
            return self.getToken(ai_environmentParser.AGENTVAR, 0)

        def agentOutputPropertyDescription(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentOutputPropertyDescriptionContext,0)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentOutputProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentOutputProperty" ):
                listener.enterAgentOutputProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentOutputProperty" ):
                listener.exitAgentOutputProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentOutputProperty" ):
                return visitor.visitAgentOutputProperty(self)
            else:
                return visitor.visitChildren(self)




    def agentOutputProperty(self):

        localctx = ai_environmentParser.AgentOutputPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_agentOutputProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(ai_environmentParser.T__17)
            self.state = 170
            self.match(ai_environmentParser.T__7)
            self.state = 171
            self.match(ai_environmentParser.AGENTVAR)
            self.state = 172
            self.agentOutputPropertyDescription()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentOutputPropertyDescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentOutputPropertyDescription

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentOutputPropertyDescription" ):
                listener.enterAgentOutputPropertyDescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentOutputPropertyDescription" ):
                listener.exitAgentOutputPropertyDescription(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentOutputPropertyDescription" ):
                return visitor.visitAgentOutputPropertyDescription(self)
            else:
                return visitor.visitChildren(self)




    def agentOutputPropertyDescription(self):

        localctx = ai_environmentParser.AgentOutputPropertyDescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_agentOutputPropertyDescription)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(ai_environmentParser.T__18)
            self.state = 175
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentInputPropertyDescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentInputPropertyDescription

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentInputPropertyDescription" ):
                listener.enterAgentInputPropertyDescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentInputPropertyDescription" ):
                listener.exitAgentInputPropertyDescription(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentInputPropertyDescription" ):
                return visitor.visitAgentInputPropertyDescription(self)
            else:
                return visitor.visitChildren(self)




    def agentInputPropertyDescription(self):

        localctx = ai_environmentParser.AgentInputPropertyDescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_agentInputPropertyDescription)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(ai_environmentParser.T__18)
            self.state = 178
            self.match(ai_environmentParser.PROPERTYVALUE)
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
        self.enterRule(localctx, 28, self.RULE_agentCustomProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(ai_environmentParser.VAR)
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
        self.enterRule(localctx, 30, self.RULE_llmDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(ai_environmentParser.T__19)
            self.state = 185
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 186
            self.match(ai_environmentParser.T__1)
            self.state = 187
            self.llmIdProp()
            self.state = 188
            self.llmProviderProp()
            self.state = 189
            self.llmModelProp()
            self.state = 190
            self.llmEndpointProp()
            self.state = 191
            self.llmVersionProp()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 192
                self.llmOtherProperty()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 198
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
        self.enterRule(localctx, 32, self.RULE_llmIdProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(ai_environmentParser.T__12)
            self.state = 201
            self.match(ai_environmentParser.T__7)
            self.state = 202
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
        self.enterRule(localctx, 34, self.RULE_llmProviderProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(ai_environmentParser.T__20)
            self.state = 205
            self.match(ai_environmentParser.T__7)
            self.state = 206
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
        self.enterRule(localctx, 36, self.RULE_llmModelProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(ai_environmentParser.T__21)
            self.state = 209
            self.match(ai_environmentParser.T__7)
            self.state = 210
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
        self.enterRule(localctx, 38, self.RULE_llmEndpointProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(ai_environmentParser.T__22)
            self.state = 213
            self.match(ai_environmentParser.T__7)
            self.state = 214
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
        self.enterRule(localctx, 40, self.RULE_llmVersionProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(ai_environmentParser.T__23)
            self.state = 217
            self.match(ai_environmentParser.T__7)
            self.state = 218
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
        self.enterRule(localctx, 42, self.RULE_llmOtherProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(ai_environmentParser.VAR)
            self.state = 221
            self.match(ai_environmentParser.T__7)
            self.state = 222
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
        self.enterRule(localctx, 44, self.RULE_toolDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(ai_environmentParser.T__24)
            self.state = 225
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 226
            self.match(ai_environmentParser.T__1)
            self.state = 227
            self.toolIdProp()
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 228
                self.toolInputProperty()
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 234
                self.toolOutputProperty()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 240
            self.toolEndpointProp()
            self.state = 241
            self.toolTypeProp()
            self.state = 242
            self.toolDescriptionProp()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 243
                self.toolOtherProperty()
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 249
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
            self.state = 251
            self.match(ai_environmentParser.T__12)
            self.state = 252
            self.match(ai_environmentParser.T__7)
            self.state = 253
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
        self.enterRule(localctx, 48, self.RULE_toolEndpointProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(ai_environmentParser.T__22)
            self.state = 256
            self.match(ai_environmentParser.T__7)
            self.state = 257
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
        self.enterRule(localctx, 50, self.RULE_toolInputProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(ai_environmentParser.T__16)
            self.state = 260
            self.match(ai_environmentParser.T__7)
            self.state = 261
            self.match(ai_environmentParser.TOOLVAR)
            self.state = 262
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
        self.enterRule(localctx, 52, self.RULE_toolOutputProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(ai_environmentParser.T__17)
            self.state = 265
            self.match(ai_environmentParser.T__7)
            self.state = 266
            self.match(ai_environmentParser.TOOLVAR)
            self.state = 267
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
        self.enterRule(localctx, 54, self.RULE_toolOutputPropertyDescription)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(ai_environmentParser.T__18)
            self.state = 270
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
        self.enterRule(localctx, 56, self.RULE_toolInputPropertyDescription)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ai_environmentParser.T__18)
            self.state = 273
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
        self.enterRule(localctx, 58, self.RULE_toolDescriptionProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(ai_environmentParser.T__25)
            self.state = 276
            self.match(ai_environmentParser.T__7)
            self.state = 277
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
        self.enterRule(localctx, 60, self.RULE_toolTypeProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(ai_environmentParser.T__26)
            self.state = 280
            self.match(ai_environmentParser.T__7)
            self.state = 281
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
        self.enterRule(localctx, 62, self.RULE_toolOtherProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(ai_environmentParser.VAR)
            self.state = 284
            self.match(ai_environmentParser.T__7)
            self.state = 285
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





