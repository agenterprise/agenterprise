llms_txt = """# AgentEnterprise AI Environment DSL - AI Generation Guide

## Overview
This guide helps AI models generate valid AgentMicroservice DSL (Domain Specific Language) files for the AgentEnterprise framework.

## Core Structure
Every AI Environment DSL file has this top-level structure:

```
ai_environment "Name" {
    architecture { ... }
    data { ... }
    infrastructure { ... }
    functional { ... }
}
```

## 1. ARCHITECTURE SECTION
Defines the technical stack components for your AI environment.

### Purpose
Specifies which tech layers are used for different aspects of the system.

### Structure
```
architecture {
    envid = "unique-identifier"
    service-techlayer = aiurn:techlayer:[source]:[path-or-url]
    ai-techlayer = aiurn:techlayer:[source]:[path-or-url]
    data-techlayer = aiurn:techlayer:[source]:[path-or-url]
    agentic-middleware-techlayer = aiurn:techlayer:[source]:[path-or-url]
}
```

### Tech Layer AIURN Format
- Source can be: `github` or `local`
- GitHub format: `aiurn:techlayer:github:www.github.com:organization:repository-name`
- Local format: `aiurn:techlayer:local:..:templates:component-name`

### Common Tech Layers
- Service Layer: `service-layer-fastapi-base`
- AI Layer: `ai-layer-pydanticai`
- Data Layer: `data-layer-pydantic`
- Middleware: `agentic-middleware-layer-redistream`

### Example
```
architecture {
    envid = "fb98001a0ce94c44ad091de3d2e78164"
    service-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:service-layer-fastapi-base
    ai-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:ai-layer-pydanticai
    data-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:data-layer-pydantic
    agentic-middleware-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:agentic-middleware-layer-redistream
}
```

## 2. DATA SECTION
Defines the data entities and their properties used in the system.

### Purpose
Describes all data models and types used by agents and tools.

### Entity Structure
```
entity "DisplayName" {
    uid = aiurn:entity:id:entityname
    element = aiurn:entity:var:fieldname -> TYPE # "Description"
    element = aiurn:entity:var:anotherfield -> TYPE # "Description"
}
```

### Data Types
- `TEXT`: String values
- `NUMBER`: Numeric values
- `BOOL`: Boolean true/false
- `LIST`: Array/list values
- `DICT`: Dictionary/object values
- `ANY`: Any type

### Field Reference Types
- Direct type: `TEXT`, `NUMBER`, `BOOL`, etc.
- Entity reference: `aiurn:entity:id:entityname` (reference to another entity)

### Element Structure
- `aiurn:entity:var:` = variable field
- `aiurn:entity:constant:` = constant field

### Example
```
data {
    entity "Restaurant Query" {
        uid = aiurn:entity:id:restaurantquery
        element = aiurn:entity:var:question -> TEXT # "The question about restaurants"
    }
    
    entity "Restaurant Answer" {
        uid = aiurn:entity:id:restaurantanswer
        element = aiurn:entity:var:answer -> TEXT # "The answer provided"
        element = aiurn:entity:var:restaurant -> aiurn:entity:id:restaurant # "Referenced restaurant"
    }
    
    entity "Restaurant" {
        uid = aiurn:entity:id:restaurant
        element = aiurn:entity:var:name -> TEXT # "Restaurant name"
        element = aiurn:entity:var:street -> TEXT # "Street address"
        element = aiurn:entity:var:city -> TEXT # "City location"
        element = aiurn:entity:var:rating -> NUMBER # "Star rating 1-5"
    }
}
```

## 3. INFRASTRUCTURE SECTION
Defines LLM (Language Model) configurations.

### Purpose
Configures all language models available for use by agents.

### LLM Structure
```
llm "DisplayName" {
    uid = aiurn:model:id:modelname
    provider = aiurn:model:provider:[azure|openai]
    model = "model-identifier"
    endpoint = "https://api.endpoint.com/"
    version = "api-version"
    aiurn:global:var:temperature = 0.7
    aiurn:global:var:customvar = value
}
```

### LLM Providers
- `aiurn:model:provider:azure` = Microsoft Azure OpenAI
- `aiurn:model:provider:openai` = OpenAI

### Common Configuration Variables
- `temperature`: Controls creativity (0.0 = deterministic, 1.0 = creative)
- `costid`: Cost center identifier for billing
- `max_tokens`: Maximum tokens in response
- Custom variables using `aiurn:global:var:variablename`

### Example
```
infrastructure {
    llm "My LLM" {
        uid = aiurn:model:id:geepeetee
        provider = aiurn:model:provider:azure
        model = "gpt-4o"
        endpoint = "https://any.openai.azure.com/"
        version = "2025-01-01-preview"
        aiurn:global:var:temperature = 0.7
        aiurn:global:var:costid = "ewe3949"
    }
}
```

## 4. FUNCTIONAL SECTION
Defines Agents and Tools - the core business logic.

### 4A. AGENTS
Autonomous entities that perform tasks using LLMs.

#### Agent Structure
```
agent "DisplayName" {
    uid = aiurn:agent:id:agentname
    namespace = aiurn:ns:domain:subdomain
    systemprompt = "System instruction for the agent"
    llmref = aiurn:model:id:modelname
    description = "What this agent does"
    example = "Example input"
    example = "Another example"
    tag = "Category"
    tag = "Another category"
    toolref = aiurn:tool:id:toolname
    in = aiurn:entity:id:inputentity
    out = aiurn:entity:id:outputentity
    aiurn:global:var:name = "Agent Name"
    aiurn:global:var:role = "role"
    aiurn:global:var:lifecycle = "permanent"
    aiurn:global:var:events = "event-name"
}
```

#### Required Properties
- `uid`: Unique identifier in format `aiurn:agent:id:name`
- `namespace`: Hierarchical namespace `aiurn:ns:domain:subdomain`
- `systemprompt`: The system prompt instructions
- `llmref`: Reference to LLM defined in infrastructure
- `in`: Input entity type
- `out`: Output entity type

#### Optional Properties
- `description`: What the agent does
- `example`: Example interactions (can have multiple)
- `tag`: Categorization tags (can have multiple)
- `toolref`: Tools available to agent (can have multiple)
- Custom variables via `aiurn:global:var:name`

#### Namespace Format
`aiurn:ns:mainarea:subarea`

Examples:
- `aiurn:ns:kitchen:cooking`
- `aiurn:ns:frontdesk:reservations`
- `aiurn:ns:payment:processing`

#### Example
```
agent "Cook" {
    uid = aiurn:agent:id:cook
    namespace = aiurn:ns:moewe:kitchen
    systemprompt = "You're a four star rated chef working at our restaurant"
    llmref = aiurn:model:id:geepeetee
    description = "A Cook in a restaurant"
    example = "How do I prepare pasta?"
    example = "What's the special today?"
    tag = "Restaurant"
    tag = "Recipes"
    toolref = aiurn:tool:id:crawler:v2
    in = aiurn:entity:id:restaurantquery
    out = aiurn:entity:id:restaurantanswer
    aiurn:global:var:name = "Chef Max"
    aiurn:global:var:role = "cook"
    aiurn:global:var:lifecycle = "permanent"
}
```

### 4B. TOOLS
Functions or services that agents can use to accomplish tasks.

#### Tool Structure
```
tool "DisplayName" {
    uid = aiurn:tool:id:toolname
    type = aiurn:tooltype:[mcp|openapi|code|ressource]
    endpoint = "implementation endpoint"
    description = "What this tool does"
    in = aiurn:entity:id:inputentity
    out = aiurn:entity:id:outputentity
    aiurn:global:var:customvar = value
}
```

#### Tool Types
- `aiurn:tooltype:code` = Inline Python/code implementation
- `aiurn:tooltype:mcp` = Model Context Protocol server
- `aiurn:tooltype:openapi` = OpenAPI/REST endpoint
- `aiurn:tooltype:ressource` = External resource

#### Code Tool Endpoint
For inline code tools, use lambda expressions:
```
endpoint = "lambda input: ToolOutputType(result=calculation)"
```

#### MCP Tool Endpoint
For Model Context Protocol tools:
```
endpoint = "https://mcp-server.com/endpoint"
```

#### Required Properties
- `uid`: Unique identifier in format `aiurn:tool:id:name`
- `type`: Tool type (one of the four types above)
- `endpoint`: Implementation details
- `description`: What the tool does

#### Optional Properties
- `in`: Input entity type
- `out`: Output entity type
- Custom variables via `aiurn:global:var:name`

#### Examples

**Code Tool:**
```
tool "BMI Calculator" {
    uid = aiurn:tool:id:bmi:v1
    type = aiurn:tooltype:code
    endpoint = "lambda bmiquery: ToolOutputType(bmi=round(bmiquery.weight / (bmiquery.height ** 2), 2))"
    description = "Tool calculating the BMI by weight and height"
    in = aiurn:entity:id:bmiquery
    out = aiurn:entity:id:bmiresult
}
```

**MCP Tool:**
```
tool "Web Crawler" {
    uid = aiurn:tool:id:crawler:v2
    type = aiurn:tooltype:mcp
    endpoint = "https://remote.mcpservers.org/fetch/mcp"
    description = "Tool for fetching and parsing webpages"
}
```

**OpenAPI Tool:**
```
tool "Weather Service" {
    uid = aiurn:tool:id:weather:v1
    type = aiurn:tooltype:openapi
    endpoint = "https://api.weather.service/v1"
    description = "Get weather information for any location"
}
```

## 5. AIURN IDENTIFIER FORMATS

### Entity IDs
`aiurn:entity:id:entityname`
- Used in `uid` fields of entities
- Used to reference entity types in `in` and `out` properties

### Entity Variables
`aiurn:entity:var:fieldname`
- Used to define entity fields
- Scope: within entity definition

### Entity Constants
`aiurn:entity:constant:fieldname`
- Used for constant fields
- Scope: within entity definition

### Agent IDs
`aiurn:agent:id:agentname`
- Used in `uid` fields of agents
- Used to reference agents in `llmref` properties

### Agent Namespaces
`aiurn:ns:domain:subdomain`
- Hierarchical organization
- Can have multiple levels (3+ parts)

### LLM IDs
`aiurn:model:id:modelname`
- Used in `uid` fields of LLMs
- Used in agent `llmref` properties

### Tool IDs
`aiurn:tool:id:toolname`
- Used in `uid` fields of tools
- Used in agent `toolref` properties
- Can include version: `aiurn:tool:id:toolname:v1`

### Global Variables
`aiurn:global:var:variablename`
- Used to set custom configuration
- Available on agents, tools, and LLMs
- Value types: number, string, boolean

## 6. COMPLETE EXAMPLE

```
ai_environment "Restaurant Management" {
    architecture {
        envid = "fb98001a0ce94c44ad091de3d2e78164"
        service-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:service-layer-fastapi-base
        ai-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:ai-layer-pydanticai
        data-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:data-layer-pydantic
        agentic-middleware-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:agentic-middleware-layer-redistream
    }
    
    data {
        entity "User Query" {
            uid = aiurn:entity:id:userquery
            element = aiurn:entity:var:question -> TEXT # "User's question"
        }
        
        entity "Restaurant Info" {
            uid = aiurn:entity:id:restaurant
            element = aiurn:entity:var:name -> TEXT # "Restaurant name"
            element = aiurn:entity:var:rating -> NUMBER # "Star rating"
        }
    }
    
    infrastructure {
        llm "Azure GPT-4" {
            uid = aiurn:model:id:gpt4
            provider = aiurn:model:provider:azure
            model = "gpt-4o"
            endpoint = "https://api.openai.azure.com/"
            version = "2025-01-01-preview"
            aiurn:global:var:temperature = 0.7
        }
    }
    
    functional {
        agent "Restaurant Advisor" {
            uid = aiurn:agent:id:advisor
            namespace = aiurn:ns:restaurant:recommendations
            systemprompt = "You are a helpful restaurant recommendation assistant"
            llmref = aiurn:model:id:gpt4
            description = "Provides restaurant recommendations"
            example = "What's a good restaurant for Italian food?"
            tag = "Recommendations"
            in = aiurn:entity:id:userquery
            out = aiurn:entity:id:restaurant
            aiurn:global:var:name = "Restaurant Advisor"
        }
        
        tool "Restaurant Search" {
            uid = aiurn:tool:id:search:v1
            type = aiurn:tooltype:openapi
            endpoint = "https://restaurants.api.com/search"
            description = "Search for restaurants by name, cuisine, or location"
        }
    }
}
```

## 7. NAMING CONVENTIONS

### Entity Names
- Use PascalCase: `RestaurantQuery`, `UserProfile`, `OrderItem`
- Be descriptive: `RestaurantReservationRequest` not just `Request`

### Agent Names
- Use PascalCase: `CookAgent`, `WaiterAssistant`
- Descriptive role: `ReservationManager`, `BillingProcessor`

### Tool Names
- Use snake_case in IDs: `aiurn:tool:id:web_crawler:v2`
- PascalCase in display names: `"Web Crawler"`
- Include version: `v1`, `v2`

### Agent Namespaces
- Use lowercase with underscores: `aiurn:ns:kitchen:food_prep`
- Hierarchical: `aiurn:ns:domain:subdomain:component`

## 8. GENERATION RULES

When generating DSL files, follow these rules:

1. **Identifiers must be unique**: Each `uid` must be unique across the entire file
2. **References must exist**: Any `ref` or `id` reference must have a corresponding definition
3. **Required fields**: All required fields must be present
4. **Type consistency**: Referenced entity types must be defined in the data section
5. **Namespace hierarchy**: Use meaningful namespaces that reflect the domain structure
6. **Comments**: Use `#` for descriptions (optional but recommended)
7. **Indentation**: Use 4 spaces for indentation
8. **Strings**: Property values should be wrapped in double quotes

## 9. VALIDATION CHECKLIST

Before generating a DSL file, verify:

- [ ] Exactly one `ai_environment` block
- [ ] All four sections present: architecture, data, infrastructure, functional
- [ ] All referenced LLM IDs exist in infrastructure section
- [ ] All referenced entity IDs exist in data section
- [ ] All referenced tool IDs exist in functional section
- [ ] No duplicate UIDs
- [ ] All namespace hierarchies are consistent
- [ ] Tool types are valid (mcp, openapi, code, ressource)
- [ ] Entity types are valid (TEXT, NUMBER, BOOL, LIST, DICT, ANY)
- [ ] Provider types are valid (azure, openai)

## 10. COMMON PATTERNS

### Pattern: Multi-stage Agent Pipeline
```
entity "Input" { uid = aiurn:entity:id:input ... }
entity "Intermediate" { uid = aiurn:entity:id:intermediate ... }
entity "Output" { uid = aiurn:entity:id:output ... }

agent "Stage1" {
    uid = aiurn:agent:id:stage1
    in = aiurn:entity:id:input
    out = aiurn:entity:id:intermediate
}

agent "Stage2" {
    uid = aiurn:agent:id:stage2
    in = aiurn:entity:id:intermediate
    out = aiurn:entity:id:output
}
```

### Pattern: Agent with Multiple Tools
```
agent "MultiTool Agent" {
    uid = aiurn:agent:id:multitool
    toolref = aiurn:tool:id:tool1:v1
    toolref = aiurn:tool:id:tool2:v1
    toolref = aiurn:tool:id:tool3:v1
}
```

### Pattern: Custom Configuration Variables
```
agent "Configured Agent" {
    uid = aiurn:agent:id:configured
    aiurn:global:var:department = "Sales"
    aiurn:global:var:timeout = 30
    aiurn:global:var:retry_count = 3
}
```

---

This guide should enable AI models to generate syntactically correct and semantically meaningful AgentEnterprise DSL files.
"""