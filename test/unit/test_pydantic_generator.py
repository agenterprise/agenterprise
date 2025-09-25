import os
from app.generator.pydanticai.generator import PydanticAgentGenerator
import pytest


def test_generate_and_write_files():
    agent_name = "TestAgent"
    systemprompt = "Test system prompt"
    properties = {"role": "tester", "language": "Python"}
    target_dir = os.path.join(os.path.dirname(__file__), '../../target/test/TestAgent')
    generator = PydanticAgentGenerator()
    agent_file, docker_file, readme_file, pyproject_file = generator.generate_all(
        agent_name=agent_name,
        systemprompt=systemprompt,
        properties=properties,
        folder_path=target_dir
    )
    # Check agent file
    with open(agent_file) as f:
        code = f.read()
    assert (f"class {agent_name}(BaseModel):" in code)
    assert(f'systemprompt: str = "{systemprompt}"'in  code)
    assert('role: str = "tester"' in code)
    assert('language: str = "Python"'  in code)
    # Check Dockerfile
    with open(docker_file) as f:
        docker_content = f.read()
    assert(f'COPY {agent_name}.py .'in docker_content)
    # Check README
    with open(readme_file) as f:
        readme_content = f.read()
    assert(agent_name in readme_content)
    assert('docker build -t' in readme_content)
    # Check pyproject.toml
    with open(pyproject_file) as f:
        pyproject_content = f.read()
    assert(f'name = "{agent_name}"' in pyproject_content)
