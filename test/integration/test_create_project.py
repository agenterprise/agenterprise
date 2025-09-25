import tempfile
import shutil
import os
from agenterprise.__main__ import run_dsl_template, run_code_generation, main

def test_project_gen():
    with tempfile.TemporaryDirectory() as tmpdir:
        dsl_filename = "mydsl.dsl"
        dsl_file = os.path.join(tmpdir, dsl_filename)
        run_dsl_template(dsl_file)
        assert os.path.exists(dsl_file)
        project_target = os.path.join(tmpdir, "target", "mydsl")
        run_code_generation(dsl_file,  project_target)
        assert os.path.exists(project_target)
        assert os.path.exists(os.path.join(project_target, "dsl", dsl_filename))
        # No need to manually clean up; TemporaryDirectory handles it

    
