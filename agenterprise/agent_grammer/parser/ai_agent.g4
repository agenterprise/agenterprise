grammar ai_agent;

import ai_llm; // Importiere die LLM-Grammatik

prog: agentDef* ;

agentDef: 'agent' STRING '{' agentIdentity agentNamespace systemPromptProperty llmRefProperty toolRefProperty* otherAgentProperty* '}' ;

systemPromptProperty: 'systemprompt' '=' STRING ;
agentIdentity: 'uid' '=' AGENTID ;
agentNamespace: 'namespace' '=' AGENTNAMESPACE ;

// Neue Property für die Referenz auf ein LLM
llmRefProperty: 'llmref' '=' LLMID ;

toolRefProperty: 'toolref' '=' TOOLID ;

otherAgentProperty: agentProperty ;

agentProperty: VAR '=' STRING ;


