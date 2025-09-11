import os
from jinja2 import Environment, FileSystemLoader
from app.model.data.ai_environment import Agent
from app.model.generators import AgentGenerator
from app.model.project import Project

class PydanticAgentGenerator(AgentGenerator):
    """
    Generates agent source code and Dockerfile from Jinja2 templates and writes them to the filesystem.
    All folder and filename definitions are accessible via self, not as parameters.
    """
    def __init__(self, target_dir: str, project: Project ):
        self.target_dir = target_dir
        self.project_root = target_dir
        self.app_dir = os.path.join(target_dir, "app")
        self.template_dir = project.get_jinja_template_path()
        self.env = Environment(loader=FileSystemLoader(self.template_dir))
        # File and folder names (can be customized after instantiation)
        self.filename_dockerfile_gen = 'Dockerfile.gen'
        self.filename_pyproject_toml = 'pyproject.toml'
        self.filename_readme = 'README.gen.md'
        self.folder_codegen = 'gen'
        self.filename_dockerfile = 'Dockerfile'

    def create_docker_buildimage_name(self, agent: Agent):
        return f'build_{agent.uid.to_varname}'
    
    def get_module_folder(self, agent: Agent):
        return os.path.join(self.app_dir, agent.namespace.to_filepath()) if agent.namespace else self.target_dir

    def get_codegen_folder(self, module_folder):
        return os.path.join(module_folder, self.folder_codegen)

    def get_agent_pyfile(self, agent: Agent, codegenfolder):
        return os.path.join(codegenfolder, f'{agent.uid.to_varname()}.py')

    def get_dockerfile(self):
        return os.path.join(self.target_dir, self.filename_dockerfile)

    def get_dockerfile_build(self, module_folder):
        return os.path.join(self.project_root, self.filename_dockerfile_gen)

    def get_readme_filepath(self, module_folder):
        return os.path.join(self.project_root, self.filename_readme)

    def get_pyproject_filepath(self, module_folder):
        return os.path.join(self.project_root, self.filename_pyproject_toml)

    def _scaffold_agent_folder(self, module_folder):
        """
        Create the agent folder if it does not exist and add __init__.py for Python module.
        Args:
            module_folder (str): Path to the agent's module folder.
        """
        os.makedirs(module_folder, exist_ok=True)
        init_path = os.path.join(module_folder, "__init__.py")
        if not os.path.exists(init_path):
            with open(init_path, "w") as f:
                f.write("")

    def generate_all(self, agent: Agent):
        """
        Scaffold agent folder (using namespace as module), generate agent code and Dockerfile, and write both to the filesystem.
        Args:
            agent (Agent): Agent dataclass instance.
        Returns:
            tuple: (agent_filepath, docker_filepath, readme_filepath, pyproject_filepath)
        """
        module_folder = self.get_module_folder(agent)
        self._scaffold_agent_folder(module_folder)
        codegenfolder = self.get_codegen_folder(module_folder)
        os.makedirs(codegenfolder, exist_ok=True)
        agent_gen_sourcecode_filepath = self.get_agent_pyfile(agent, codegenfolder)
        docker_filepath = self.get_dockerfile()
        docker_filepath_build = self.get_dockerfile_build(module_folder)
        readme_filepath = self.get_readme_filepath(module_folder)
        pyproject_filepath = self.get_pyproject_filepath(module_folder)
        # Agent code
        agent_code = self._render_agent(agent)
        with open(agent_gen_sourcecode_filepath, 'w') as f:
            f.write(agent_code)
        # Dockerfile
        run, build = self._render_dockerfile(agent)
        with open(docker_filepath, 'w') as f:
            f.write(run)
        with open(docker_filepath_build, 'w') as f:
            f.write(build)
        # README
        readme_code = self._render_readme(agent, module_folder)
        with open(readme_filepath, 'w') as f:
            f.write(readme_code)
        # pyproject.toml
        pyproject_code = self._render_pyproject(agent)
        with open(pyproject_filepath, 'w') as f:
            f.write(pyproject_code)
        return agent_gen_sourcecode_filepath, docker_filepath, readme_filepath, pyproject_filepath

    def _render_agent(self, agent: Agent):
        template = self.env.get_template('agent.jinja2')
        return template.render(
            agent_name=agent.name,
            systemprompt=agent.systemprompt,
            properties={ key.to_varname():val for key,val in agent.properties.items()  }
        )

    def _render_dockerfile(self, agent: Agent):
        template_build = self.env.get_template('Dockerfile.build.jinja2')
        template_run = self.env.get_template('Dockerfile.jinja2')
        pyfile_name = f'{agent.uid}.py'
        return (
            template_run.render(agent_file=pyfile_name, docker_imagename=self.create_docker_buildimage_name(agent)),
            template_build.render(agent_file=pyfile_name, uid=agent.uid, pyproject_file=self.filename_pyproject_toml)
        )

    def _render_readme(self, agent: Agent, agent_folder):
        template = self.env.get_template('README.jinja2')
        return template.render(
            agent_name=agent.name,
            systemprompt=agent.systemprompt,
            properties=agent.properties,
            agent_folder=agent_folder,
            filename_dockerfile_gen=self.filename_dockerfile_gen,
            docker_imagename=self.create_docker_buildimage_name(agent)
        )

    def _render_pyproject(self, agent: Agent):
        template = self.env.get_template('pyproject.toml.jinja2')
        return template.render(project_name=agent.name)