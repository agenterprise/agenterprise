from agenterprise.model.listener.AIURN import AIURN
from agenterprise.model.project import Project
def test_project_setup_default():

    service_techstack = AIURN("aiurn:techstack:github::agenterprise:service-layer-fastapi-base")
    ai_techstack = AIURN("aiurn:techstack:github::agenterprise:ai-layer-pydanticai")
    data_techstack = AIURN("aiurn:techstack:github::agenterprise:data-layer-pydantic")
    p = Project(ai_techstack=ai_techstack, service_techstack=service_techstack, data_techstack=data_techstack, target_dir="/tmp",envid="12344")

    assert p.get_projectlayer() == "https://github.com/agenterprise/service-layer-fastapi-base.git"
    assert p.get_agentlayer() == "https://github.com/agenterprise/ai-layer-pydanticai.git"
