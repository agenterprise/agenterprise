grammar ai_environment;

//// AI Environment Grammar 
///////////////////////
ai_envDef: 'ai_environment' PROPERTYVALUE '{' 
                    'architecture' '{'envId architectureServiceStack architectureAiStack architectureDataStack'}' 
                    'data' '{' entityDef* '}' 
                    'infrastructure' '{' llmDef* '}'  
                    'functional' '{' agentDef*  toolDef* '}' 
                    '}' 
                    ;

//environmentid
envId: 'envid' '=' PROPERTYVALUE ;
architectureServiceStack: 'service-techlayer' '=' TECHLAYER_AIURN; //service TECHLAYER
architectureAiStack: 'ai-techlayer' '=' TECHLAYER_AIURN; // AI TECHLAYERs
architectureDataStack: 'data-techlayer' '=' TECHLAYER_AIURN; // DATA TECHLAYERs


///////////
// Data
///////////
entityDef: 'entity' PROPERTYVALUE '{'
           entityIdProp
           entityElementProp*
       '}' ;

entityIdProp: 'uid' '=' ENTITY_ID ;
entityElementProp: 'element' '=' (ENTITY_VAR | ENTITY_CONSTANT) entityElementType entityElementDescription;
entityElementType:  '->' (ENTITY_TYPE | ENTITY_ID);
entityElementDescription: '#' PROPERTYVALUE;


/////////// 
// Agents
///////////
agentDef: 'agent' PROPERTYVALUE '{' agentIdentity agentNamespace agentSystemPromptProperty agentLLMRefProperty agentToolRefProperty* agentInputProperty? agentOutputProperty? agentCustomProperty* '}' ;

agentSystemPromptProperty: 'systemprompt' '=' PROPERTYVALUE ;
agentIdentity: 'uid' '=' AGENTID ;
agentNamespace: 'namespace' '=' AGENTNAMESPACE ;
agentLLMRefProperty: 'llmref' '=' LLMID ;
agentToolRefProperty: 'toolref' '=' TOOLID ;
agentInputProperty: 'in' '=' ENTITY_ID;
agentOutputProperty: 'out' '='  ENTITY_ID;

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
           toolInputProperty?
           toolOutputProperty?
           toolEndpointProp
           toolTypeProp
           toolDescriptionProp
           toolOtherProperty*
       '}' ;

toolIdProp: 'uid' '=' TOOLID ;
toolEndpointProp: 'endpoint' '=' PROPERTYVALUE ;
toolInputProperty: 'in' '=' ENTITY_ID;
toolOutputProperty: 'out' '='  ENTITY_ID;
toolDescriptionProp: 'description' '=' PROPERTYVALUE ;
toolTypeProp: 'type' '=' TOOL_TYPE ;
toolOtherProperty: VAR '=' PROPERTYVALUE  ;
/////// Lexer TOKENS ///////
TECHLAYER_RESSOURCE:  'github' | 'local';
TECHLAYER_AIURN: 'aiurn:techlayer:'TECHLAYER_RESSOURCE':'[a-zA-Z._][a-zA-Z_0-9.:-]* ;

// VARs
VAR: 'aiurn:global:var:'[a-zA-Z_][a-zA-Z0-9_]* ;


//Entity
ENTITY_ID: 'aiurn:entity:id:'[a-zA-Z_][a-zA-Z0-9_]*;
ENTITY_VAR: 'aiurn:entity:var:'[a-zA-Z_][a-zA-Z0-9_]*;
ENTITY_CONSTANT: 'aiurn:entity:constant:'[a-zA-Z_][a-zA-Z0-9_]*;
ENTITY_TYPE: ('TEXT' | 'NUMBER' | 'BOOL' | 'LIST' | 'DICT' | 'ANY');


//LLMs
LLMPROVIDER: 'aiurn:model:provider:azure' | 'aiurn:model:provider:openai' ;
LLMID: 'aiurn:model:id:'[a-zA-Z_][a-zA-Z_0-9:]* ;


//Tools
TOOLVAR: 'aiurn:tool:var:'[a-zA-Z_][a-zA-Z0-9_:]* ;
TOOLID: 'aiurn:tool:id:'[a-zA-Z_][a-zA-Z_0-9:]* ;
TOOL_TYPE: 'aiurn:tooltype:mcp' | 'aiurn:tooltype:openapi' | 'aiurn:tooltype:code' | 'aiurn:tooltype:ressource'  ;

//Agents
AGENTID: 'aiurn:agent:id:'[a-zA-Z_][a-zA-Z_0-9:]* ;
AGENTNAMESPACE: 'aiurn:ns:'[a-zA-Z_][a-zA-Z_0-9:]* ;
AGENTVAR: 'aiurn:agentvar:'[a-zA-Z_][a-zA-Z0-9_:]* ;


fragment FLOAT: [0-9]+ '.' [0-9]+ ;
fragment INT: [0-9]+ ;
fragment BOOL: 'True' | 'False' ;
fragment STRING: '"' (~["])* '"' ;
PROPERTYVALUE: FLOAT | INT | BOOL | STRING;
THINK: '...' (~["])* '...' ;
WS:     [ \t\r\n]+ -> skip;  // Whitespace
COMMENT: '//' ~[\r\n]* -> skip ; // Single line comment
ML_COMMENT: '/*' .*? '*/' -> skip ; // Multi line comment   