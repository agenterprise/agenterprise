grammar agent;

prog: agentDef* ;

agentDef: 'agent' STRING '{' agentIdentity agentNamespace systemPromptProperty otherAgentProperty* '}' ;
systemPromptProperty: 'systemprompt' '=' STRING ;
agentIdentity: 'uid' '=' ID ;
agentNamespace: 'namespace' '=' ID ;
otherAgentProperty: agentProperty ;

agentProperty: 'systemprompt' '=' STRING
            | ID '=' STRING
            | 'prompt' '=' STRING
            ;

STRING: '"' (~["])* '"' ;
ID: '"' [a-zA-Z_][a-zA-Z0-9_]* '"' ;
WS:     [ \t\r\n]+ -> skip;  // Weißraum ignorieren