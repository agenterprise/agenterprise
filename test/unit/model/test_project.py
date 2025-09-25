from agenterprise.model.listener.AIURN import AIURN
from agenterprise.model.project import Project
def test_project_setup_default():

    service_techstack = AIURN("aiurn:techstack:github::agenterprise:service-layer-fastapi-base")
    ai_techstack = AIURN("aiurn:techstack:github::agenterprise:ai-layer-pydanticai")
    p = Project(ai_techstack=ai_techstack, service_techstack=service_techstack,target_dir="/tmp",envid="12344")

    assert p.get_projectlayer() == "https://github.com/agenterprise/service-layer-fastapi-base.git"
