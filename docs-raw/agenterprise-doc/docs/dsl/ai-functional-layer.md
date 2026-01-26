---
hide:
  - toc
---
# AI Functional Layer

This section covers the AI functional layer in the Agenterprise DSL. It describes how to define agents, their properties, prompts, references, and variables.

## Agent
Example
```dsl
agent "Cook" {
        uid = aiurn:agent:id:cook
        namespace = aiurn:ns:moewe:kitchen
        systemprompt = "You're a four star rated metre working at restaurant https://moewe.agenterprise.ai/"
        llmref = aiurn:model:id:geepeetee 
        toolref = aiurn:tool:id:crawler:v2
        in = aiurn:entity:id:restaurantquery
        out = aiurn:entity:id:restaurantanswer 
        aiurn:global:var:name = "Max Mustermann"
        aiurn:global:var:role = "cook"
        aiurn:global:var:lifeycle = "permanent"
        aiurn:global:var:events = "onRestaurantOpening"     
        
}
```
### Specs
Give the Agent a name by assign a name to agent %MY_NAME% { ... }

| Attribute | Assignment | Rule  | Cardinality  | Examples |
| --------  | --------   | -------- | -------- | -------- |
| uid       | aiurn:agent:id:%AGENT_ID% | append %AGENT_ID% to _aiurn:agent:id:_ the name of your agent | 1..1 | aiurn:agent:id:_cook_ 
| namespace | aiurn:ns:%NAMESPACE%  | append %NAMESPACE% to _aiurn:agent:ns:_ the namespace of the agent. | 1..1 | aiurn:ns:_mynamespace:subnamespace_ <br/>  aiurn:ns:_mynamespace_
| systemprompt | %PROMPT% | The systemprompt | 1..1 | Your act as ...
| llmref    | aiurn:model:id:%LLMID% | take the uid given to the [LLM Defintion](infrastruture-layer.md) | 1..1 | aiurn:model:id:geepeetee:_myllmid_ 
| toolref   | aiurn:tool:id:%TOOLID% | take the uid given to the Tool Definition (below) | 1..1 | aiurn:tool:id:_mycrawler_ 
| in  |  aiurn:entity:id:%ENTITY_ID% | input value  to the agent | 0..N | in = aiurn:entity:id:restaurantquery
| out  |  aiurn:entity:id:%ENTITY_ID% | output value  to the agent | 0..N | out = aiurn:entity:id:restaurantanswer 
| aiurn:global:var | aiurn:globa:var:%VARNAME%| add a property to the agent | 0..N |  aiurn:global:var:role = "cook"


## Tool
Example:
```dsl
tool "bmicalculator" {
        uid = aiurn:tool:id:bmi:v1
        in = aiurn:entity:id:bmiquery
        out = aiurn:entity:id:bmiresult
        endpoint = "lambda bmiquery: ToolOutputType(bmi=round(bmiquery.weight / (bmiquery.height ** 2), 2))"
        type = aiurn:tooltype:code
        description = "Tool calculating the bmi by weight and height"
}
```
### Specs
Give the Tool a name by assign a name to tool %MY_NAME% { ... }

| Attribute | Assignment | Rule  | Cardinality  | Examples |
| --------  | --------   | -------- | -------- | -------- |
| uid       | aiurn:tool:id:%TOOL_ID% | append %TOOL_ID% to _aiurn:tool:id:_ the name of your tool | 1..1 | aiurn:tool:id:_bmi:v1_ 
| in | aiurn:entity:id:%ENTITY_ID% | specify a input variable that will be provided | 0..N | in = aiurn:entity:id:bmiquery
| out | aiurn:entity:id:%ENTITY_ID% | specify a output variable that will be provided | 0..N | out = aiurn:entity:id:bmiresult
| endpoint    | %ENDPOINT% | Depending on type specify: <ul><li> MCP --> a streamable https url to remote MCP server</li><li>python code --> write a custom python function</li><ul>| 1..1 | <ul><li> MCP --> https://remote.mcpservers.org/fetch/mcp</li><li>python code --> ```"lambda weight, height: round(weight / (height ** 2), 2)"```</li><ul>
| type   | aiurn:tooltype:code <br/> aiurn:tooltype:mcp <br/> aiurn:tooltype:openapi <br/> aiurn:tooltype:ressource | specify the tool type | 1..1  | aiurn:tooltype:code
| description| a text |A  description of the tool | 1..1 | "Tool calculating the bmi by weight and height"