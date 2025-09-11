# {{ cookiecutter.project_name }}


{% for key, agent in cookiecutter.agents.items() %}

## {{ agent['name'] }}

This agent is generated using Pydantic and Jinja2.

### System Prompt
```
{{ agent.systemprompt }}
```

### Properties
{% for key, value in agent.properties.items() %}
- **{{ key | aiurnvar }}**: {{ value }}
{% endfor %}

{% endfor %}

# Deployment
## Build Docker Image with external pip index

```bash
# Create a secret file containing your pip index URL
echo "https://pypi.org/simple/" > pip_index_url.txt

# Build the Docker image using BuildKit and mount the secret
DOCKER_BUILDKIT=1 docker build \
  --secret id=pip_index_url,src=pip_index_url.txt \
  -t {{ cookiecutter.package_name }} -f Dockerfile.build .
```

## Run Agent

```bash
docker run --rm {{ cookiecutter.package_name}}
```
