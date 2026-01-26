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
- Produces ready-to-use code, Dockerfiles, and configuration
- Designed for enterprise and MDSD (Model-Driven Software Development) workflows

---

## Installation

### PyPI

```bash
pip install agenterprise
```

### Local
Follow these steps to install it from source
```bash
git clone https://github.com/agenterprise/agenterprise.git
cd agenterprise
pip install .
```

Or, for development:

```bash
pip install -e .
```

## Usage Example

### Create a DSL File
You can either start with a DSL File from scratch (see http://www.agenterprise.ai) or generate a sample file with:
```bash
agenterprise --dsl-template --dsl mydsl.dsl     
```
### Generate a project
Whith your created DSL File you can now generate a project:
```bash
agenterprise --code-generation --dsl mydsl.dsl --target target/mydsl
```

---



## Python Compatibility

- Python >= 3.12

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/agenterprise/agenterprise/tree/master?tab=MIT-1-ov-file#readme) file for details.


---

## Project Links

- Homepage: [https://www.agenterprise.ai](https://www.agenterprise.ai)
- Repository: [https://github.com/agenterprise/agenterprise](https://github.com/agenterprise/agenterprise)
- Issues: [https://github.com/agenterprise/agenterprise/issues](https://github.com/agenterprise/agenterprise/issues)

---

## Author

Michael Vonrueden  
Email: [mail@agenterprise.ai](mailto:mail@agenterprise.ai)

---

