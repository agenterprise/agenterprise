# AI Technology Stacks

Agenterprise provides ready-to-use technology stacks for each layer of your AI environment. Mix and match stacks based on your project requirements.

## Available Stacks

| Stack | Layer | Description | Key Features | Reference |
|-------|-------|-------------|--------------|-----------|
| **[service-layer-fastapi-base](https://github.com/agenterprise/service-layer-fastapi-base)** | Service | FastAPI-based REST API framework | 🔥 Async/await, a2a service routing, Auto OpenAPI docs | `aiurn:techlayer:github:www.github.com:agenterprise:service-layer-fastapi-base` |
| **[ai-layer-pydanticai](https://github.com/agenterprise/ai-layer-pydanticai)** | AI | PydanticAI integration with structured outputs | 🤖 a2a messaging, Type-safe interactions, Multi-LLM support | `aiurn:techlayer:github:www.github.com:agenterprise:ai-layer-pydanticai` |
| **[data-layer-pydantic](https://github.com/agenterprise/data-layer-pydantic)** | Data | Pydantic-based data validation | 📊 JSON schema generation, Strict validation, Custom validators | `aiurn:techlayer:github:www.github.com:agenterprise:data-layer-pydantic` |
| **[agentic-middleware-layer-redistream](https://github.com/agenterprise/agentic-middleware-layer-redistream)** | Middleware | Redis Streams for agent communication | ⚡ Real-time streaming, a2a coordination, Message persistence | `aiurn:techlayer:github:www.github.com:agenterprise:agentic-middleware-layer-redistream` |

## Complete Stack Example

```dsl
architecture{
    envid = "fb98001a0ce94c44ad091de3d2e78164"
    service-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:service-layer-fastapi-base
    ai-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:ai-layer-pydanticai
    data-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:data-layer-pydantic
    agentic-middleware-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:agentic-middleware-layer-redistream
}
```

## Discover More

- [Agenterprise GitHub Organization](https://github.com/agenterprise)
- [AI-Layers List](https://github.com/stars/agenterprise/lists/ai-layers)
- [Service-Layers List](https://github.com/stars/agenterprise/lists/service-layers)
