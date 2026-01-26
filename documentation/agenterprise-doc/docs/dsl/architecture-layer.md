---
hide:
  - toc
---
# Architecture Layer

The Architecture Layer defines how your AI environment is structured and which technology stacks it uses for services, AI models, data handling, and agentic middleware.

### 🆕 Agent-to-Agent (a2a) Integration

Agenterprise's key differentiator is built-in **Agent-to-Agent (a2a) integration** for seamless multi-agent communication. The latest stacks include a2a capabilities:

- **AI Layer (ai-layer-pydanticai)**: Direct agent-to-agent message passing and coordination
- **Service Layer (service-layer-fastapi-base)**: Service mesh for distributed agents
- **Middleware Layer (agentic-middleware-layer-redistream)**: High-performance event streaming between agents

Learn more about [available tech stacks](../techstacks/index.md).

## Available Technology Stacks

Agenterprise provides ready-to-use technology stacks that you can reference in your architecture layer. Choose the stacks that best fit your project requirements:

### Service Layer Stacks

Service layers provide the REST API and business logic framework:

- **service-layer-fastapi-base** - High-performance FastAPI-based microservice framework with async support
  - Reference: `aiurn:techlayer:github:www.github.com:agenterprise:service-layer-fastapi-base`
  - Best for: High-performance APIs, real-time applications

### AI Layer Stacks

AI layers handle Large Language Model (LLM) integration and agent orchestration:

- **ai-layer-pydanticai** - PydanticAI integration for structured AI model interactions
  - Reference: `aiurn:techlayer:github:www.github.com:agenterprise:ai-layer-pydanticai`
  - Best for: Type-safe AI agent implementations, structured outputs

### Data Layer Stacks

Data layers manage data validation, serialization, and persistence:

- **data-layer-pydantic** - Pydantic-based data validation and modeling
  - Reference: `aiurn:techlayer:github:www.github.com:agenterprise:data-layer-pydantic`
  - Best for: Strong data validation, schema definition, JSON serialization

### Agentic Middleware Stacks

Middleware layers provide inter-agent communication and event streaming:

- **agentic-middleware-layer-redistream** - Redis-based streaming middleware for agent communication
  - Reference: `aiurn:techlayer:github:www.github.com:agenterprise:agentic-middleware-layer-redistream`
  - Best for: Multi-agent systems, real-time event streaming, distributed agents

### Stack Combinations

A typical complete stack setup:

```dsl
architecture{
    envid = "fb98001a0ce94c44ad091de3d2e78164"
    service-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:service-layer-fastapi-base
    ai-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:ai-layer-pydanticai
    data-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:data-layer-pydantic
    agentic-middleware-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:agentic-middleware-layer-redistream
}
```

### Using Local or Custom Stacks

You can also reference stacks stored locally:

```dsl
service-techlayer = aiurn:techlayer:local:..:templates:service-layer-fastapi-base
ai-techlayer = aiurn:techlayer:local:..:templates:ai-layer-custom
```

### Discovering More Stacks

Find curated lists for Agenterprise layers at:
* [Agenterprise AI-Layers List](https://github.com/stars/agenterprise/lists/ai-layers)
* [Agenterprise Service-Layers List](https://github.com/stars/agenterprise/lists/service-layers)

Feel free to:
* Clone templates for your own purposes
* Create custom stacks by modifying existing templates
* Get in contact with Agenterprise to add your custom stacks to the community lists

---

## Architecture Configuration

### Overview

```dsl
 architecture{
    envid = "fb98001a0ce94c44ad091de3d2e78164"
    service-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:service-layer-fastapi-base
    ai-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:ai-layer-pydanticai
    data-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:data-layer-pydantic     
   
}
```

### Specifications

| Attribute | Assignment | Rule  | Cardinality  | Examples |
| --------  | --------   | -------- | -------- | -------- |
| envid       | %UID% | a unique id as %UID% representing the project | 1..1 | envid = "fb98001a0ce94c44ad091de3d2e78164"
| service-techlayer | aiurn:techlayer:local:%RELATIVE_LOCAL_PATH% <br/>  aiurn:techlayer:github:%GITHUB_DOMAIN%:%PROFILE%:%TEMPLATE% | <ul><li>set your path %RELATIVE_LOCAL_PATH% in an urn style </li><li> %GITHUB_DOMAIN%:%PROFILE%:%TEMPLATE% specifies a public template to a github project in urn style.</li></ul> | 1..1 | service-techlayer = aiurn:techlayer:local:..:templates:service-layer-fastapi-base <br/> service-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:service-layer-fastapi-base
| ai-techlayer | aiurn:techlayer:local:%RELATIVE_LOCAL_PATH% <br/>  aiurn:techlayer:github:%GITHUB_DOMAIN%:%PROFILE%:%TEMPLATE% | <ul><li>set your path %RELATIVE_LOCAL_PATH% in an urn style </li><li> %GITHUB_DOMAIN%:%PROFILE%:%TEMPLATE% specifies a public template to a github project in urn style.</li></ul> | 1..1 | ai-techlayer = aiurn:techlayer:local:..:templates:ai-layer-pydanticai <br/> service-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:ai-layer-pydanticai
| data-techlayer | aiurn:techlayer:local:%RELATIVE_LOCAL_PATH% <br/>  aiurn:techlayer:github:%GITHUB_DOMAIN%:%PROFILE%:%TEMPLATE% | <ul><li>set your path %RELATIVE_LOCAL_PATH% in an urn style </li><li> %GITHUB_DOMAIN%:%PROFILE%:%TEMPLATE% specifies a public template to a github project in urn style.</li></ul> | 1..1 | data-techlayer = aiurn:techlayer:local:..:templates:data-layer-pydantic   <br/> service-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:data-layer-pydantic