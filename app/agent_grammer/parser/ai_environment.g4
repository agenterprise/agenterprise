grammar ai_environment;

import ai_llm, ai_agent;



ai_envDef: 'ai_environment' STRING '@nonfunctional' '{'envid deploymentPattern techstack '}' '@functional' '{' agentDef* llmDef* '}' ;

//environmentid
envid: 'envid' '=' STRING ;
//deploymentpattern
deploymentPattern: 'deployment' '=' DEPLOYMENT ;
DEPLOYMENT: DEPLOYMENT_MICROSERVICE | DEPLOYMENT_SWARM | DEPLOYMENT_MCPSERVICE ;
DEPLOYMENT_MICROSERVICE: 'aiurn:deployment:microservice';
DEPLOYMENT_SWARM: 'aiurn:deployment:swarm';
DEPLOYMENT_MCPSERVICE: 'aiurn:deployment:mcpservice';

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