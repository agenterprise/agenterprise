from abc import ABC, abstractmethod

from app.model.data.ai_environment import Agent
from app.model.project import Project


class BaseGenerator():

    @abstractmethod
    def __init__(self, target_dir: str, project: Project ):
        pass

    def namespace_to_path(self, urn):
        return "a/b/c"

class AgentGenerator(BaseGenerator):

    @abstractmethod
    def generate_all(self, agent: Agent):
        pass
