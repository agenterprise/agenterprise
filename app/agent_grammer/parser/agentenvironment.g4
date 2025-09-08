grammar agentenvironment;

import agent;


env: envDef* ;


envDef: 'agentenvironment' STRING '{' environmentProperty agentDef* '}' ;
environmentProperty: 'runtime' '=' KUBE|FLOWISE ;


KUBE: 'KUBE';
FLOWISE: 'FLOWISE';
STRING: '"' (~["])* '"';
ID: [a-zA-Z_][a-zA-Z0-9_]* ;
WS:     [ \t\r\n]+ -> skip;  // Weißraum ignorieren