grammar ai_llm;

llmSet: llmDef* ;

llmDef: 'llm' STRING '{'
           llmIdProp
           llmProviderProp
           llmModelProp
           llmEndpointProp
           llmVersionProp
           llmOtherProperty*
       '}' ;

llmIdProp: 'uid' '=' LLMID ;
llmProviderProp: 'provider' '=' LLMPROVIDER ;
llmModelProp: 'model' '=' STRING ;
llmEndpointProp: 'endpoint' '=' STRING ;
llmVersionProp: 'version' '=' STRING ;

// Für weitere optionale Properties
llmOtherProperty: VAR '=' STRING ;


