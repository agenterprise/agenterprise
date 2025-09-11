import os
from typing import List
import uuid


class ProjectTemplate():

    def __init__(self, urn, name, template_url, projectlistener:List,agentlistener:List, servicelistener:List):
        self.urn = urn
        self.name = name
        self.template_url = template_url    
        self.AGENTLAYER = "agentlayer"
        self.SERVICELAYER = "servicelayer"
        self.PROJECTLAYER= "projectlayer"   
        self.agentlistener = agentlistener
        self.servicelistener = servicelistener
        self.projectlistener = projectlistener


class Project():

    def __init__(self, urn: str, target_dir: str, techstacks: list, envid: str = None):
        self.techstacks = techstacks
        self.project_build_id = envid
        try:
            self.template = [e for e in self.techstacks if e.urn == urn][0]
        except IndexError:
            raise ValueError(f"Unknown project template urn: {urn}. Available: {[e.urn for e in self.techstacks]}")
        self.target_dir = target_dir
        self.cookiecutter_template = self.template.template_url

    # Beispiel für die Abfrage des Pfads:
    def get_template_path(self):
        return self.template.template_url
    
    def get_projectlayer(self):
        return os.path.join(self.template.template_url,self.template.PROJECTLAYER)
    
    def get_agentlayer(self):
        return os.path.join(self.template.template_url,self.template.AGENTLAYER)
    
    def get_servicelayer(self):
        return os.path.join(self.template.template_url,self.template.SERVICELAYER)
    