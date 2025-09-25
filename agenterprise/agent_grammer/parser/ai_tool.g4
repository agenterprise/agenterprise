grammar ai_tool;

toolSet: toolDef* ;

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

// Für weitere optionale Properties
toolOtherProperty: VAR '=' STRING ;


