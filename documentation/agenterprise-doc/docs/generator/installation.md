# Installation

Agenterprise can be installed via PyPI or from source for development purposes.

## System Requirements

- **Python**: 3.12 or higher
- **Operating System**: macOS, Linux, or Windows
- **Package Manager**: pip or uv (optional but recommended)

## Installation from PyPI

The easiest way to install Agenterprise is via PyPI:

```bash
pip install agenterprise
```

This will install the latest stable version with all required dependencies. See [PyPI](https://pypi.org/project/agenterprise/) for more details.

## Installation from Source

For development or to use the latest development version, install from the GitHub repository:

```bash
git clone https://github.com/agenterprise/agenterprise.git
cd agenterprise
pip install -e .
```

The `-e` flag installs the package in editable mode, allowing you to make changes to the source code without needing to reinstall.

## Development Installation

If you plan to contribute or develop features for Agenterprise, follow these steps:

```bash
git clone https://github.com/agenterprise/agenterprise.git
cd agenterprise
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

This installs additional development dependencies needed for testing and documentation.

## Verify Installation

After installation, verify that the CLI is available:

```bash
agenterprise --version
```

You should see the version number of the installed Agenterprise package.

## Quick Start: Generate Your First Project

### 1. Create a DSL Template

You can either start with a DSL File from scratch or generate a sample file with:

```bash
agenterprise --dsl-template --dsl mydsl.dsl
```

This generates a sample DSL file that you can use as a starting point. You can edit this file to define your AI environment, architecture, data structures, and agents.

### 2. Generate a Project

With your created DSL File, generate a complete project:

```bash
agenterprise --code-generation --dsl mydsl.dsl --target target/mydsl
```

The generator creates:
- Complete application structure in `app/`
- Deployment configurations in `deployment/`
- Generated documentation in `docs/`
- Project-specific README and configuration files

### 3. Explore Your Generated Project

```bash
cd target/mydsl
ls -la
```

You'll see a complete project structure ready for development and deployment.

## Troubleshooting

### Python Version Issues

If you encounter version-related errors, ensure you're using Python 3.12 or higher:

```bash
python --version
```

If you need to use a specific Python version, consider using `pyenv` or virtual environments.

### Missing Dependencies

If you encounter missing dependency errors, try reinstalling with updated dependencies:

```bash
pip install --upgrade agenterprise
```

### Virtual Environment Issues

Use a Python virtual environment to avoid conflicts:

```bash
python -m venv agenterprise-env
source agenterprise-env/bin/activate  # On Windows: agenterprise-env\Scripts\activate
pip install agenterprise
```

## Next Steps

- **Learn the [AI DSL](../dsl/index.md)** to understand how to define your AI environments
- **Explore [Generator Features](index.md)** to understand what the generator can do
- **Check the GitHub repository** for templates and additional resources

## Getting Help

- **GitHub Issues**: Report bugs or request features on [GitHub](https://github.com/agenterprise/agenterprise/issues)
- **Community**: Join community discussions for support
- **Documentation**: Visit [agenterprise.ai](https://www.agenterprise.ai) for more information
