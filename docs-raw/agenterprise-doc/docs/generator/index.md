# AI Generator

The Agenterprise Generator transforms your DSL (Domain-Specific Language) definitions into complete, production-ready project structures with all necessary code, configurations, and deployment files.

## Generator Features

- **Technology-Agnostic**: Generate code for different tech stacks from the same DSL
- **Extensible**: Customize templates to match your project requirements
- **Reproducible**: Regenerate projects without losing custom code in designated extension areas
- **Multi-Layer Support**: Architecture, infrastructure, data, and AI functional layers

## How the Generator Works

The generator processes your DSL definition in several steps:

1. **DSL Parsing**: Reads and validates your DSL file
2. **Model Analysis**: Extracts architecture, infrastructure, data, and functional layer definitions
3. **Code Generation**: Creates boilerplate code based on the specified technology layers
4. **Project Structure**: Organizes generated files into a production-ready layout

## Generated Project Structure

A generated project includes:

```
target/mydsl/
├── app/                          # Application source code
│   ├── main.py                  # Entry point
│   ├── ext/                     # Extension points for custom code
│   └── gen/                     # Generated code (regenerable)
├── deployment/                   # Deployment configurations
│   ├── Container.build          # Container build script
│   └── Container.run            # Container run script
├── docs/                         # Generated documentation
├── dsl/                          # Your DSL file
├── pyproject.toml               # Python project configuration
├── README.md                    # Project documentation
└── static/                       # Static assets
```

## Customization and Extension

The generator supports extension points that are preserved during regeneration:

- **`ext/`** folder: Add your custom code here
- **Marked sections**: Code between special markers won't be overwritten
- **Template modifications**: Customize generation behavior via configuration

## Getting Started

1. **[Installation](installation.md)** - Set up Agenterprise
2. **[Learn the DSL](../dsl/index.md)** - Understand the domain-specific language
3. **[Create your first project](installation.md#quick-start-generate-your-first-project)** - Generate a project from a DSL

## Advanced Topics

### Technology Layers

Configure different technology stacks for:
- **Service Layer**: FastAPI, Flask, Django, etc.
- **AI Layer**: PydanticAI, LangChain, etc.
- **Data Layer**: SQLAlchemy, Pydantic, etc.

### Multiple Regenerations

The generator supports multiple regenerations of the same project:
- Your custom code in `ext/` is preserved
- New features added to the DSL are regenerated
- Infrastructure code is updated without losing changes

## Next Steps

- **[Install Agenterprise](installation.md)** to get started
- **Explore [DSL documentation](../dsl/index.md)** to design your system
- **Check the GitHub repository** for templates and examples

## Getting Help

- **GitHub Issues**: Report bugs or request features on [GitHub](https://github.com/agenterprise/agenterprise/issues)
- **Community**: Join community discussions for support
- **Documentation**: Visit [agenterprise.ai](https://www.agenterprise.ai) for more information