# Agenterprise - Model-Driven AI Agent Development

**Define your AI architecture once. Deploy with any tech stack. Scale without vendor lock-in.**

## Why Agenterprise?

Building enterprise AI agents is complex. You juggle:
- Multiple AI agents that need to communicate (a2a)
- Choosing between FastAPI, PydanticAI, Pydantic, Redis...
- Rapid iteration between architecture and implementation
- Avoiding tech stack lock-in

**Agenterprise solves this with Model-Driven Development:**

```
┌──────────────────────────────────────────────────────────┐
│  1. Write your AI architecture in Agenterprise DSL       │
├──────────────────────────────────────────────────────────┤
│  ✅ Define agents, tools, data, infrastructure           │
│  ✅ Technology-agnostic, version-independent             │
│  ✅ Built-in Agent-to-Agent (a2a) support                │
├──────────────────────────────────────────────────────────┤
│  2. Generator creates production-ready project            │
├──────────────────────────────────────────────────────────┤
│  ✅ FastAPI service layer with a2a routing               │
│  ✅ PydanticAI agents with built-in a2a support          │
│  ✅ Pydantic data validation & schemas                   │
│  ✅ Redis Streams for agent coordination                 │
│  ✅ Docker & deployment artifacts                        │
├──────────────────────────────────────────────────────────┤
│  3. Extend & Deploy                                       │
├──────────────────────────────────────────────────────────┤
│  ✅ Add custom code in ext/ (never overwritten)          │
│  ✅ Fork stacks for technical customization              │
│  ✅ Regenerate anytime without losing your code          │
│  ✅ Deploy to Docker, Kubernetes, or serverless          │
└──────────────────────────────────────────────────────────┘
```

## Key Differentiators

### 🤖 Built-in Agent-to-Agent (a2a) Communication
Multi-agent systems require seamless coordination. Agenterprise has a2a communication baked into its AI and Service layers—no add-ons needed.

### 🔄 Tech Stack Flexibility
- Write your DSL once
- Swap FastAPI ↔ other frameworks
- Change PydanticAI ↔ LangChain
- Add middleware (Redis, RabbitMQ, etc.)
- **Same architecture, different implementation**

### 📦 From PoC to Enterprise
- **Quick PoC**: Generate minimal stack with FastAPI + PydanticAI
- **Scale Up**: Add Redis middleware for multi-agent coordination
- **Enterprise Ready**: Customize templates, extend in designated code zones

### 🏗️ Model-Driven Architecture
- Decouples **what** (architecture) from **how** (technology)
- Version your architecture independently of frameworks
- Migrate tech stacks without rewriting your AI logic

---

## Quick Start: 3 Steps

### 1️⃣ Write Your DSL

Define your AI environment in Agenterprise's simple, human-readable language:

```dsl
ai_environment "MyAgentApp" {
    architecture {
        envid = "unique-project-id"
        service-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:service-layer-fastapi-base
        ai-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:ai-layer-pydanticai
        data-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:data-layer-pydantic
        agentic-middleware-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:agentic-middleware-layer-redistream
    }
}
```

See the full [DSL documentation](dsl/index.md) for more.

### 2️⃣ Generate Your Project

```bash
agenterprise --code-generation --dsl mydsl.dsl --target ./my-agent-app
```

Get a **production-ready project** with:
- Complete FastAPI service
- Agent definitions with PydanticAI
- Data models with Pydantic
- **Docker & deployment configuration** (Dockerfile, docker-compose, deployment scripts)
- README and docs
- Ready to deploy to Kubernetes, Docker, or serverless platforms

### 3️⃣ Extend & Deploy

- Add custom logic in designated `ext/` folders
- Regenerate anytime without losing your code
- Deploy to Docker, Kubernetes, or serverless

---

## Two Paths to Extensibility

Agenterprise is designed to be extended endlessly:

### 1️⃣ Technical Extensibility: Extend Tech Stacks

Fork and customize any stack for your needs:

```
Official Stack (fastapi-base)
         ↓
   Your Fork (my-fastapi-enhanced)
         ↓
   Use in DSL: aiurn:techlayer:local:..:templates:my-fastapi-enhanced
```

- Clone any stack from GitHub
- Modify for your specific requirements
- Reference locally or share with the community
- Create entire new layers (e.g., custom LLM integration, alternative databases)

**Result:** Unlimited tech stack combinations tailored to your needs.

### 2️⃣ Functional Extensibility: Extend Generated Projects

Every generated application has designated extension points:

```
Generated Code (safe to regenerate)
         ↓
    ext/ folder (your custom code - never overwritten)
         ↓
    Your Business Logic & Custom Features
```

- Write custom agents, tools, and services in `ext/`
- Regenerate the base project anytime—your code stays intact
- Add business logic without touching generated files
- Iterate your architecture, keep your implementation

**Result:** Seamless iteration between architecture (DSL) and implementation (custom code).

---

## Available Tech Stacks

Choose from curated, actively maintained stacks (Alpha stage). This is just the beginning—the ecosystem will grow with community contributions:

| Stack | Purpose | Highlights |
|-------|---------|-----------|
| **[service-layer-fastapi-base](https://github.com/agenterprise/service-layer-fastapi-base)** | REST API layer | Async, Auto OpenAPI docs, a2a routing |
| **[ai-layer-pydanticai](https://github.com/agenterprise/ai-layer-pydanticai)** | Agent orchestration | Type-safe, **built-in a2a support**, Multi-LLM |
| **[data-layer-pydantic](https://github.com/agenterprise/data-layer-pydantic)** | Data validation | JSON schema, Custom validators |
| **[agentic-middleware-layer-redistream](https://github.com/agenterprise/agentic-middleware-layer-redistream)** | Agent communication | Real-time streaming, Message persistence, a2a |

👉 **[Explore all available stacks →](techstacks/index.md)**

**More coming:** Fork any stack or [contribute your own](https://github.com/agenterprise) to expand the ecosystem!

---

## Learn More

- **[AI DSL Guide](dsl/index.md)** - Learn the domain-specific language
- **[Generator Documentation](generator/index.md)** - Understand code generation
- **[Installation](generator/installation.md)** - Get started in minutes
- **[Tech Stacks](techstacks/index.md)** - See all available components

---

## About Agenterprise

Agenterprise is an **open-source** project built for developers who need:
- Rapid experimentation with AI architectures
- Tech-stack independence
- Multi-agent coordination built-in
- Enterprise-grade foundation

**Status:** Currently in Alpha. We're actively developing and welcome feedback!

---

## Community & Support

- 🐙 [GitHub Organization](https://github.com/agenterprise)
- 💬 [Discussions](https://github.com/agenterprise/agenterprise/discussions)
- 🐛 [Report Issues](https://github.com/agenterprise/agenterprise/issues)
- ⭐ **Star us on GitHub** if you find Agenterprise useful!
