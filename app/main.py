import os
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from app.agent_grammer.parser.agentenvironmentLexer import agentenvironmentLexer
from app.agent_grammer.parser.agentenvironmentParser import agentenvironmentParser
from app.generator.pydanticai.listener import PydanticAIListener
from app.generator.pydanticai.generator import AgentFileGenerator
from app.datamodel.agent import Agent  # <-- Use the shared Agent dataclass


def scaffold_project_structure(target_dir):
    """
    Create initial project structure if it does not exist.
    """
    os.makedirs(target_dir, exist_ok=True)
    # Example: create a src folder and a .gitignore
    src_dir = os.path.join(target_dir, "src")
    os.makedirs(src_dir, exist_ok=True)
    gitignore_path = os.path.join(target_dir, ".gitignore")
    if not os.path.exists(gitignore_path):
        with open(gitignore_path, "w") as f:
            f.write("__pycache__/\n*.pyc\n.env\n")
    # Add more initial files/folders as needed


def run_setup(target_dir, dsl_file):
    scaffold_project_structure(target_dir)
    print(f"Project structure created in {target_dir}")
    if not dsl_file:
        raise ValueError("DSL file (--dsl) must be specified for code-generation.")
    run_code_generation(dsl_file, target_dir)


def run_code_generation(dsl_file, target_dir):
    input_stream = FileStream(dsl_file)
    lexer = agentenvironmentLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = agentenvironmentParser(stream)
    tree = parser.env()

    listeners = [PydanticAIListener()]
    walker = ParseTreeWalker()
    for listener in listeners:
        walker.walk(listener, tree)

    generator = AgentFileGenerator(target_dir=target_dir)
    for agent in listeners[0].agents:
        # Ensure agent is an instance of the imported Agent dataclass
        generator.generate_all(
            agent=agent
        )

    print(f"Agent source code updated in {target_dir}")


def run_dsl_template(dsl_file):
    if not dsl_file:
        raise ValueError("DSL file (--dsl) must be specified for template generation.")
    dsl_dir = os.path.dirname(dsl_file)
    os.makedirs(dsl_dir, exist_ok=True)
    if not os.path.exists(dsl_file):
        with open(dsl_file, "w") as f:
            f.write("// Agent DSL template\n// Define your agents here\n")
        print(f"DSL template created at {dsl_file}")
    else:
        print(f"DSL file already exists at {dsl_file}")


def main(mode, dsl_file=None, target_dir=None):
    if mode == "setup":
        run_setup(target_dir, dsl_file)
        return
    if mode == "code-generation":
        run_code_generation(dsl_file, target_dir)
        return
    if mode == "dsl-template":
        run_dsl_template(dsl_file)
        return


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Agent project generator")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--setup", action="store_true", help="Initial project setup (scaffold folders)")
    group.add_argument("--code-generation", action="store_true", help="Generate agent code from DSL")
    group.add_argument("--dsl-template", action="store_true", help="Generate a DSL template file at the specified path")
    parser.add_argument("--dsl", type=str, help="Path to agent DSL file (required for setup/code-generation/template)")
    parser.add_argument("--target", type=str, help="Target directory for generated code (required for setup/code-generation)")
    args = parser.parse_args()

    if args.setup:
        if not args.target:
            raise ValueError("--target is required for setup.")
        if not args.dsl:
            raise ValueError("--dsl is required for setup.")
        main("setup", target_dir=args.target, dsl_file=args.dsl)
    elif args.code_generation:
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
