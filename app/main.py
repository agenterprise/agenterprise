import os
import sys
from typing import List
import uuid
import logging 
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from cookiecutter.main import cookiecutter
from cookiecutter.exceptions import OutputDirExistsException

from app.model.data.ai_environment import Agent, Tool
from app.model.data.ai_environment import LLM
from app.model.generators import AgentGenerator
from app.model.listener.agent.listener import BaseAIAgentListener
from app.model.listener.llm.listener import BaseAILLMListener
from app.model.listener.service.listener import BasicServiceListener
from app.model.listener.nonfunctional.listener import NonFunctionalListener
from app.model.listener.tool.listener import BaseAIToolListener
from app.model.project import  Project
from app.agent_grammer.parser.ai_environmentLexer import ai_environmentLexer
from app.agent_grammer.parser.ai_environmentParser import ai_environmentParser

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(levelname)s: %(message)s')

logger = logging.getLogger(__name__)


def _scaffold_project_layer(target_dir, proj: Project):
    """
    Create initial project structure using the selected cookiecutter template.
    """
    logger.info(f"Scaffolding project layer in {target_dir} using template {proj.get_projectlayer()}")
    template_path =  proj.get_projectlayer()
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
            template_path,
            directory="projectlayer",
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

    template_path = proj.get_llmlayer()
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
            template_path,
            directory="llmlayer",
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
    template_path =  proj.get_agentlayer()
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
            template_path,
            directory="agentlayer",
            output_dir=os.path.dirname(os.path.abspath(target_dir)),
            no_input=True,
            extra_context={"project_name": project_name, "agent":agent.__dict__, "project_build_id": proj.project_build_id},
            overwrite_if_exists=True
        )
    except OutputDirExistsException:
        raise RuntimeError("The output directory exists already.")

def _scaffold_tool_layer(target_dir, proj: Project, tool:Tool):
    """
    Create initial project structure using the selected cookiecutter template.
    """
    logger.info(f"Scaffolding tool layer in {target_dir} using template {proj.get_toollayer()}")
    template_path = proj.get_toollayer()
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
            template_path,
            directory="toollayer",
            output_dir=os.path.dirname(os.path.abspath(target_dir)),
            no_input=True,
            extra_context={"project_name": project_name, "tool":tool.__dict__, "project_build_id": proj.project_build_id},
            overwrite_if_exists=True
        )
    except OutputDirExistsException:
        raise RuntimeError("The output directory exists already.")
    

def _scaffold_service_layer(target_dir, proj: Project, agents:List[Agent], llms:List[LLM], tools:List[Tool]):
    """
    Create initial project structure using the selected cookiecutter template.
    """
    logger.info(f"Scaffolding service layer in {target_dir} using template {proj.get_servicelayer()}")
    agents = [agent.__dict__ for agent in agents]
    agents = dict(enumerate(agents))

    llms = [llm.__dict__ for llm in llms]
    llms = dict(enumerate(llms))

    tools = [tool.__dict__ for tool in tools]
    tools = dict(enumerate(tools))
    
    template_path =  proj.get_servicelayer()
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
            template_path,
            directory="servicelayer",
            output_dir=os.path.dirname(os.path.abspath(target_dir)),
            no_input=True,
            extra_context={"project_name": project_name, "agents":agents, "tools":tools, "llms":llms, "project_build_id": proj.project_build_id},
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
    project = Project(ai_techstack=aiEnv.ai_techstack,service_techstack=aiEnv.service_techstack, target_dir=target_dir,  envid=aiEnv.envid)
    _scaffold_project_layer(target_dir, project)
    # Functional Part

    #LLM Layer
    llmListener = project.llmlistener()
    walker.walk(llmListener, tree)
    for llm in llmListener.llms:
        _scaffold_llm_layer(target_dir, project, llm)

    # Agent Layer
    agentListener = project.agentlistener()
    walker.walk(agentListener, tree)
    for agent in agentListener.agents:
        _scaffold_agent_layer(target_dir, project, agent)

    # Tool Layer
    toolListener = project.toollistener()
    walker.walk(toolListener, tree)
    for tool in toolListener.tools:
        _scaffold_tool_layer(target_dir, project, tool)

    # Service Layer
    serviceListener = project.servicelistener()
    walker.walk(serviceListener, tree)
    _scaffold_service_layer(target_dir, project, agentListener.agents, llmListener.llms, toolListener.tools)
 
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

