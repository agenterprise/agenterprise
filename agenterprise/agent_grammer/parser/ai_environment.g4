grammar ai_environment;

//// AI Environment Grammar 
///////////////////////
ai_envDef: 'ai_environment' PROPERTYVALUE '{' 
                    'architecture' '{'envId architectureServiceStack architectureAiStack '}' 
                    'infrastructure' '{' llmDef* '}'  
                    'functional' '{' agentDef*  toolDef* '}' 
                    '}' 
                    ;

//environmentid
envId: 'envid' '=' PROPERTYVALUE ;
architectureServiceStack: 'service-techlayer' '=' TECHLAYER_AIURN; //service TECHLAYER
architectureAiStack: 'ai-techlayer' '=' TECHLAYER_AIURN; // AI TECHLAYERs


/////////// 
// Agents
///////////
agentDef: 'agent' PROPERTYVALUE '{' agentIdentity agentNamespace agentSystemPromptProperty agentLLMRefProperty agentToolRefProperty* agentCustomProperty* '}' ;

agentSystemPromptProperty: 'systemprompt' '=' PROPERTYVALUE ;
agentIdentity: 'uid' '=' AGENTID ;
agentNamespace: 'namespace' '=' AGENTNAMESPACE ;
agentLLMRefProperty: 'llmref' '=' LLMID ;
agentToolRefProperty: 'toolref' '=' TOOLID ;
agentCustomProperty: VAR '=' PROPERTYVALUE   ;

///////////
// LLMs
///////////
llmDef: 'llm' PROPERTYVALUE '{'
           llmIdProp
           llmProviderProp
           llmModelProp
           llmEndpointProp
           llmVersionProp
           llmOtherProperty*
       '}' ;

llmIdProp: 'uid' '=' LLMID ;
llmProviderProp: 'provider' '=' LLMPROVIDER ;
llmModelProp: 'model' '=' PROPERTYVALUE ;
llmEndpointProp: 'endpoint' '=' PROPERTYVALUE ;
llmVersionProp: 'version' '=' PROPERTYVALUE ;
llmOtherProperty: VAR '=' PROPERTYVALUE; 

///////////
// Tools
///////////
toolDef: 'tool' PROPERTYVALUE '{'
           toolIdProp
           toolEndpointProp
           toolTypeProp
           toolDescriptionProp
           toolOtherProperty*
       '}' ;

toolIdProp: 'uid' '=' TOOLID ;
toolEndpointProp: 'endpoint' '=' PROPERTYVALUE ;
toolDescriptionProp: 'description' '=' PROPERTYVALUE ;
toolTypeProp: 'type' '=' TOOL_TYPE ;
toolOtherProperty: VAR '=' PROPERTYVALUE  ;

/////// Lexer TOKENS ///////
TECHLAYER_RESSOURCE:  'github' | 'local';
TECHLAYER_AIURN: 'aiurn:techlayer:'TECHLAYER_RESSOURCE':'[a-zA-Z._][a-zA-Z_0-9.:-]* ;

// URNs
VAR: 'aiurn:var:'[a-zA-Z_][a-zA-Z0-9_]* ;

//LLMs
LLMPROVIDER: 'aiurn:model:provider:azure' | 'aiurn:model:provider:openai' ;
//LLMPRODUCT: 'aiurn:model:product:azure' | 'aiurn:provider:openai' ;

LLMID: 'aiurn:model:id:'[a-zA-Z_][a-zA-Z_0-9:]* ;

//Tools
TOOLID: 'aiurn:tool:'[a-zA-Z_][a-zA-Z_0-9:]* ;
TOOL_TYPE: 'aiurn:tooltype:mcp' | 'aiurn:tooltype:openapi' | 'aiurn:tooltype:code' | 'aiurn:tooltype:ressource'  ;

//Agents
AGENTID: 'aiurn:agent:'[a-zA-Z_][a-zA-Z_0-9:]* ;
AGENTNAMESPACE: 'aiurn:ns:'[a-zA-Z_][a-zA-Z_0-9:]* ;

fragment FLOAT: [0-9]+ '.' [0-9]+ ;
fragment INT: [0-9]+ ;
fragment BOOL: 'True' | 'False' ;
fragment STRING: '"' (~["])* '"' ;
PROPERTYVALUE: FLOAT | INT | BOOL | STRING;

WS:     [ \t\r\n]+ -> skip;  // Weißraum ignorieren