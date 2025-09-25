grammar ai_environment;

//// AI Environment Grammar 
///////////////////////
ai_envDef: 'ai_environment' STRING '{' 
                    'architecture' '{'envId architectureServiceStack architectureAiStack '}' 
                    'infrastructure' '{' llmDef* '}'  
                    'functional' '{' agentDef*  toolDef* '}' 
                    '}' 
                    ;

//environmentid
envId: 'envid' '=' STRING ;
architectureServiceStack: 'service-techlayer' '=' TECHLAYER_AIURN; //service TECHLAYER
architectureAiStack: 'ai-techlayer' '=' TECHLAYER_AIURN; // AI TECHLAYERs


/////////// 
// Agents
///////////
agentDef: 'agent' STRING '{' agentIdentity agentNamespace agentSystemPromptProperty agentLLMRefProperty agentToolRefProperty* agentCustomProperty* '}' ;

agentSystemPromptProperty: 'systemprompt' '=' STRING ;
agentIdentity: 'uid' '=' AGENTID ;
agentNamespace: 'namespace' '=' AGENTNAMESPACE ;
agentLLMRefProperty: 'llmref' '=' LLMID ;
agentToolRefProperty: 'toolref' '=' TOOLID ;
agentCustomProperty: VAR '=' STRING  ;

///////////
// LLMs
///////////
llmDef: 'llm' STRING '{'
           llmIdProp
           llmProviderProp
           llmModelProp
           llmEndpointProp
           llmVersionProp
           llmOtherProperty*
       '}' ;

llmIdProp: 'uid' '=' LLMID ;
llmProviderProp: 'provider' '=' LLMPROVIDER ;
llmModelProp: 'model' '=' STRING ;
llmEndpointProp: 'endpoint' '=' STRING ;
llmVersionProp: 'version' '=' STRING ;
llmOtherProperty: VAR '=' STRING ;

///////////
// Tools
///////////
toolDef: 'tool' STRING '{'
           toolIdProp
           toolEndpointProp
           toolTypeProp
           toolDescription
           toolOtherProperty*
       '}' ;

toolIdProp: 'uid' '=' TOOLID ;
toolEndpointProp: 'endpoint' '=' STRING ;
toolDescription: 'description' '=' STRING ;
toolTypeProp: 'type' '=' TOOL_TYPE ;
toolOtherProperty: VAR '=' STRING ;

/////// Lexer TOKENS ///////
TECHLAYER_RESSOURCE:  'github' | 'zip' | 'file' ;
TECHLAYER_AIURN: 'aiurn:techlayer:'TECHLAYER_RESSOURCE':'[a-zA-Z_][a-zA-Z_0-9.:-]* ;

// URNs
VAR: 'aiurn:var:'[a-zA-Z_][a-zA-Z0-9_]* ;

//LLMs
LLMPROVIDER: 'aiurn:provider:azure' | 'aiurn:provider:openai' ;
LLMID: 'aiurn:model:llm:'[a-zA-Z_][a-zA-Z_0-9:]* ;

//Tools
TOOLID: 'aiurn:tool:'[a-zA-Z_][a-zA-Z_0-9:]* ;
TOOL_TYPE: 'aiurn:tooltype:mcp' | 'aiurn:tooltype:openapi' | 'aiurn:tooltype:code' ;

//Agents
AGENTID: 'aiurn:agent:'[a-zA-Z_][a-zA-Z_0-9:]* ;
AGENTNAMESPACE: 'aiurn:ns:'[a-zA-Z_][a-zA-Z_0-9:]* ;



STRING: '"' (~["])* '"' ;
WS:     [ \t\r\n]+ -> skip;  // Weißraum ignorieren