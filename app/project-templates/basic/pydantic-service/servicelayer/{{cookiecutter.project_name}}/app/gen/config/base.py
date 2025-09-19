import logging
import sys
from app.gen.config.service_settings import BaseAISettings
from app.gen.config.crosscutting_settings import CrossCuttingSettings

setting = BaseAISettings()

crosscutting = CrossCuttingSettings()
logging.basicConfig(level=crosscutting.log_level, stream=sys.stdout, format=crosscutting.log_format)

def app():
    
    from app.gen.aiapp import BaseAIApp as AIApp
    from app.gen.middleware.http import BaseHttpMiddleware as HttpMiddleware
    from app.gen.routes.router import BaseRouter as Router
    from app.gen.aimodel.registry import baseAimodelregistry as modelregistry
    from app.gen.ioc.IoCContainer import IoCContainer
    {% for key, agent in cookiecutter.agents.items() %}
    from app.gen.agents.{{agent.uid | aiurnpath}}.agent import BaseAgent as {{agent.uid | aiurnpath}}
    {% endfor %}
   
    router = Router(
         {% for key, agent in cookiecutter.agents.items() %}
        {{agent.uid | aiurnpath}}={{agent.uid | aiurnpath}}(modelregistry=modelregistry),
        {% endfor %}
    )
    middleware = HttpMiddleware()

    container = IoCContainer(middleware=middleware, router=router, modelregistry=modelregistry, toolregistry=None)
    return AIApp(container, title=setting.app_name, version=setting.app_version)

def logger_conf():
    return {
           "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
        "access": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr"
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "uvicorn.error": {
            "level": "INFO",
            "handlers": ["default"],
            "propagate": False
        },
        "uvicorn.access": {
            "level": "INFO",
            "handlers": ["access"],
            "propagate": False
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["default"],
        "propagate": False
    }
        }