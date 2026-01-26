---
hide:
  - toc
---
# Infrastructure Layer

## LLM (Large Language Model)
Example:
```dsl
infrastructure {
   llm "My LLM" {
        uid = aiurn:model:id:geepeetee
        provider = aiurn:model:provider:azure 
        model = "gpt-4o"
        endpoint = "https://any.openai.azure.com/"
        version = "2025-01-01-preview"
        aiurn:global:var:temperature = 0.7
        aiurn:global:var:costid = "ewe3949" 
        aiurn:global:var:hello = True 
    }
}
```
### Specs
Give the LLM a name by assign a name to tool %MY_NAME% { ... }

| Attribute | Assignment | Rule  | Cardinality  | Examples |
| --------  | --------   | -------- | -------- | -------- |
| uid       | aiurn:model:id:%MODEL_ID% | append %MODEL_ID% to _aiurn:model:id:_ the identifier of your llm | 1..1 | uid = aiurn:model:id:_geepeetee_
| provider | aiurn:model:provider:azure or <br/> aiurn:model:provider:openai | specify the provider of the Model [^1]: More Provider to follow.| 1..1 | provider = aiurn:model:provider:azure 
| model | %MODEL_NAME% | specify the given name of the model, recognize this with the selected provider. I.e Azure Foundry uses a custom name for this | 1..1 | model = "gpt-4o"
| endpoint    | %ENDPOINT% | The endpoint the provider ensures access| 1..1 |  endpoint = "https://any.openai.azure.com/"
| version   | %VERSION% | a version how to talk to the provider | 1..1  | version = "2025-01-01-preview"
| aiurn:global:var | aiurn::globalvar:%VARNAME% = %MY_VALUE"| add a property to the llm. The parameter names can also overide model options if name is aligned | 0..N | aiurn:var:temperature = 0.7
