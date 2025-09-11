import unittest
import os
from app.generator.pydanticai.generator import PydanticAgentGenerator

class TestPydanticGenerator(unittest.TestCase):
    def test_generate_and_write_files(self):
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
        self.assertIn(f"class {agent_name}(BaseModel):", code)
        self.assertIn(f'systemprompt: str = "{systemprompt}"', code)
        self.assertIn('role: str = "tester"', code)
        self.assertIn('language: str = "Python"', code)
        # Check Dockerfile
        with open(docker_file) as f:
            docker_content = f.read()
        self.assertIn(f'COPY {agent_name}.py .', docker_content)
        # Check README
        with open(readme_file) as f:
            readme_content = f.read()
        self.assertIn(agent_name, readme_content)
        self.assertIn('docker build -t', readme_content)
        # Check pyproject.toml
        with open(pyproject_file) as f:
            pyproject_content = f.read()
        self.assertIn(f'name = "{agent_name}"', pyproject_content)

if __name__ == "__main__":
    unittest.main()
