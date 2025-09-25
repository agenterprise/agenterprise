grammar ai_environment;

import ai_llm, ai_agent, ai_tool;



ai_envDef: 'ai_environment' STRING 'architecture' '{'envid serviceStack aiStack '}' 'infrastructure' '{' llmDef* '}'  'functional' '{' agentDef*  toolDef* '}' ;

//environmentid
envid: 'envid' '=' STRING ;

//service
serviceStack: 'service-techstack' '=' TECHSTACK_AIURN ;
// AI Techstacks
aiStack: 'ai-techstack' '=' TECHSTACK_AIURN ;
TECHSTACK_RESSOURCE:  'github' | 'zip' | 'file' ;
TECHSTACK_AIURN: 'aiurn:techstack:'TECHSTACK_RESSOURCE':'[a-zA-Z_][a-zA-Z_0-9.:-]* ;


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