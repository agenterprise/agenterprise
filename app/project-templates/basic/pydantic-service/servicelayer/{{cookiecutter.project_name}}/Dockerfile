# Dockerfile.jinja2 for multi-stage build
FROM python:3.12-slim AS run_{{cookiecutter.project_build_id}}
WORKDIR /app
COPY --from=build_{{cookiecutter.project_build_id}} /app /app
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
CMD ["uv", "run", "python", "app:main"]
