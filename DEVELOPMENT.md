## Quick Start

### 1. Create a virtual environment

Use [uv venv](https://github.com/astral-sh/uv) or your preferred tool:

```bash
uv venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
uv sync --extra dev
```

### 3. Prepare your DSL file

Grab `dsl-examples/agentmicroservice.a4` or copy and modify it

### 4. Generate agent code

At CLI execute
```bash
 uv run python -m agenterprise --code-generation  --dsl dsl-examples/agentmicroservice.a4 --target target/myagentenv  
```

### 5. Explore the generated code

The generated agent code is generated at target/myagentenv  

# Develop and modify
## Grammar

The grammar is based at agenterprise/agent_grammer/parser. Here the ANTLR based Grammar is placed (*.g4)
For deep details please consult https://www.agenterprise.ai/

### Grammar Modification 
In order to be sure the grammar is still valid you can test with 
```bash
antlr4-parse agenterprise/agent_grammer/parser/ai_environment.g4 ai_envDef template-definitions/agentmicroservice.dsl
```
If test are a sucessfull it is mandatory to generate the parser. 
Note: The parsers will be in same directory as the grammar. 
```bash
antlr4 -Dlanguage=Python3 -visitor agenterprise/agent_grammer/parser/ai_environment.dsl
```

# Check Template Definitions
