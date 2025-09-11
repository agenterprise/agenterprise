import os
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from cookiecutter.main import cookiecutter
from cookiecutter.exceptions import OutputDirExistsException

from app.model.generators import AgentGenerator
from app.model.listener.agent.listener import PydanticAIListener
from app.model.listener.nonfunctional.listener import NonFunctionalListener
from app.model.project import  Project, ProjectTemplate
from app.agent_grammer.parser.ai_environmentLexer import ai_environmentLexer
from app.agent_grammer.parser.ai_environmentParser import ai_environmentParser
from app.generator.pydanticai.generator import PydanticAgentGenerator


techstacks = [ProjectTemplate(
                        'aiurn:techstack:basic:pydantic', 
                        'Pydantic Standalone',
                        os.path.join("project-templates", "basic", "pydantic-standalone"),
                        [(PydanticAIListener,
                        [PydanticAgentGenerator])] ),
                 ProjectTemplate(
                        'aiurn:techstack:basic:pydantic', 
                        'Pydantic Standalone',
                        os.path.join("project-templates", "basic", "pydantic-standalone"),
                        [(PydanticAIListener,
                        [PydanticAgentGenerator])] )
                        
                 ]

def _scaffold_project_structure(target_dir, proj: Project):
    """
    Create initial project structure using the selected cookiecutter template.
    """
    template_path = os.path.join(os.path.dirname(__file__), proj.get_template_path())
    project_name = os.path.basename(os.path.abspath(target_dir))
    try:
        cookiecutter(
            template_path,
            output_dir=os.path.dirname(os.path.abspath(target_dir)),
            no_input=True,
            extra_context={"project_name": project_name}
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

    project = Project(urn=nonfuncListener.environment.techstack, target_dir=target_dir, techstacks=techstacks)
    _scaffold_project_structure(target_dir, project)
    # Functional Part
    for bundle in project.template.generatorbundles:
        listenerClass = bundle[0]
        listener = listenerClass()
        
        walker.walk(listener, tree)

        for generatorClass in bundle[1]:
            
            generator = generatorClass(target_dir=target_dir, project=project)
            if issubclass(generatorClass, AgentGenerator):
                for agent in listener.agents:
                    generator.generate_all(
                        agent=agent
                    )
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

