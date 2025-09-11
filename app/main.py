import os
from typing import List
import uuid
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from cookiecutter.main import cookiecutter
from cookiecutter.exceptions import OutputDirExistsException

from app.model.data.ai_environment import Agent
from app.model.generators import AgentGenerator
from app.model.listener.agent.listener import BaseAIAgentListener
from app.model.listener.service.listener import BasicServiceListener
from app.model.listener.nonfunctional.listener import NonFunctionalListener
from app.model.project import  Project, ProjectTemplate
from app.agent_grammer.parser.ai_environmentLexer import ai_environmentLexer
from app.agent_grammer.parser.ai_environmentParser import ai_environmentParser


techstacks = [ProjectTemplate(
                        'aiurn:techstack:basic:pydantic', 
                        'Pydantic Standalone',
                        os.path.join("project-templates", "basic", "pydantic-service"),
                        [NonFunctionalListener],
                        [BaseAIAgentListener],
                        [BasicServiceListener] )
                        
                 ]


def _scaffold_project_layer(target_dir, proj: Project, ):
    """
    Create initial project structure using the selected cookiecutter template.
    """
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
 
def _scaffold_agent_layer(target_dir, proj: Project, agent:Agent):
    """
    Create initial project structure using the selected cookiecutter template.
    """
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
    

def _scaffold_service_layer(target_dir, proj: Project, agents:List[Agent]):
    """
    Create initial project structure using the selected cookiecutter template.
    """

    agents = [agent.__dict__ for agent in agents]
    agents = dict(enumerate(agents))
    
    template_path = os.path.join(os.path.dirname(__file__), proj.get_servicelayer())
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
            template_path,
            output_dir=os.path.dirname(os.path.abspath(target_dir)),
            no_input=True,
            extra_context={"project_name": project_name, "agents":agents, "project_build_id": proj.project_build_id},
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
    # Agent Layer
    for listenerClass in project.template.agentlistener:
        listener = listenerClass()
        
        walker.walk(listener, tree)
        for agent in listener.agents:
            _scaffold_agent_layer(target_dir, project, agent)

    # Service Layer
    for listener in project.template.servicelistener:
        listener = listenerClass()
        
        walker.walk(listener, tree)
        for agent in listener.agents:
            _scaffold_service_layer(target_dir, project, listener.agents)
        
        
       
    print(f"AI Environment generated to {target_dir}")


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

