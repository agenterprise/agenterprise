from pydantic import BaseModel

class {{ cookiecutter.agent.name }}(BaseModel):
    systemprompt: str = "{{ cookiecutter.agent.systemprompt }}"
    {% for key, value in cookiecutter.agent.properties.items() %}
    {{ key | aiurnvar }}: str = "{{ value }}"
    {% endfor %}

    def ask(self, query: str):
        # Hier kann die Agent-Logik implementiert werden
        return (f"Agent '{{ cookiecutter.agent.name  }}' gestartet mit Systemprompt: {{ cookiecutter.agent.systemprompt }} sagt {query}")