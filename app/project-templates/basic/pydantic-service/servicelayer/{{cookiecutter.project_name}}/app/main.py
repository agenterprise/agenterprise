import uvicorn
import sys
import logging
from app.gen.config.service_settings import BaseAISettings, EnvEnum
from app.gen.config.crosscutting_settings import CrossCuttingSettings

settings = BaseAISettings()


logger = logging.getLogger(__name__)
crosscutting = CrossCuttingSettings()
def app():
   
    try:
        if settings.run_environment == EnvEnum.base:
            from app.gen.config.base import app

        logger.info(f"Running App in Env Mode: {settings.run_environment}")
        return app()
    except Exception as e:
        logger.error(f"Error during app initialization: {e}")
        raise

def logger_conf():
    try:
        if settings.run_environment == EnvEnum.base:
            from app.gen.config.base import logger_conf

        logger.info(f"Applying Logging in Env Mode: {settings.run_environment}")
        return logger_conf()
    except Exception as e:
        logger.error(f"Error during logger initialization: {e}")
        raise

def main():
    logger.info(f"Starting {settings.app_name}")
    uvicorn.run("main:app", 
                host=str(settings.uvicorn_host), 
                reload=settings.uvicorn_reload, 
                port=settings.uvicorn_port, 
                env_file=settings.uvicorn_env_file, 
                log_level=settings.uvicorn_log_level,
                log_config=logger_conf())
if __name__ == "__main__":
    main()