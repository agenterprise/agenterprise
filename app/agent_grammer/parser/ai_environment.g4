grammar ai_environment;

import ai_llm, ai_agent;



ai_envDef: 'ai_environment' STRING 'architecture' '{'envid appPattern techstack '}' 'infrastructure' '{' llmDef* '}'  'functional' '{' agentDef* '}' ;

//environmentid
envid: 'envid' '=' STRING ;
//appPattern
appPattern: 'app-pattern' '=' APP ;
APP: APP_MICROSERVICE | APP_SWARM | APP_MCPSERVICE ;
APP_MICROSERVICE: 'aiurn:app:microservice';
APP_SWARM: 'aiurn:app:swarm';
APP_MCPSERVICE: 'aiurn:app:mcpservice';

// Techstacks
techstack: 'techstack' '=' TECHSTACK_AIURN ;
TECHSTACK_CATEGORY: 'enterprise' | 'basic' ;
TECHSTACK_AIURN: 'aiurn:techstack:'TECHSTACK_CATEGORY':'[a-zA-Z_][a-zA-Z_0-9:]* ;


// URNs
VAR: 'aiurn:var:'[a-zA-Z_][a-zA-Z0-9_]* ;
LLMPROVIDER: 'aiurn:provider:azure' | 'aiurn:provider:openai' ;
LLMID: 'aiurn:model:llm:'[a-zA-Z_][a-zA-Z_0-9:]* ;
AGENTID: 'aiurn:agent:'[a-zA-Z_][a-zA-Z_0-9:]* ;
NAMESPACE: 'aiurn:ns:'[a-zA-Z_][a-zA-Z_0-9:]* ;



STRING: '"' (~["])* '"' ;
WS:     [ \t\r\n]+ -> skip;  // Weißraum ignorieren