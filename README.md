# Agenterprise: AI Agent Generator

## Getting Started

1. **Install dependencies**  
   Make sure you have [uv](https://github.com/astral-sh/uv) installed (recommended for fast Python dependency management):

   ```bash
   uv pip install -r pyproject.toml
   ```

2. **Prepare your DSL file**
    Place your agent DSL file (e.g. template-definitions/agentswarm.a4) in the project directory or specify your own path.

3. **Initialize the project and generate agents**
    Run the following command to scaffold the project and generate agent code:
    ```bash
    uv run python -m app.main --setup --dsl definitions/agentswarm.a4 --target target/myagentenv
    ```

4. **Explore the generated code**
    The generated agent code and Dockerfiles will be available in the target/myagentenv directory.