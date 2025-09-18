import os
import sys
from typing import List
import uuid
import logging 
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from cookiecutter.main import cookiecutter
from cookiecutter.exceptions import OutputDirExistsException

from app.model.data.ai_environment import Agent
from app.model.data.ai_environment import LLM
from app.model.generators import AgentGenerator
from app.model.listener.agent.listener import BaseAIAgentListener
from app.model.listener.llm.listener import BaseAILLMListener
from app.model.listener.service.listener import BasicServiceListener
from app.model.listener.nonfunctional.listener import NonFunctionalListener
from app.model.project import  Project, ProjectTemplate
from app.agent_grammer.parser.ai_environmentLexer import ai_environmentLexer
from app.agent_grammer.parser.ai_environmentParser import ai_environmentParser

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(levelname)s: %(message)s')

logger = logging.getLogger(__name__)
techstacks = [ProjectTemplate(
                        'aiurn:techstack:basic:pydantic', 
                        'Pydantic Standalone',
                        os.path.join("project-templates", "basic", "pydantic-service"),
                        NonFunctionalListener,
                        BaseAIAgentListener,
                        BaseAILLMListener,
                        BasicServiceListener )
                        
                 ]


def _scaffold_project_layer(target_dir, proj: Project):
    """
    Create initial project structure using the selected cookiecutter template.
    """
    logger.info(f"Scaffolding project layer in {target_dir} using template {proj.get_projectlayer()}")
    template_path = os.path.join(os.path.dirname(__file__), proj.get_projectlayer())
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
            template_path,
            output_dir=os.path.dirname(os.path.abspath(target_dir)),
            no_input=True,
            extra_context={"project_name": project_name,"project_build_id": proj.project_build_id},
            overwrite_if_exists=True,
            skip_if_file_exists=True
        )
    except OutputDirExistsException:
        raise RuntimeError("The output directory exists already.")

def _scaffold_llm_layer(target_dir, proj: Project, llm:LLM):
    """
    Create layer for llms
    """
    logger.info(f"Scaffolding llm layer in {target_dir} using template {proj.get_llmlayer()}")

    template_path = os.path.join(os.path.dirname(__file__), proj.get_llmlayer())
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
            template_path,
            output_dir=os.path.dirname(os.path.abspath(target_dir)),
            no_input=True,
            extra_context={"project_name": project_name, "llm":llm.__dict__, "project_build_id": proj.project_build_id},
            overwrite_if_exists=True
        )
    except OutputDirExistsException:
        raise RuntimeError("The output directory exists already.")
   
def _scaffold_agent_layer(target_dir, proj: Project, agent:Agent):
    """
    Create initial project structure using the selected cookiecutter template.
    """
    logger.info(f"Scaffolding agent layer in {target_dir} using template {proj.get_agentlayer()}")
    template_path = os.path.join(os.path.dirname(__file__), proj.get_agentlayer())
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
            template_path,
            output_dir=os.path.dirname(os.path.abspath(target_dir)),
            no_input=True,
            extra_context={"project_name": project_name, "agent":agent.__dict__, "project_build_id": proj.project_build_id},
            overwrite_if_exists=True
        )
    except OutputDirExistsException:
        raise RuntimeError("The output directory exists already.")
    

def _scaffold_service_layer(target_dir, proj: Project, agents:List[Agent], llms:List[LLM]):
    """
    Create initial project structure using the selected cookiecutter template.
    """
    logger.info(f"Scaffolding service layer in {target_dir} using template {proj.get_servicelayer()}")
    agents = [agent.__dict__ for agent in agents]
    agents = dict(enumerate(agents))

    llms = [llm.__dict__ for llm in llms]
    llms = dict(enumerate(llms))
    
    template_path = os.path.join(os.path.dirname(__file__), proj.get_servicelayer())
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
            template_path,
            output_dir=os.path.dirname(os.path.abspath(target_dir)),
            no_input=True,
            extra_context={"project_name": project_name, "agents":agents, "llms":llms, "project_build_id": proj.project_build_id},
            overwrite_if_exists=True
        )
    except OutputDirExistsException:
        raise RuntimeError("The output directory exists already.")
        


def run_code_generation(dsl_file, target_dir):
    """
        run the code generation by dsl file
        1. Identifiy Project Template
        2. Start Code Generation
    """
    input_stream = FileStream(dsl_file)
    lexer = ai_environmentLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ai_environmentParser(stream)
    tree = parser.ai_envDef()
    
    # Nonfunctional Part
    nonfuncListener = NonFunctionalListener()
    walker = ParseTreeWalker()
    walker.walk(nonfuncListener, tree)

    aiEnv = nonfuncListener.environment
    project = Project(urn=aiEnv.techstack, target_dir=target_dir, techstacks=techstacks, envid=aiEnv.envid)
    _scaffold_project_layer(target_dir, project)
    # Functional Part

    #LLM Layer
    llmListener = project.template.llmlistener()
    walker.walk(llmListener, tree)
    for llm in llmListener.llms:
        _scaffold_llm_layer(target_dir, project, llm)

    # Agent Layer
    agentListener = project.template.agentlistener()
    walker.walk(agentListener, tree)
    for agent in agentListener.agents:
        _scaffold_agent_layer(target_dir, project, agent)

    # Service Layer
    serviceListener = project.template.servicelistener()
    walker.walk(serviceListener, tree)
    _scaffold_service_layer(target_dir, project, agentListener.agents, llmListener.llms)
 
    logger.info(f"AI Environment generated to {target_dir}")


def run_dsl_template(dsl_file):
    raise RuntimeError("Not implemented")


def main(mode, dsl_file=None, target_dir=None):
    
    if mode == "code-generation":
        run_code_generation(dsl_file, target_dir)
        return
    if mode == "dsl-template":
        run_dsl_template(dsl_file)
        return


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI project generator")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--code-generation", action="store_true", help="Generate agent code from DSL")
    group.add_argument("--dsl-template", action="store_true", help="Generate a DSL template file at the specified path")
    parser.add_argument("--dsl", type=str, help="Path to agent DSL file (required for setup/code-generation/template)")
    parser.add_argument("--target", type=str, help="Target directory for generated code (required for setup/code-generation)")
    args = parser.parse_args()

    if args.code_generation:
        if not args.target:
            raise ValueError("--target is required for code-generation.")
        if not args.dsl:
            raise ValueError("--dsl is required for code-generation.")
        main("code-generation", dsl_file=args.dsl, target_dir=args.target)
    elif args.dsl_template:
        if not args.dsl:
            raise ValueError("--dsl is required for dsl-template.")
        main("dsl-template", dsl_file=args.dsl)
    else:
        parser.print_help()

