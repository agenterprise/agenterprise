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
        4,1,53,313,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,5,0,85,8,0,10,0,12,0,88,9,0,1,0,1,0,1,0,1,0,5,0,94,8,0,10,
        0,12,0,97,9,0,1,0,1,0,1,0,1,0,5,0,103,8,0,10,0,12,0,106,9,0,1,0,
        5,0,109,8,0,10,0,12,0,112,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,5,6,142,8,6,10,6,12,6,145,9,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,5,11,173,8,11,10,11,12,11,176,9,11,
        1,11,3,11,179,8,11,1,11,3,11,182,8,11,1,11,5,11,185,8,11,10,11,12,
        11,188,9,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,
        14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,
        17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,5,20,233,8,20,10,20,12,20,236,9,
        20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,
        23,1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,
        26,1,27,1,27,1,27,1,27,1,27,3,27,269,8,27,1,27,3,27,272,8,27,1,27,
        1,27,1,27,1,27,5,27,278,8,27,10,27,12,27,281,9,27,1,27,1,27,1,28,
        1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,
        1,31,1,31,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,1,34,
        1,34,1,34,0,0,35,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,0,2,1,0,38,39,
        2,0,37,37,40,40,290,0,70,1,0,0,0,2,116,1,0,0,0,4,120,1,0,0,0,6,124,
        1,0,0,0,8,128,1,0,0,0,10,132,1,0,0,0,12,136,1,0,0,0,14,148,1,0,0,
        0,16,152,1,0,0,0,18,158,1,0,0,0,20,161,1,0,0,0,22,164,1,0,0,0,24,
        191,1,0,0,0,26,195,1,0,0,0,28,199,1,0,0,0,30,203,1,0,0,0,32,207,
        1,0,0,0,34,211,1,0,0,0,36,215,1,0,0,0,38,219,1,0,0,0,40,223,1,0,
        0,0,42,239,1,0,0,0,44,243,1,0,0,0,46,247,1,0,0,0,48,251,1,0,0,0,
        50,255,1,0,0,0,52,259,1,0,0,0,54,263,1,0,0,0,56,284,1,0,0,0,58,288,
        1,0,0,0,60,292,1,0,0,0,62,296,1,0,0,0,64,300,1,0,0,0,66,304,1,0,
        0,0,68,308,1,0,0,0,70,71,5,1,0,0,71,72,5,49,0,0,72,73,5,2,0,0,73,
        74,5,3,0,0,74,75,5,2,0,0,75,76,3,2,1,0,76,77,3,4,2,0,77,78,3,6,3,
        0,78,79,3,8,4,0,79,80,3,10,5,0,80,81,5,4,0,0,81,82,5,5,0,0,82,86,
        5,2,0,0,83,85,3,12,6,0,84,83,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,
        86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,0,89,90,5,4,0,0,90,91,5,
        6,0,0,91,95,5,2,0,0,92,94,3,40,20,0,93,92,1,0,0,0,94,97,1,0,0,0,
        95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,0,98,99,5,
        4,0,0,99,100,5,7,0,0,100,104,5,2,0,0,101,103,3,22,11,0,102,101,1,
        0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,110,1,
        0,0,0,106,104,1,0,0,0,107,109,3,54,27,0,108,107,1,0,0,0,109,112,
        1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,113,1,0,0,0,112,110,
        1,0,0,0,113,114,5,4,0,0,114,115,5,4,0,0,115,1,1,0,0,0,116,117,5,
        8,0,0,117,118,5,9,0,0,118,119,5,49,0,0,119,3,1,0,0,0,120,121,5,10,
        0,0,121,122,5,9,0,0,122,123,5,35,0,0,123,5,1,0,0,0,124,125,5,11,
        0,0,125,126,5,9,0,0,126,127,5,35,0,0,127,7,1,0,0,0,128,129,5,12,
        0,0,129,130,5,9,0,0,130,131,5,35,0,0,131,9,1,0,0,0,132,133,5,13,
        0,0,133,134,5,9,0,0,134,135,5,35,0,0,135,11,1,0,0,0,136,137,5,14,
        0,0,137,138,5,49,0,0,138,139,5,2,0,0,139,143,3,14,7,0,140,142,3,
        16,8,0,141,140,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,
        0,0,0,144,146,1,0,0,0,145,143,1,0,0,0,146,147,5,4,0,0,147,13,1,0,
        0,0,148,149,5,15,0,0,149,150,5,9,0,0,150,151,5,37,0,0,151,15,1,0,
        0,0,152,153,5,16,0,0,153,154,5,9,0,0,154,155,7,0,0,0,155,156,3,18,
        9,0,156,157,3,20,10,0,157,17,1,0,0,0,158,159,5,17,0,0,159,160,7,
        1,0,0,160,19,1,0,0,0,161,162,5,18,0,0,162,163,5,49,0,0,163,21,1,
        0,0,0,164,165,5,19,0,0,165,166,5,49,0,0,166,167,5,2,0,0,167,168,
        3,26,13,0,168,169,3,28,14,0,169,170,3,24,12,0,170,174,3,30,15,0,
        171,173,3,32,16,0,172,171,1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,
        0,174,175,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,177,179,3,34,17,
        0,178,177,1,0,0,0,178,179,1,0,0,0,179,181,1,0,0,0,180,182,3,36,18,
        0,181,180,1,0,0,0,181,182,1,0,0,0,182,186,1,0,0,0,183,185,3,38,19,
        0,184,183,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,
        0,187,189,1,0,0,0,188,186,1,0,0,0,189,190,5,4,0,0,190,23,1,0,0,0,
        191,192,5,20,0,0,192,193,5,9,0,0,193,194,5,49,0,0,194,25,1,0,0,0,
        195,196,5,15,0,0,196,197,5,9,0,0,197,198,5,46,0,0,198,27,1,0,0,0,
        199,200,5,21,0,0,200,201,5,9,0,0,201,202,5,47,0,0,202,29,1,0,0,0,
        203,204,5,22,0,0,204,205,5,9,0,0,205,206,5,42,0,0,206,31,1,0,0,0,
        207,208,5,23,0,0,208,209,5,9,0,0,209,210,5,44,0,0,210,33,1,0,0,0,
        211,212,5,24,0,0,212,213,5,9,0,0,213,214,5,37,0,0,214,35,1,0,0,0,
        215,216,5,25,0,0,216,217,5,9,0,0,217,218,5,37,0,0,218,37,1,0,0,0,
        219,220,5,36,0,0,220,221,5,9,0,0,221,222,5,49,0,0,222,39,1,0,0,0,
        223,224,5,26,0,0,224,225,5,49,0,0,225,226,5,2,0,0,226,227,3,42,21,
        0,227,228,3,44,22,0,228,229,3,46,23,0,229,230,3,48,24,0,230,234,
        3,50,25,0,231,233,3,52,26,0,232,231,1,0,0,0,233,236,1,0,0,0,234,
        232,1,0,0,0,234,235,1,0,0,0,235,237,1,0,0,0,236,234,1,0,0,0,237,
        238,5,4,0,0,238,41,1,0,0,0,239,240,5,15,0,0,240,241,5,9,0,0,241,
        242,5,42,0,0,242,43,1,0,0,0,243,244,5,27,0,0,244,245,5,9,0,0,245,
        246,5,41,0,0,246,45,1,0,0,0,247,248,5,28,0,0,248,249,5,9,0,0,249,
        250,5,49,0,0,250,47,1,0,0,0,251,252,5,29,0,0,252,253,5,9,0,0,253,
        254,5,49,0,0,254,49,1,0,0,0,255,256,5,30,0,0,256,257,5,9,0,0,257,
        258,5,49,0,0,258,51,1,0,0,0,259,260,5,36,0,0,260,261,5,9,0,0,261,
        262,5,49,0,0,262,53,1,0,0,0,263,264,5,31,0,0,264,265,5,49,0,0,265,
        266,5,2,0,0,266,268,3,56,28,0,267,269,3,60,30,0,268,267,1,0,0,0,
        268,269,1,0,0,0,269,271,1,0,0,0,270,272,3,62,31,0,271,270,1,0,0,
        0,271,272,1,0,0,0,272,273,1,0,0,0,273,274,3,58,29,0,274,275,3,66,
        33,0,275,279,3,64,32,0,276,278,3,68,34,0,277,276,1,0,0,0,278,281,
        1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,0,280,282,1,0,0,0,281,279,
        1,0,0,0,282,283,5,4,0,0,283,55,1,0,0,0,284,285,5,15,0,0,285,286,
        5,9,0,0,286,287,5,44,0,0,287,57,1,0,0,0,288,289,5,29,0,0,289,290,
        5,9,0,0,290,291,5,49,0,0,291,59,1,0,0,0,292,293,5,24,0,0,293,294,
        5,9,0,0,294,295,5,37,0,0,295,61,1,0,0,0,296,297,5,25,0,0,297,298,
        5,9,0,0,298,299,5,37,0,0,299,63,1,0,0,0,300,301,5,32,0,0,301,302,
        5,9,0,0,302,303,5,49,0,0,303,65,1,0,0,0,304,305,5,33,0,0,305,306,
        5,9,0,0,306,307,5,45,0,0,307,67,1,0,0,0,308,309,5,36,0,0,309,310,
        5,9,0,0,310,311,5,49,0,0,311,69,1,0,0,0,13,86,95,104,110,143,174,
        178,181,186,234,268,271,279
    ]

class ai_environmentParser ( Parser ):

    grammarFileName = "ai_environment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ai_environment'", "'{'", "'architecture'", 
                     "'}'", "'data'", "'infrastructure'", "'functional'", 
                     "'envid'", "'='", "'service-techlayer'", "'ai-techlayer'", 
                     "'data-techlayer'", "'agentic-middleware-techlayer'", 
                     "'entity'", "'uid'", "'element'", "'->'", "'#'", "'agent'", 
                     "'systemprompt'", "'namespace'", "'llmref'", "'toolref'", 
                     "'in'", "'out'", "'llm'", "'provider'", "'model'", 
                     "'endpoint'", "'version'", "'tool'", "'description'", 
                     "'type'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "TECHLAYER_RESSOURCE", "TECHLAYER_AIURN", 
                      "VAR", "ENTITY_ID", "ENTITY_VAR", "ENTITY_CONSTANT", 
                      "ENTITY_TYPE", "LLMPROVIDER", "LLMID", "TOOLVAR", 
                      "TOOLID", "TOOL_TYPE", "AGENTID", "AGENTNAMESPACE", 
                      "AGENTVAR", "PROPERTYVALUE", "THINK", "WS", "COMMENT", 
                      "ML_COMMENT" ]

    RULE_ai_envDef = 0
    RULE_envId = 1
    RULE_architectureServiceStack = 2
    RULE_architectureAiStack = 3
    RULE_architectureDataStack = 4
    RULE_architectureAgenticMiddlewareStack = 5
    RULE_entityDef = 6
    RULE_entityIdProp = 7
    RULE_entityElementProp = 8
    RULE_entityElementType = 9
    RULE_entityElementDescription = 10
    RULE_agentDef = 11
    RULE_agentSystemPromptProperty = 12
    RULE_agentIdentity = 13
    RULE_agentNamespace = 14
    RULE_agentLLMRefProperty = 15
    RULE_agentToolRefProperty = 16
    RULE_agentInputProperty = 17
    RULE_agentOutputProperty = 18
    RULE_agentCustomProperty = 19
    RULE_llmDef = 20
    RULE_llmIdProp = 21
    RULE_llmProviderProp = 22
    RULE_llmModelProp = 23
    RULE_llmEndpointProp = 24
    RULE_llmVersionProp = 25
    RULE_llmOtherProperty = 26
    RULE_toolDef = 27
    RULE_toolIdProp = 28
    RULE_toolEndpointProp = 29
    RULE_toolInputProperty = 30
    RULE_toolOutputProperty = 31
    RULE_toolDescriptionProp = 32
    RULE_toolTypeProp = 33
    RULE_toolOtherProperty = 34

    ruleNames =  [ "ai_envDef", "envId", "architectureServiceStack", "architectureAiStack", 
                   "architectureDataStack", "architectureAgenticMiddlewareStack", 
                   "entityDef", "entityIdProp", "entityElementProp", "entityElementType", 
                   "entityElementDescription", "agentDef", "agentSystemPromptProperty", 
                   "agentIdentity", "agentNamespace", "agentLLMRefProperty", 
                   "agentToolRefProperty", "agentInputProperty", "agentOutputProperty", 
                   "agentCustomProperty", "llmDef", "llmIdProp", "llmProviderProp", 
                   "llmModelProp", "llmEndpointProp", "llmVersionProp", 
                   "llmOtherProperty", "toolDef", "toolIdProp", "toolEndpointProp", 
                   "toolInputProperty", "toolOutputProperty", "toolDescriptionProp", 
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
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    TECHLAYER_RESSOURCE=34
    TECHLAYER_AIURN=35
    VAR=36
    ENTITY_ID=37
    ENTITY_VAR=38
    ENTITY_CONSTANT=39
    ENTITY_TYPE=40
    LLMPROVIDER=41
    LLMID=42
    TOOLVAR=43
    TOOLID=44
    TOOL_TYPE=45
    AGENTID=46
    AGENTNAMESPACE=47
    AGENTVAR=48
    PROPERTYVALUE=49
    THINK=50
    WS=51
    COMMENT=52
    ML_COMMENT=53

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


        def architectureDataStack(self):
            return self.getTypedRuleContext(ai_environmentParser.ArchitectureDataStackContext,0)


        def architectureAgenticMiddlewareStack(self):
            return self.getTypedRuleContext(ai_environmentParser.ArchitectureAgenticMiddlewareStackContext,0)


        def entityDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.EntityDefContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.EntityDefContext,i)


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
            self.state = 70
            self.match(ai_environmentParser.T__0)
            self.state = 71
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 72
            self.match(ai_environmentParser.T__1)
            self.state = 73
            self.match(ai_environmentParser.T__2)
            self.state = 74
            self.match(ai_environmentParser.T__1)
            self.state = 75
            self.envId()
            self.state = 76
            self.architectureServiceStack()
            self.state = 77
            self.architectureAiStack()
            self.state = 78
            self.architectureDataStack()
            self.state = 79
            self.architectureAgenticMiddlewareStack()
            self.state = 80
            self.match(ai_environmentParser.T__3)
            self.state = 81
            self.match(ai_environmentParser.T__4)
            self.state = 82
            self.match(ai_environmentParser.T__1)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 83
                self.entityDef()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(ai_environmentParser.T__3)
            self.state = 90
            self.match(ai_environmentParser.T__5)
            self.state = 91
            self.match(ai_environmentParser.T__1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 92
                self.llmDef()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(ai_environmentParser.T__3)
            self.state = 99
            self.match(ai_environmentParser.T__6)
            self.state = 100
            self.match(ai_environmentParser.T__1)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 101
                self.agentDef()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 107
                self.toolDef()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self.match(ai_environmentParser.T__3)
            self.state = 114
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
            self.state = 116
            self.match(ai_environmentParser.T__7)
            self.state = 117
            self.match(ai_environmentParser.T__8)
            self.state = 118
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
            self.state = 120
            self.match(ai_environmentParser.T__9)
            self.state = 121
            self.match(ai_environmentParser.T__8)
            self.state = 122
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
            self.state = 124
            self.match(ai_environmentParser.T__10)
            self.state = 125
            self.match(ai_environmentParser.T__8)
            self.state = 126
            self.match(ai_environmentParser.TECHLAYER_AIURN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArchitectureDataStackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TECHLAYER_AIURN(self):
            return self.getToken(ai_environmentParser.TECHLAYER_AIURN, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_architectureDataStack

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArchitectureDataStack" ):
                listener.enterArchitectureDataStack(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArchitectureDataStack" ):
                listener.exitArchitectureDataStack(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArchitectureDataStack" ):
                return visitor.visitArchitectureDataStack(self)
            else:
                return visitor.visitChildren(self)




    def architectureDataStack(self):

        localctx = ai_environmentParser.ArchitectureDataStackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_architectureDataStack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(ai_environmentParser.T__11)
            self.state = 129
            self.match(ai_environmentParser.T__8)
            self.state = 130
            self.match(ai_environmentParser.TECHLAYER_AIURN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArchitectureAgenticMiddlewareStackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TECHLAYER_AIURN(self):
            return self.getToken(ai_environmentParser.TECHLAYER_AIURN, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_architectureAgenticMiddlewareStack

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArchitectureAgenticMiddlewareStack" ):
                listener.enterArchitectureAgenticMiddlewareStack(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArchitectureAgenticMiddlewareStack" ):
                listener.exitArchitectureAgenticMiddlewareStack(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArchitectureAgenticMiddlewareStack" ):
                return visitor.visitArchitectureAgenticMiddlewareStack(self)
            else:
                return visitor.visitChildren(self)




    def architectureAgenticMiddlewareStack(self):

        localctx = ai_environmentParser.ArchitectureAgenticMiddlewareStackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_architectureAgenticMiddlewareStack)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(ai_environmentParser.T__12)
            self.state = 133
            self.match(ai_environmentParser.T__8)
            self.state = 134
            self.match(ai_environmentParser.TECHLAYER_AIURN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def entityIdProp(self):
            return self.getTypedRuleContext(ai_environmentParser.EntityIdPropContext,0)


        def entityElementProp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.EntityElementPropContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.EntityElementPropContext,i)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_entityDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityDef" ):
                listener.enterEntityDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityDef" ):
                listener.exitEntityDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntityDef" ):
                return visitor.visitEntityDef(self)
            else:
                return visitor.visitChildren(self)




    def entityDef(self):

        localctx = ai_environmentParser.EntityDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_entityDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(ai_environmentParser.T__13)
            self.state = 137
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 138
            self.match(ai_environmentParser.T__1)
            self.state = 139
            self.entityIdProp()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 140
                self.entityElementProp()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.match(ai_environmentParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityIdPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTITY_ID(self):
            return self.getToken(ai_environmentParser.ENTITY_ID, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_entityIdProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityIdProp" ):
                listener.enterEntityIdProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityIdProp" ):
                listener.exitEntityIdProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntityIdProp" ):
                return visitor.visitEntityIdProp(self)
            else:
                return visitor.visitChildren(self)




    def entityIdProp(self):

        localctx = ai_environmentParser.EntityIdPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_entityIdProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ai_environmentParser.T__14)
            self.state = 149
            self.match(ai_environmentParser.T__8)
            self.state = 150
            self.match(ai_environmentParser.ENTITY_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityElementPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entityElementType(self):
            return self.getTypedRuleContext(ai_environmentParser.EntityElementTypeContext,0)


        def entityElementDescription(self):
            return self.getTypedRuleContext(ai_environmentParser.EntityElementDescriptionContext,0)


        def ENTITY_VAR(self):
            return self.getToken(ai_environmentParser.ENTITY_VAR, 0)

        def ENTITY_CONSTANT(self):
            return self.getToken(ai_environmentParser.ENTITY_CONSTANT, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_entityElementProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityElementProp" ):
                listener.enterEntityElementProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityElementProp" ):
                listener.exitEntityElementProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntityElementProp" ):
                return visitor.visitEntityElementProp(self)
            else:
                return visitor.visitChildren(self)




    def entityElementProp(self):

        localctx = ai_environmentParser.EntityElementPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_entityElementProp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(ai_environmentParser.T__15)
            self.state = 153
            self.match(ai_environmentParser.T__8)
            self.state = 154
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 155
            self.entityElementType()
            self.state = 156
            self.entityElementDescription()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityElementTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTITY_TYPE(self):
            return self.getToken(ai_environmentParser.ENTITY_TYPE, 0)

        def ENTITY_ID(self):
            return self.getToken(ai_environmentParser.ENTITY_ID, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_entityElementType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityElementType" ):
                listener.enterEntityElementType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityElementType" ):
                listener.exitEntityElementType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntityElementType" ):
                return visitor.visitEntityElementType(self)
            else:
                return visitor.visitChildren(self)




    def entityElementType(self):

        localctx = ai_environmentParser.EntityElementTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_entityElementType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(ai_environmentParser.T__16)
            self.state = 159
            _la = self._input.LA(1)
            if not(_la==37 or _la==40):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityElementDescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_entityElementDescription

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityElementDescription" ):
                listener.enterEntityElementDescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityElementDescription" ):
                listener.exitEntityElementDescription(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntityElementDescription" ):
                return visitor.visitEntityElementDescription(self)
            else:
                return visitor.visitChildren(self)




    def entityElementDescription(self):

        localctx = ai_environmentParser.EntityElementDescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_entityElementDescription)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(ai_environmentParser.T__17)
            self.state = 162
            self.match(ai_environmentParser.PROPERTYVALUE)
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


        def agentInputProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentInputPropertyContext,0)


        def agentOutputProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentOutputPropertyContext,0)


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
        self.enterRule(localctx, 22, self.RULE_agentDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(ai_environmentParser.T__18)
            self.state = 165
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 166
            self.match(ai_environmentParser.T__1)
            self.state = 167
            self.agentIdentity()
            self.state = 168
            self.agentNamespace()
            self.state = 169
            self.agentSystemPromptProperty()
            self.state = 170
            self.agentLLMRefProperty()
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 171
                self.agentToolRefProperty()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 177
                self.agentInputProperty()


            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 180
                self.agentOutputProperty()


            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 183
                self.agentCustomProperty()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 189
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
        self.enterRule(localctx, 24, self.RULE_agentSystemPromptProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(ai_environmentParser.T__19)
            self.state = 192
            self.match(ai_environmentParser.T__8)
            self.state = 193
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
        self.enterRule(localctx, 26, self.RULE_agentIdentity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(ai_environmentParser.T__14)
            self.state = 196
            self.match(ai_environmentParser.T__8)
            self.state = 197
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
        self.enterRule(localctx, 28, self.RULE_agentNamespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(ai_environmentParser.T__20)
            self.state = 200
            self.match(ai_environmentParser.T__8)
            self.state = 201
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
        self.enterRule(localctx, 30, self.RULE_agentLLMRefProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(ai_environmentParser.T__21)
            self.state = 204
            self.match(ai_environmentParser.T__8)
            self.state = 205
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
        self.enterRule(localctx, 32, self.RULE_agentToolRefProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(ai_environmentParser.T__22)
            self.state = 208
            self.match(ai_environmentParser.T__8)
            self.state = 209
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

        def ENTITY_ID(self):
            return self.getToken(ai_environmentParser.ENTITY_ID, 0)

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
        self.enterRule(localctx, 34, self.RULE_agentInputProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(ai_environmentParser.T__23)
            self.state = 212
            self.match(ai_environmentParser.T__8)
            self.state = 213
            self.match(ai_environmentParser.ENTITY_ID)
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

        def ENTITY_ID(self):
            return self.getToken(ai_environmentParser.ENTITY_ID, 0)

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
        self.enterRule(localctx, 36, self.RULE_agentOutputProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(ai_environmentParser.T__24)
            self.state = 216
            self.match(ai_environmentParser.T__8)
            self.state = 217
            self.match(ai_environmentParser.ENTITY_ID)
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
        self.enterRule(localctx, 38, self.RULE_agentCustomProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(ai_environmentParser.VAR)
            self.state = 220
            self.match(ai_environmentParser.T__8)
            self.state = 221
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
        self.enterRule(localctx, 40, self.RULE_llmDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(ai_environmentParser.T__25)
            self.state = 224
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 225
            self.match(ai_environmentParser.T__1)
            self.state = 226
            self.llmIdProp()
            self.state = 227
            self.llmProviderProp()
            self.state = 228
            self.llmModelProp()
            self.state = 229
            self.llmEndpointProp()
            self.state = 230
            self.llmVersionProp()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 231
                self.llmOtherProperty()
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 237
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
        self.enterRule(localctx, 42, self.RULE_llmIdProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ai_environmentParser.T__14)
            self.state = 240
            self.match(ai_environmentParser.T__8)
            self.state = 241
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
        self.enterRule(localctx, 44, self.RULE_llmProviderProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(ai_environmentParser.T__26)
            self.state = 244
            self.match(ai_environmentParser.T__8)
            self.state = 245
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
        self.enterRule(localctx, 46, self.RULE_llmModelProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(ai_environmentParser.T__27)
            self.state = 248
            self.match(ai_environmentParser.T__8)
            self.state = 249
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
        self.enterRule(localctx, 48, self.RULE_llmEndpointProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(ai_environmentParser.T__28)
            self.state = 252
            self.match(ai_environmentParser.T__8)
            self.state = 253
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
        self.enterRule(localctx, 50, self.RULE_llmVersionProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(ai_environmentParser.T__29)
            self.state = 256
            self.match(ai_environmentParser.T__8)
            self.state = 257
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
        self.enterRule(localctx, 52, self.RULE_llmOtherProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(ai_environmentParser.VAR)
            self.state = 260
            self.match(ai_environmentParser.T__8)
            self.state = 261
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


        def toolInputProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolInputPropertyContext,0)


        def toolOutputProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolOutputPropertyContext,0)


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
        self.enterRule(localctx, 54, self.RULE_toolDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(ai_environmentParser.T__30)
            self.state = 264
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 265
            self.match(ai_environmentParser.T__1)
            self.state = 266
            self.toolIdProp()
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 267
                self.toolInputProperty()


            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 270
                self.toolOutputProperty()


            self.state = 273
            self.toolEndpointProp()
            self.state = 274
            self.toolTypeProp()
            self.state = 275
            self.toolDescriptionProp()
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 276
                self.toolOtherProperty()
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 282
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
        self.enterRule(localctx, 56, self.RULE_toolIdProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(ai_environmentParser.T__14)
            self.state = 285
            self.match(ai_environmentParser.T__8)
            self.state = 286
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
        self.enterRule(localctx, 58, self.RULE_toolEndpointProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(ai_environmentParser.T__28)
            self.state = 289
            self.match(ai_environmentParser.T__8)
            self.state = 290
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

        def ENTITY_ID(self):
            return self.getToken(ai_environmentParser.ENTITY_ID, 0)

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
        self.enterRule(localctx, 60, self.RULE_toolInputProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(ai_environmentParser.T__23)
            self.state = 293
            self.match(ai_environmentParser.T__8)
            self.state = 294
            self.match(ai_environmentParser.ENTITY_ID)
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

        def ENTITY_ID(self):
            return self.getToken(ai_environmentParser.ENTITY_ID, 0)

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
        self.enterRule(localctx, 62, self.RULE_toolOutputProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(ai_environmentParser.T__24)
            self.state = 297
            self.match(ai_environmentParser.T__8)
            self.state = 298
            self.match(ai_environmentParser.ENTITY_ID)
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
        self.enterRule(localctx, 64, self.RULE_toolDescriptionProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ai_environmentParser.T__31)
            self.state = 301
            self.match(ai_environmentParser.T__8)
            self.state = 302
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
        self.enterRule(localctx, 66, self.RULE_toolTypeProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(ai_environmentParser.T__32)
            self.state = 305
            self.match(ai_environmentParser.T__8)
            self.state = 306
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
        self.enterRule(localctx, 68, self.RULE_toolOtherProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(ai_environmentParser.VAR)
            self.state = 309
            self.match(ai_environmentParser.T__8)
            self.state = 310
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





