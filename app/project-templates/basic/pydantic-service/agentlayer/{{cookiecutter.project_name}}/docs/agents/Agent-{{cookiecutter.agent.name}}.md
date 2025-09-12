# Agent "{{ cookiecutter.agent['name'] }}""
Overview agent
### System Prompt
```
{{ cookiecutter.agent.systemprompt }}
```
### Properties
{% for key, value in cookiecutter.agent.properties.items() %}
- **{{ key | aiurnvar }}**: {{ value }}
{% endfor %}



