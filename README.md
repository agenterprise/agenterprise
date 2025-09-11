# Agenterprise: AI Agent Generator

## Getting Started



0. **Create a virtual environment**  
    Use [uv venv](https://github.com/astral-sh/uv) to create an isolated Python environment for your dependencies:
    ```bash
    uv venv .venv
    ```
    Then activate the environment:
    ```bash
    source .venv/bin/activate
    ```

1. **Install dependencies**  
    Make sure you have [uv](https://github.com/astral-sh/uv) installed (recommended for fast Python dependency management):

    ```bash
    uv pip install -r pyproject.toml
    ```

2. **Prepare your DSL file**
    Place your agent DSL file (e.g. template-definitions/agentmicroservice.a4) in the project directory or specify your own path.

3. **Initialize the project and generate agents**
    Run the following command to scaffold the project and generate agent code:
    ```bash
    uv run python -m app.main --setup --dsl template-definitions/agentmicroservice.a4 --target target/myagentenv
    ```


4. **Explore the generated code**
    The generated agent code and Dockerfiles will be available in the target/myagentenv directory.

---

**Enterprise Environments:**
For details on how to set up and use this project in enterprise or corporate environments (e.g. with internal package indexes, proxies, or authentication), please consult [ENTERPRISE.md](ENTERPRISE.md).

