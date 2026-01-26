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
        4,1,55,341,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,5,0,99,8,0,10,0,12,0,102,9,0,1,0,1,0,1,0,1,0,5,0,108,
        8,0,10,0,12,0,111,9,0,1,0,1,0,1,0,1,0,5,0,117,8,0,10,0,12,0,120,
        9,0,1,0,5,0,123,8,0,10,0,12,0,126,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,5,6,155,8,6,10,6,12,6,158,9,6,1,6,1,6,1,7,1,7,
        3,7,164,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,186,8,12,10,12,12,12,
        189,9,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,3,13,204,8,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,
        1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,
        1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,
        1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,
        1,25,5,25,254,8,25,10,25,12,25,257,9,25,1,25,1,25,1,26,1,26,1,26,
        1,26,1,26,1,26,3,26,267,8,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,
        1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,
        1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,5,33,297,8,33,10,33,12,33,
        300,9,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,3,34,311,8,
        34,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,
        38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,41,1,
        41,1,41,1,41,1,41,0,0,42,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        74,76,78,80,82,0,2,1,0,40,41,2,0,39,39,42,42,328,0,84,1,0,0,0,2,
        130,1,0,0,0,4,134,1,0,0,0,6,138,1,0,0,0,8,142,1,0,0,0,10,146,1,0,
        0,0,12,150,1,0,0,0,14,163,1,0,0,0,16,165,1,0,0,0,18,169,1,0,0,0,
        20,175,1,0,0,0,22,178,1,0,0,0,24,181,1,0,0,0,26,203,1,0,0,0,28,205,
        1,0,0,0,30,209,1,0,0,0,32,213,1,0,0,0,34,217,1,0,0,0,36,221,1,0,
        0,0,38,225,1,0,0,0,40,229,1,0,0,0,42,233,1,0,0,0,44,237,1,0,0,0,
        46,241,1,0,0,0,48,245,1,0,0,0,50,249,1,0,0,0,52,266,1,0,0,0,54,268,
        1,0,0,0,56,272,1,0,0,0,58,276,1,0,0,0,60,280,1,0,0,0,62,284,1,0,
        0,0,64,288,1,0,0,0,66,292,1,0,0,0,68,310,1,0,0,0,70,312,1,0,0,0,
        72,316,1,0,0,0,74,320,1,0,0,0,76,324,1,0,0,0,78,328,1,0,0,0,80,332,
        1,0,0,0,82,336,1,0,0,0,84,85,5,1,0,0,85,86,5,51,0,0,86,87,5,2,0,
        0,87,88,5,3,0,0,88,89,5,2,0,0,89,90,3,2,1,0,90,91,3,4,2,0,91,92,
        3,6,3,0,92,93,3,8,4,0,93,94,3,10,5,0,94,95,5,4,0,0,95,96,5,5,0,0,
        96,100,5,2,0,0,97,99,3,12,6,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,
        1,0,0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,0,103,104,
        5,4,0,0,104,105,5,6,0,0,105,109,5,2,0,0,106,108,3,50,25,0,107,106,
        1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,112,
        1,0,0,0,111,109,1,0,0,0,112,113,5,4,0,0,113,114,5,7,0,0,114,118,
        5,2,0,0,115,117,3,24,12,0,116,115,1,0,0,0,117,120,1,0,0,0,118,116,
        1,0,0,0,118,119,1,0,0,0,119,124,1,0,0,0,120,118,1,0,0,0,121,123,
        3,66,33,0,122,121,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,
        1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,128,5,4,0,0,128,129,
        5,4,0,0,129,1,1,0,0,0,130,131,5,8,0,0,131,132,5,9,0,0,132,133,5,
        51,0,0,133,3,1,0,0,0,134,135,5,10,0,0,135,136,5,9,0,0,136,137,5,
        37,0,0,137,5,1,0,0,0,138,139,5,11,0,0,139,140,5,9,0,0,140,141,5,
        37,0,0,141,7,1,0,0,0,142,143,5,12,0,0,143,144,5,9,0,0,144,145,5,
        37,0,0,145,9,1,0,0,0,146,147,5,13,0,0,147,148,5,9,0,0,148,149,5,
        37,0,0,149,11,1,0,0,0,150,151,5,14,0,0,151,152,5,51,0,0,152,156,
        5,2,0,0,153,155,3,14,7,0,154,153,1,0,0,0,155,158,1,0,0,0,156,154,
        1,0,0,0,156,157,1,0,0,0,157,159,1,0,0,0,158,156,1,0,0,0,159,160,
        5,4,0,0,160,13,1,0,0,0,161,164,3,16,8,0,162,164,3,18,9,0,163,161,
        1,0,0,0,163,162,1,0,0,0,164,15,1,0,0,0,165,166,5,15,0,0,166,167,
        5,9,0,0,167,168,5,39,0,0,168,17,1,0,0,0,169,170,5,16,0,0,170,171,
        5,9,0,0,171,172,7,0,0,0,172,173,3,20,10,0,173,174,3,22,11,0,174,
        19,1,0,0,0,175,176,5,17,0,0,176,177,7,1,0,0,177,21,1,0,0,0,178,179,
        5,18,0,0,179,180,5,51,0,0,180,23,1,0,0,0,181,182,5,19,0,0,182,183,
        5,51,0,0,183,187,5,2,0,0,184,186,3,26,13,0,185,184,1,0,0,0,186,189,
        1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,187,
        1,0,0,0,190,191,5,4,0,0,191,25,1,0,0,0,192,204,3,28,14,0,193,204,
        3,30,15,0,194,204,3,32,16,0,195,204,3,34,17,0,196,204,3,36,18,0,
        197,204,3,38,19,0,198,204,3,40,20,0,199,204,3,42,21,0,200,204,3,
        44,22,0,201,204,3,46,23,0,202,204,3,48,24,0,203,192,1,0,0,0,203,
        193,1,0,0,0,203,194,1,0,0,0,203,195,1,0,0,0,203,196,1,0,0,0,203,
        197,1,0,0,0,203,198,1,0,0,0,203,199,1,0,0,0,203,200,1,0,0,0,203,
        201,1,0,0,0,203,202,1,0,0,0,204,27,1,0,0,0,205,206,5,20,0,0,206,
        207,5,9,0,0,207,208,5,51,0,0,208,29,1,0,0,0,209,210,5,15,0,0,210,
        211,5,9,0,0,211,212,5,48,0,0,212,31,1,0,0,0,213,214,5,21,0,0,214,
        215,5,9,0,0,215,216,5,49,0,0,216,33,1,0,0,0,217,218,5,22,0,0,218,
        219,5,9,0,0,219,220,5,44,0,0,220,35,1,0,0,0,221,222,5,23,0,0,222,
        223,5,9,0,0,223,224,5,46,0,0,224,37,1,0,0,0,225,226,5,24,0,0,226,
        227,5,9,0,0,227,228,5,39,0,0,228,39,1,0,0,0,229,230,5,25,0,0,230,
        231,5,9,0,0,231,232,5,39,0,0,232,41,1,0,0,0,233,234,5,26,0,0,234,
        235,5,9,0,0,235,236,5,51,0,0,236,43,1,0,0,0,237,238,5,27,0,0,238,
        239,5,9,0,0,239,240,5,51,0,0,240,45,1,0,0,0,241,242,5,28,0,0,242,
        243,5,9,0,0,243,244,5,51,0,0,244,47,1,0,0,0,245,246,5,38,0,0,246,
        247,5,9,0,0,247,248,5,51,0,0,248,49,1,0,0,0,249,250,5,29,0,0,250,
        251,5,51,0,0,251,255,5,2,0,0,252,254,3,52,26,0,253,252,1,0,0,0,254,
        257,1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,256,258,1,0,0,0,257,
        255,1,0,0,0,258,259,5,4,0,0,259,51,1,0,0,0,260,267,3,54,27,0,261,
        267,3,56,28,0,262,267,3,58,29,0,263,267,3,60,30,0,264,267,3,62,31,
        0,265,267,3,64,32,0,266,260,1,0,0,0,266,261,1,0,0,0,266,262,1,0,
        0,0,266,263,1,0,0,0,266,264,1,0,0,0,266,265,1,0,0,0,267,53,1,0,0,
        0,268,269,5,15,0,0,269,270,5,9,0,0,270,271,5,44,0,0,271,55,1,0,0,
        0,272,273,5,30,0,0,273,274,5,9,0,0,274,275,5,43,0,0,275,57,1,0,0,
        0,276,277,5,31,0,0,277,278,5,9,0,0,278,279,5,51,0,0,279,59,1,0,0,
        0,280,281,5,32,0,0,281,282,5,9,0,0,282,283,5,51,0,0,283,61,1,0,0,
        0,284,285,5,33,0,0,285,286,5,9,0,0,286,287,5,51,0,0,287,63,1,0,0,
        0,288,289,5,38,0,0,289,290,5,9,0,0,290,291,5,51,0,0,291,65,1,0,0,
        0,292,293,5,34,0,0,293,294,5,51,0,0,294,298,5,2,0,0,295,297,3,68,
        34,0,296,295,1,0,0,0,297,300,1,0,0,0,298,296,1,0,0,0,298,299,1,0,
        0,0,299,301,1,0,0,0,300,298,1,0,0,0,301,302,5,4,0,0,302,67,1,0,0,
        0,303,311,3,70,35,0,304,311,3,74,37,0,305,311,3,76,38,0,306,311,
        3,72,36,0,307,311,3,80,40,0,308,311,3,78,39,0,309,311,3,82,41,0,
        310,303,1,0,0,0,310,304,1,0,0,0,310,305,1,0,0,0,310,306,1,0,0,0,
        310,307,1,0,0,0,310,308,1,0,0,0,310,309,1,0,0,0,311,69,1,0,0,0,312,
        313,5,15,0,0,313,314,5,9,0,0,314,315,5,46,0,0,315,71,1,0,0,0,316,
        317,5,32,0,0,317,318,5,9,0,0,318,319,5,51,0,0,319,73,1,0,0,0,320,
        321,5,24,0,0,321,322,5,9,0,0,322,323,5,39,0,0,323,75,1,0,0,0,324,
        325,5,25,0,0,325,326,5,9,0,0,326,327,5,39,0,0,327,77,1,0,0,0,328,
        329,5,26,0,0,329,330,5,9,0,0,330,331,5,51,0,0,331,79,1,0,0,0,332,
        333,5,35,0,0,333,334,5,9,0,0,334,335,5,47,0,0,335,81,1,0,0,0,336,
        337,5,38,0,0,337,338,5,9,0,0,338,339,5,51,0,0,339,83,1,0,0,0,12,
        100,109,118,124,156,163,187,203,255,266,298,310
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
                     "'in'", "'out'", "'description'", "'example'", "'tag'", 
                     "'llm'", "'provider'", "'model'", "'endpoint'", "'version'", 
                     "'tool'", "'type'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TECHLAYER_RESSOURCE", "TECHLAYER_AIURN", "VAR", "ENTITY_ID", 
                      "ENTITY_VAR", "ENTITY_CONSTANT", "ENTITY_TYPE", "LLMPROVIDER", 
                      "LLMID", "TOOLVAR", "TOOLID", "TOOL_TYPE", "AGENTID", 
                      "AGENTNAMESPACE", "AGENTVAR", "PROPERTYVALUE", "THINK", 
                      "WS", "COMMENT", "ML_COMMENT" ]

    RULE_ai_envDef = 0
    RULE_envId = 1
    RULE_architectureServiceStack = 2
    RULE_architectureAiStack = 3
    RULE_architectureDataStack = 4
    RULE_architectureAgenticMiddlewareStack = 5
    RULE_entityDef = 6
    RULE_entityProp = 7
    RULE_entityIdProp = 8
    RULE_entityElementProp = 9
    RULE_entityElementType = 10
    RULE_entityElementDescription = 11
    RULE_agentDef = 12
    RULE_agentProperty = 13
    RULE_agentSystemPromptProperty = 14
    RULE_agentIdentity = 15
    RULE_agentNamespace = 16
    RULE_agentLLMRefProperty = 17
    RULE_agentToolRefProperty = 18
    RULE_agentInputProperty = 19
    RULE_agentOutputProperty = 20
    RULE_agentDescriptionProp = 21
    RULE_agentExampleProp = 22
    RULE_agentTagsProp = 23
    RULE_agentCustomProperty = 24
    RULE_llmDef = 25
    RULE_llmProp = 26
    RULE_llmIdProp = 27
    RULE_llmProviderProp = 28
    RULE_llmModelProp = 29
    RULE_llmEndpointProp = 30
    RULE_llmVersionProp = 31
    RULE_llmOtherProperty = 32
    RULE_toolDef = 33
    RULE_toolProp = 34
    RULE_toolIdProp = 35
    RULE_toolEndpointProp = 36
    RULE_toolInputProperty = 37
    RULE_toolOutputProperty = 38
    RULE_toolDescriptionProp = 39
    RULE_toolTypeProp = 40
    RULE_toolOtherProperty = 41

    ruleNames =  [ "ai_envDef", "envId", "architectureServiceStack", "architectureAiStack", 
                   "architectureDataStack", "architectureAgenticMiddlewareStack", 
                   "entityDef", "entityProp", "entityIdProp", "entityElementProp", 
                   "entityElementType", "entityElementDescription", "agentDef", 
                   "agentProperty", "agentSystemPromptProperty", "agentIdentity", 
                   "agentNamespace", "agentLLMRefProperty", "agentToolRefProperty", 
                   "agentInputProperty", "agentOutputProperty", "agentDescriptionProp", 
                   "agentExampleProp", "agentTagsProp", "agentCustomProperty", 
                   "llmDef", "llmProp", "llmIdProp", "llmProviderProp", 
                   "llmModelProp", "llmEndpointProp", "llmVersionProp", 
                   "llmOtherProperty", "toolDef", "toolProp", "toolIdProp", 
                   "toolEndpointProp", "toolInputProperty", "toolOutputProperty", 
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
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    TECHLAYER_RESSOURCE=36
    TECHLAYER_AIURN=37
    VAR=38
    ENTITY_ID=39
    ENTITY_VAR=40
    ENTITY_CONSTANT=41
    ENTITY_TYPE=42
    LLMPROVIDER=43
    LLMID=44
    TOOLVAR=45
    TOOLID=46
    TOOL_TYPE=47
    AGENTID=48
    AGENTNAMESPACE=49
    AGENTVAR=50
    PROPERTYVALUE=51
    THINK=52
    WS=53
    COMMENT=54
    ML_COMMENT=55

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
            self.state = 84
            self.match(ai_environmentParser.T__0)
            self.state = 85
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 86
            self.match(ai_environmentParser.T__1)
            self.state = 87
            self.match(ai_environmentParser.T__2)
            self.state = 88
            self.match(ai_environmentParser.T__1)
            self.state = 89
            self.envId()
            self.state = 90
            self.architectureServiceStack()
            self.state = 91
            self.architectureAiStack()
            self.state = 92
            self.architectureDataStack()
            self.state = 93
            self.architectureAgenticMiddlewareStack()
            self.state = 94
            self.match(ai_environmentParser.T__3)
            self.state = 95
            self.match(ai_environmentParser.T__4)
            self.state = 96
            self.match(ai_environmentParser.T__1)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 97
                self.entityDef()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(ai_environmentParser.T__3)
            self.state = 104
            self.match(ai_environmentParser.T__5)
            self.state = 105
            self.match(ai_environmentParser.T__1)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 106
                self.llmDef()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
            self.match(ai_environmentParser.T__3)
            self.state = 113
            self.match(ai_environmentParser.T__6)
            self.state = 114
            self.match(ai_environmentParser.T__1)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 115
                self.agentDef()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 121
                self.toolDef()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(ai_environmentParser.T__3)
            self.state = 128
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
            self.state = 130
            self.match(ai_environmentParser.T__7)
            self.state = 131
            self.match(ai_environmentParser.T__8)
            self.state = 132
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
            self.state = 134
            self.match(ai_environmentParser.T__9)
            self.state = 135
            self.match(ai_environmentParser.T__8)
            self.state = 136
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
            self.state = 138
            self.match(ai_environmentParser.T__10)
            self.state = 139
            self.match(ai_environmentParser.T__8)
            self.state = 140
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
            self.state = 142
            self.match(ai_environmentParser.T__11)
            self.state = 143
            self.match(ai_environmentParser.T__8)
            self.state = 144
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
            self.state = 146
            self.match(ai_environmentParser.T__12)
            self.state = 147
            self.match(ai_environmentParser.T__8)
            self.state = 148
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

        def entityProp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.EntityPropContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.EntityPropContext,i)


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
            self.state = 150
            self.match(ai_environmentParser.T__13)
            self.state = 151
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 152
            self.match(ai_environmentParser.T__1)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 153
                self.entityProp()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
            self.match(ai_environmentParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entityIdProp(self):
            return self.getTypedRuleContext(ai_environmentParser.EntityIdPropContext,0)


        def entityElementProp(self):
            return self.getTypedRuleContext(ai_environmentParser.EntityElementPropContext,0)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_entityProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityProp" ):
                listener.enterEntityProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityProp" ):
                listener.exitEntityProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntityProp" ):
                return visitor.visitEntityProp(self)
            else:
                return visitor.visitChildren(self)




    def entityProp(self):

        localctx = ai_environmentParser.EntityPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_entityProp)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.entityIdProp()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.entityElementProp()
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
        self.enterRule(localctx, 16, self.RULE_entityIdProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(ai_environmentParser.T__14)
            self.state = 166
            self.match(ai_environmentParser.T__8)
            self.state = 167
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
        self.enterRule(localctx, 18, self.RULE_entityElementProp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(ai_environmentParser.T__15)
            self.state = 170
            self.match(ai_environmentParser.T__8)
            self.state = 171
            _la = self._input.LA(1)
            if not(_la==40 or _la==41):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 172
            self.entityElementType()
            self.state = 173
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
        self.enterRule(localctx, 20, self.RULE_entityElementType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(ai_environmentParser.T__16)
            self.state = 176
            _la = self._input.LA(1)
            if not(_la==39 or _la==42):
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
        self.enterRule(localctx, 22, self.RULE_entityElementDescription)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(ai_environmentParser.T__17)
            self.state = 179
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

        def agentProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.AgentPropertyContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.AgentPropertyContext,i)


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
            self.state = 181
            self.match(ai_environmentParser.T__18)
            self.state = 182
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 183
            self.match(ai_environmentParser.T__1)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 275413762048) != 0):
                self.state = 184
                self.agentProperty()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 190
            self.match(ai_environmentParser.T__3)
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

        def agentSystemPromptProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentSystemPromptPropertyContext,0)


        def agentIdentity(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentIdentityContext,0)


        def agentNamespace(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentNamespaceContext,0)


        def agentLLMRefProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentLLMRefPropertyContext,0)


        def agentToolRefProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentToolRefPropertyContext,0)


        def agentInputProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentInputPropertyContext,0)


        def agentOutputProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentOutputPropertyContext,0)


        def agentDescriptionProp(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentDescriptionPropContext,0)


        def agentExampleProp(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentExamplePropContext,0)


        def agentTagsProp(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentTagsPropContext,0)


        def agentCustomProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.AgentCustomPropertyContext,0)


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
        self.enterRule(localctx, 26, self.RULE_agentProperty)
        try:
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.agentSystemPromptProperty()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.agentIdentity()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.agentNamespace()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.agentLLMRefProperty()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 5)
                self.state = 196
                self.agentToolRefProperty()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 6)
                self.state = 197
                self.agentInputProperty()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 7)
                self.state = 198
                self.agentOutputProperty()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 8)
                self.state = 199
                self.agentDescriptionProp()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 9)
                self.state = 200
                self.agentExampleProp()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 10)
                self.state = 201
                self.agentTagsProp()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 11)
                self.state = 202
                self.agentCustomProperty()
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
        self.enterRule(localctx, 28, self.RULE_agentSystemPromptProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(ai_environmentParser.T__19)
            self.state = 206
            self.match(ai_environmentParser.T__8)
            self.state = 207
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
        self.enterRule(localctx, 30, self.RULE_agentIdentity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(ai_environmentParser.T__14)
            self.state = 210
            self.match(ai_environmentParser.T__8)
            self.state = 211
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
            self.state = 213
            self.match(ai_environmentParser.T__20)
            self.state = 214
            self.match(ai_environmentParser.T__8)
            self.state = 215
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
        self.enterRule(localctx, 34, self.RULE_agentLLMRefProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(ai_environmentParser.T__21)
            self.state = 218
            self.match(ai_environmentParser.T__8)
            self.state = 219
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
        self.enterRule(localctx, 36, self.RULE_agentToolRefProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(ai_environmentParser.T__22)
            self.state = 222
            self.match(ai_environmentParser.T__8)
            self.state = 223
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
        self.enterRule(localctx, 38, self.RULE_agentInputProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(ai_environmentParser.T__23)
            self.state = 226
            self.match(ai_environmentParser.T__8)
            self.state = 227
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
        self.enterRule(localctx, 40, self.RULE_agentOutputProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(ai_environmentParser.T__24)
            self.state = 230
            self.match(ai_environmentParser.T__8)
            self.state = 231
            self.match(ai_environmentParser.ENTITY_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentDescriptionPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentDescriptionProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentDescriptionProp" ):
                listener.enterAgentDescriptionProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentDescriptionProp" ):
                listener.exitAgentDescriptionProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentDescriptionProp" ):
                return visitor.visitAgentDescriptionProp(self)
            else:
                return visitor.visitChildren(self)




    def agentDescriptionProp(self):

        localctx = ai_environmentParser.AgentDescriptionPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_agentDescriptionProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(ai_environmentParser.T__25)
            self.state = 234
            self.match(ai_environmentParser.T__8)
            self.state = 235
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentExamplePropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentExampleProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentExampleProp" ):
                listener.enterAgentExampleProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentExampleProp" ):
                listener.exitAgentExampleProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentExampleProp" ):
                return visitor.visitAgentExampleProp(self)
            else:
                return visitor.visitChildren(self)




    def agentExampleProp(self):

        localctx = ai_environmentParser.AgentExamplePropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_agentExampleProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(ai_environmentParser.T__26)
            self.state = 238
            self.match(ai_environmentParser.T__8)
            self.state = 239
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentTagsPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def getRuleIndex(self):
            return ai_environmentParser.RULE_agentTagsProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentTagsProp" ):
                listener.enterAgentTagsProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentTagsProp" ):
                listener.exitAgentTagsProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgentTagsProp" ):
                return visitor.visitAgentTagsProp(self)
            else:
                return visitor.visitChildren(self)




    def agentTagsProp(self):

        localctx = ai_environmentParser.AgentTagsPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_agentTagsProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ai_environmentParser.T__27)
            self.state = 242
            self.match(ai_environmentParser.T__8)
            self.state = 243
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
        self.enterRule(localctx, 48, self.RULE_agentCustomProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(ai_environmentParser.VAR)
            self.state = 246
            self.match(ai_environmentParser.T__8)
            self.state = 247
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

        def llmProp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.LlmPropContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.LlmPropContext,i)


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
        self.enterRule(localctx, 50, self.RULE_llmDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(ai_environmentParser.T__28)
            self.state = 250
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 251
            self.match(ai_environmentParser.T__1)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 290984067072) != 0):
                self.state = 252
                self.llmProp()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 258
            self.match(ai_environmentParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlmPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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


        def llmOtherProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.LlmOtherPropertyContext,0)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_llmProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlmProp" ):
                listener.enterLlmProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlmProp" ):
                listener.exitLlmProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlmProp" ):
                return visitor.visitLlmProp(self)
            else:
                return visitor.visitChildren(self)




    def llmProp(self):

        localctx = ai_environmentParser.LlmPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_llmProp)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.llmIdProp()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.llmProviderProp()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                self.llmModelProp()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 263
                self.llmEndpointProp()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 264
                self.llmVersionProp()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 6)
                self.state = 265
                self.llmOtherProperty()
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
        self.enterRule(localctx, 54, self.RULE_llmIdProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(ai_environmentParser.T__14)
            self.state = 269
            self.match(ai_environmentParser.T__8)
            self.state = 270
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
        self.enterRule(localctx, 56, self.RULE_llmProviderProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ai_environmentParser.T__29)
            self.state = 273
            self.match(ai_environmentParser.T__8)
            self.state = 274
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
        self.enterRule(localctx, 58, self.RULE_llmModelProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(ai_environmentParser.T__30)
            self.state = 277
            self.match(ai_environmentParser.T__8)
            self.state = 278
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
        self.enterRule(localctx, 60, self.RULE_llmEndpointProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(ai_environmentParser.T__31)
            self.state = 281
            self.match(ai_environmentParser.T__8)
            self.state = 282
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
        self.enterRule(localctx, 62, self.RULE_llmVersionProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(ai_environmentParser.T__32)
            self.state = 285
            self.match(ai_environmentParser.T__8)
            self.state = 286
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
        self.enterRule(localctx, 64, self.RULE_llmOtherProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(ai_environmentParser.VAR)
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


    class ToolDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTYVALUE(self):
            return self.getToken(ai_environmentParser.PROPERTYVALUE, 0)

        def toolProp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ai_environmentParser.ToolPropContext)
            else:
                return self.getTypedRuleContext(ai_environmentParser.ToolPropContext,i)


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
        self.enterRule(localctx, 66, self.RULE_toolDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(ai_environmentParser.T__33)
            self.state = 293
            self.match(ai_environmentParser.PROPERTYVALUE)
            self.state = 294
            self.match(ai_environmentParser.T__1)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 313650085888) != 0):
                self.state = 295
                self.toolProp()
                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 301
            self.match(ai_environmentParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToolPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def toolIdProp(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolIdPropContext,0)


        def toolInputProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolInputPropertyContext,0)


        def toolOutputProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolOutputPropertyContext,0)


        def toolEndpointProp(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolEndpointPropContext,0)


        def toolTypeProp(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolTypePropContext,0)


        def toolDescriptionProp(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolDescriptionPropContext,0)


        def toolOtherProperty(self):
            return self.getTypedRuleContext(ai_environmentParser.ToolOtherPropertyContext,0)


        def getRuleIndex(self):
            return ai_environmentParser.RULE_toolProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToolProp" ):
                listener.enterToolProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToolProp" ):
                listener.exitToolProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToolProp" ):
                return visitor.visitToolProp(self)
            else:
                return visitor.visitChildren(self)




    def toolProp(self):

        localctx = ai_environmentParser.ToolPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_toolProp)
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.toolIdProp()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.toolInputProperty()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 305
                self.toolOutputProperty()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 306
                self.toolEndpointProp()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 5)
                self.state = 307
                self.toolTypeProp()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 6)
                self.state = 308
                self.toolDescriptionProp()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 7)
                self.state = 309
                self.toolOtherProperty()
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
        self.enterRule(localctx, 70, self.RULE_toolIdProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(ai_environmentParser.T__14)
            self.state = 313
            self.match(ai_environmentParser.T__8)
            self.state = 314
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
        self.enterRule(localctx, 72, self.RULE_toolEndpointProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(ai_environmentParser.T__31)
            self.state = 317
            self.match(ai_environmentParser.T__8)
            self.state = 318
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
        self.enterRule(localctx, 74, self.RULE_toolInputProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(ai_environmentParser.T__23)
            self.state = 321
            self.match(ai_environmentParser.T__8)
            self.state = 322
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
        self.enterRule(localctx, 76, self.RULE_toolOutputProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(ai_environmentParser.T__24)
            self.state = 325
            self.match(ai_environmentParser.T__8)
            self.state = 326
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
        self.enterRule(localctx, 78, self.RULE_toolDescriptionProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(ai_environmentParser.T__25)
            self.state = 329
            self.match(ai_environmentParser.T__8)
            self.state = 330
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
        self.enterRule(localctx, 80, self.RULE_toolTypeProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(ai_environmentParser.T__34)
            self.state = 333
            self.match(ai_environmentParser.T__8)
            self.state = 334
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
        self.enterRule(localctx, 82, self.RULE_toolOtherProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(ai_environmentParser.VAR)
            self.state = 337
            self.match(ai_environmentParser.T__8)
            self.state = 338
            self.match(ai_environmentParser.PROPERTYVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





