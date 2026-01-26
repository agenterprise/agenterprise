import os
import sys
from typing import List
import logging 
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from cookiecutter.main import cookiecutter
from cookiecutter.exceptions import OutputDirExistsException

from agenterprise.model.data.ai_environment import Agent, Entity, Tool
from agenterprise.model.data.ai_environment import LLM
from agenterprise.model.listener.nonfunctional.listener import NonFunctionalListener
from agenterprise.model.project import  Project
from agenterprise.agent_grammer.parser.ai_environmentLexer import ai_environmentLexer
from agenterprise.agent_grammer.parser.ai_environmentParser import ai_environmentParser

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(levelname)s: %(message)s')

logger = logging.getLogger(__name__)

class AIEnvironmentErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, eroer):
        logger.error(f"Syntax error at line {line}, column {column}: {msg}")
        logger.error("Exiting due to syntax error.")
        sys.exit(1) 


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
            extra_context={"project_name": project_name,
                           "project_build_id": proj.project_build_id,
                           "dsl_file": proj.get_dsl_filename()},
            overwrite_if_exists=True,
            skip_if_file_exists=True
        )
    except OutputDirExistsException:
        raise RuntimeError("The output directory exists already.")

def _scaffold_llm_layer(target_dir, proj: Project, llm:LLM, llms:List[LLM]):
    """
    Create layer for llms
    """
    logger.info(f"Scaffolding llm layer in {target_dir} using template {proj.get_llmlayer()}")

    llms = [llm.__dict__ for llm in llms]
    llms = dict(enumerate(llms))
    
    template_path = proj.get_llmlayer()
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
            template_path,
            directory="llmlayer",
            output_dir=os.path.dirname(os.path.abspath(target_dir)),
            no_input=True,
            extra_context={"project_name": project_name,
                           "llm":llm.__dict__, 
                           "llms":llms, 
                           "project_build_id": proj.project_build_id,
                           "dsl_file": proj.get_dsl_filename()},
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
            extra_context={"project_name": project_name, 
                           "agent":agent.__dict__, 
                           "project_build_id": proj.project_build_id,
                           "dsl_file": proj.get_dsl_filename()},
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
            extra_context={"project_name": project_name, 
                           "tool":tool.__dict__, 
                           "project_build_id": proj.project_build_id,
                           "dsl_file": proj.get_dsl_filename()},
            overwrite_if_exists=True
        )
    except OutputDirExistsException:
        raise RuntimeError("The output directory exists already.")
    
def _scaffold_entity_layer(target_dir, proj: Project, entity:Entity):
    """
    Create entities.
    """
    logger.info(f"Scaffolding entity layer in {target_dir} using template {proj.get_entitylayer()}")
    template_path = proj.get_entitylayer()
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
                template_path,
                directory="entitylayer",
                output_dir=os.path.dirname(os.path.abspath(target_dir)),
                no_input=True,
                extra_context={"project_name": project_name, 
                               "entity":entity.__dict__, 
                               "project_build_id": proj.project_build_id,
                               "dsl_file": proj.get_dsl_filename()},
                overwrite_if_exists=True
            )
    except OutputDirExistsException:
        raise RuntimeError("The output directory exists already.")
    

def _scaffold_service_layer(target_dir, proj: Project, agents:List[Agent], llms:List[LLM], tools:List[Tool], entities:List[Entity]):
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

    entities = [entity.__dict__ for entity in entities]
    entities = dict(enumerate(entities))
    
    template_path =  proj.get_servicelayer()
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
            template_path,
            directory="servicelayer",
            output_dir=os.path.dirname(os.path.abspath(target_dir)),
            no_input=True,
            extra_context={"project_name": project_name, 
                           "agents":agents, 
                           "tools":tools, 
                           "llms":llms, 
                           "entities":entities, 
                           "project_build_id": proj.project_build_id,
                           "dsl_file": proj.get_dsl_filename()},
            overwrite_if_exists=True
        )
    except OutputDirExistsException:
        raise RuntimeError("The output directory exists already.")
    
def _scaffold_agentic_middleware_layer(target_dir, proj: Project, agents:List[Agent], llms:List[LLM], tools:List[Tool], entities:List[Entity]):
    """
    Create initial project structure using the selected cookiecutter template.
    """
    logger.info(f"Scaffolding agentic middleware layer in {target_dir} using template {proj.get_agentic_middleware_layer()}")
    agents = [agent.__dict__ for agent in agents]
    agents = dict(enumerate(agents))

    llms = [llm.__dict__ for llm in llms]
    llms = dict(enumerate(llms))

    tools = [tool.__dict__ for tool in tools]
    tools = dict(enumerate(tools))

    entities = [entity.__dict__ for entity in entities]
    entities = dict(enumerate(entities))
    
    template_path =  proj.get_agentic_middleware_layer()
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
            template_path,
            directory="middlewarelayer",
            output_dir=os.path.dirname(os.path.abspath(target_dir)),
            no_input=True,
            extra_context={"project_name": project_name, 
                           "agents":agents, 
                           "tools":tools, 
                           "llms":llms, 
                           "entities":entities, 
                           "project_build_id": proj.project_build_id,
                           "dsl_file": proj.get_dsl_filename()},
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
 
    parser.addErrorListener(AIEnvironmentErrorListener())
    tree = parser.ai_envDef()
    dsl_target_file = os.path.join(target_dir, "dsl", os.path.basename(dsl_file))
    os.makedirs(os.path.dirname(dsl_target_file), exist_ok=True)
    with open(dsl_target_file, "w") as f:
        f.write(str(input_stream))

    os.makedirs(os.path.join(target_dir, ".ai"), exist_ok=True)
    llms_txt_target = os.path.join(target_dir, ".ai", os.path.basename("llms.txt"))
    with open(llms_txt_target, "w") as f:
        from agenterprise.agent_grammer.support.llms_txt import llms_txt
        f.write(llms_txt)
    logger.info(f"Wrote {llms_txt_target}")  
   
    
    # Nonfunctional Part
    nonfuncListener = NonFunctionalListener()
    walker = ParseTreeWalker()
    walker.walk(nonfuncListener, tree)

    aiEnv = nonfuncListener.environment
    project = Project(ai_techstack=aiEnv.ai_techlayer,
                      service_techstack=aiEnv.service_techlayer, 
                      data_techstack=aiEnv.data_techlayer,
                      agentic_middleware_techstack=aiEnv.agentic_middleware_techlayer,
                      target_dir=target_dir,  
                      envid=aiEnv.envid,
                      dsl_file=dsl_target_file)
    _scaffold_project_layer(target_dir, project)
    
   

    # Functional Part

    #LLM Layer
    llmListener = project.llmlistener()
    walker.walk(llmListener, tree)
    for llm in llmListener.llms:
        _scaffold_llm_layer(target_dir, project, llm, llmListener.llms)

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
    
    # Entity Layer
    entityListener = project.entitylistener()
    walker.walk(entityListener, tree)
    for entity in entityListener.entites:
        _scaffold_entity_layer(target_dir, project, entity)

    # Agentic Middleware Layer
    agenticMiddlwareListener = project.agenticMiddlewareListener()
    walker.walk(agenticMiddlwareListener, tree)
    _scaffold_agentic_middleware_layer(target_dir, project, agentListener.agents, llmListener.llms, toolListener.tools, entityListener.entites)
 
    # Service Layer
    serviceListener = project.servicelistener()
    walker.walk(serviceListener, tree)
    _scaffold_service_layer(target_dir, project, agentListener.agents, llmListener.llms, toolListener.tools, entityListener.entites)
 
    
    logger.info(f"AI Environment generated to {target_dir}")


def run_dsl_template(dsl_file):
    with open(dsl_file, "w") as f:
        from agenterprise.agent_grammer.examples.agentmicroservice import example
        f.write(example)
    logger.info(f"DSL template generated to {dsl_file}")    


def main():
    
    import argparse
    from importlib import metadata

    parser = argparse.ArgumentParser(description="AI project generator. Visit https://www.agenterprise.ai/ for more information.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--code-generation", action="store_true", help="Generate agent code from DSL")
    group.add_argument("--dsl-template", action="store_true", help="Generate a DSL template file at the specified path")
    parser.add_argument("--dsl", type=str, help="Path to agent DSL file (required for setup/code-generation/template)")
    parser.add_argument("--target", type=str, help="Target directory for generated code (required for setup/code-generation)")
    parser.add_argument("--version", action="store_true", help="Show the installed version of Agenterprise")
    args = parser.parse_args()

    if args.version:
        version = metadata.version("agenterprise")
        print(f"Agenterprise version: {version}")
        sys.exit(0)
    elif args.code_generation and args.dsl_template:
        raise ValueError("Only one of --code-generation or --dsl-template can be specified.")   
    elif args.code_generation:
        if not args.target:
            raise ValueError("--target is required for code-generation.")
        if not args.dsl:
            raise ValueError("--dsl is required for code-generation.")
        run_code_generation(args.dsl, args.target)
    elif args.dsl_template:
        if not args.dsl:
            raise ValueError("--dsl is required for dsl-template.")
        run_dsl_template(args.dsl)
    else:
        parser.print_help()
    

if __name__ == "__main__":
   
    main()
