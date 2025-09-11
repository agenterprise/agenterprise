import os


class ProjectTemplate():

    def __init__(self, urn, name, template_url, generatorbundles):
        self.urn = urn
        self.name = name
        self.template_url = template_url    
        self.generatorbundles = generatorbundles


class Project():

    def __init__(self, urn: str, target_dir: str, techstacks: list):
        self.techstacks = techstacks
        try:
            self.template = [e for e in self.techstacks if e.urn == urn][0]
        except IndexError:
            raise ValueError(f"Unknown project template urn: {urn}. Available: {[e.urn for e in self.techstacks]}")
        self.target_dir = target_dir
        self.cookiecutter_template = self.template.template_url

    # Beispiel für die Abfrage des Pfads:
    def get_template_path(self):
        return self.template.template_url
    
    def get_jinja_template_path(self):
        return os.path.join(os.path.join(self.target_dir, ".jinja_templates"))