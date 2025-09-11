grammar ai_llm;

llms: llmDef* ;

llmDef: 'llm' STRING '{'
           llmIdProp
           providerProp
           modelProp
           endpointProp
           versionProp
           otherLLMProperty*
       '}' ;

llmIdProp: 'uid' '=' LLMID ;
providerProp: 'provider' '=' LLMPROVIDER ;
modelProp: 'model' '=' STRING ;
endpointProp: 'endpoint' '=' STRING ;
versionProp: 'version' '=' STRING ;

// Für weitere optionale Properties
otherLLMProperty: VAR '=' STRING ;


