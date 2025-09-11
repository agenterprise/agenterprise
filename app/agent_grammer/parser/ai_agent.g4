grammar ai_agent;

import ai_llm; // Importiere die LLM-Grammatik

prog: agentDef* ;

agentDef: 'agent' STRING '{' agentIdentity agentNamespace systemPromptProperty llmRefProperty otherAgentProperty* '}' ;

systemPromptProperty: 'systemprompt' '=' STRING ;
agentIdentity: 'uid' '=' AGENTID ;
agentNamespace: 'namespace' '=' NAMESPACE ;

// Neue Property für die Referenz auf ein LLM
llmRefProperty: 'llmref' '=' LLMID ;

otherAgentProperty: agentProperty ;

agentProperty: VAR '=' STRING ;


