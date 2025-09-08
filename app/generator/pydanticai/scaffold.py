# Project Scaffold Generator
import os

def scaffold_project(target_dir, project_name):
    os.makedirs(target_dir, exist_ok=True)
   
  
    # .gitignore
    with open(os.path.join(target_dir, ".gitignore"), "w") as f:
        f.write("__pycache__/\n*.pyc\n.env\n")
    # src directory
    src_dir = os.path.join(target_dir, "src")
    os.makedirs(src_dir, exist_ok=True)
    with open(os.path.join(src_dir, "__init__.py"), "w") as f:
        f.write("")

# Example usage:
# scaffold_project("/path/to/target/project", "MyProject")
