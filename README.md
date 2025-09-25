# Agenterprise

[![PyPI - Version](https://img.shields.io/pypi/v/agenterprise?label=PyPI&color=blue)](https://pypi.org/project/agenterprise/)
[![Python Versions](https://img.shields.io/pypi/pyversions/agenterprise.svg)](https://pypi.org/project/agenterprise/)
[![License](https://img.shields.io/pypi/l/agenterprise.svg)](https://github.com/agenterprise/agenterprise/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/agenterprise/agenterprise?style=social)](https://github.com/agenterprise/agenterprise)

**Agenterprise** is a powerful generator for AI agent environments, enabling rapid prototyping and deployment of agent-based systems in Python. It leverages modern code generation, Pydantic, and DSL-driven workflows to streamline the creation of scalable, enterprise-ready AI solutions.

---

## Features

- Generate complete AI agent environments from a DSL specification
- Supports modern Python (3.12+)
- Integrates with Pydantic, ANTLR, Cookiecutter, and Jinja2
- Produces ready-to-use code, Dockerfiles, and configuration
- Designed for enterprise and MDSD (Model-Driven Software Development) workflows

---

## Installation

> **Note:** Agenterprise is not yet published on PyPI. To install from source, clone the repository and use pip:

```bash
git clone https://github.com/agenterprise/agenterprise.git
cd agenterprise
pip install .
```

Or, for development:

```bash
pip install -e .
```

---

## Quick Start

### 1. Create a virtual environment

Use [uv venv](https://github.com/astral-sh/uv) or your preferred tool:

```bash
uv venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
uv pip install -r pyproject.toml
```

### 3. Prepare your DSL file

Place your agent DSL file (e.g. `template-definitions/agentmicroservice.a4`) in the project directory or specify your own path.

### 4. Generate agent code

```bash
uv run python -m app.main --setup --dsl template-definitions/agentmicroservice.a4 --target target/myagentenv
```

### 5. Explore the generated code

The generated agent code and Dockerfiles will be available in the `target/myagentenv` directory.

---

## Usage Example

After generating your agent environment, you can import and use the generated modules in your own Python code:

```python
from target.myagentenv.app.main import main

main()
```

Or run the CLI as shown above.

---

## Python Compatibility

- Python >= 3.12

---

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

---

## Project Links

- Homepage: [https://agenterprise.ai](https://agenterprise.ai)
- Repository: [https://github.com/agenterprise/agenterprise](https://github.com/agenterprise/agenterprise)
- Issues: [https://github.com/agenterprise/agenterprise/issues](https://github.com/agenterprise/agenterprise/issues)

---

## Author

Michael Vonrueden  
Email: [mail@agenterprise.ai](mailto:mail@agenterprise.ai)

---

## Enterprise Environments

For details on how to set up and use this project in enterprise or corporate environments (e.g. with internal package indexes, proxies, or authentication), please consult [ENTERPRISE.md](ENTERPRISE.md).
