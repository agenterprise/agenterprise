from agenterprise.model.listener.AIURN import AIURN

def test_github():
    t1 = "aiurn:service-stack:github:www.github.com:agenterprise:ai-layer-pydanticai"
    airun = AIURN(t1)
    githuburl = airun.to_url()
    assert githuburl == "https://www.github.com/agenterprise/ai-layer-pydanticai.git"

    t2 = "aiurn:service-stack:github:myenterprise-hub.com:agenterprise:ai-layer-pydanticai"
    airun = AIURN(t2)
    githuburl = airun.to_url()
    assert githuburl == "https://myenterprise-hub.com/agenterprise/ai-layer-pydanticai.git"

    t3 = "aiurn:service-stack:github::agenterprise:ai-layer-pydanticai"
    airun = AIURN(t3)
    githuburl = airun.to_url()
    assert githuburl == "https://github.com/agenterprise/ai-layer-pydanticai.git"

def test_local():
    t1 = "aiurn:service-stack:local:/:mytemplate/tetete"
    airun = AIURN(t1)
    fileurl = airun.to_url()
    assert fileurl == "/mytemplate/tetete"

    t2 = "aiurn:service-stack:local::mytemplate/tetete"
    airun = AIURN(t2)
    fileurl = airun.to_url()
    assert fileurl == "mytemplate/tetete"


