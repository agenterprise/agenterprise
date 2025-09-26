ai_environment "AgentMicroservice" {
    architecture{
        envid = "c672da0bd68f41f1b77442524cfa48c4"
        service-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:service-layer-fastapi-base
        ai-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:ai-layer-pydanticai
    }

    infrastructure {
        llm "My LLM" {
            uid = aiurn:model:llm:geepeetee
            provider = aiurn:provider:azure 
            model = "gpt-4o"
            endpoint = "https://any.openai.azure.com/openai/deployments/gpt-4o/chat/completions"
            version = "2025-01-01-preview"
        }
    }


    functional{
        agent "Cook" {
            uid = aiurn:agent:cook
            namespace = aiurn:ns:janes_diner:kitchen
            systemprompt = "You're a four star rated metre"
            llmref = aiurn:model:llm:geepeetee 
            toolref = aiurn:tool:cooking:v1
            toolref = aiurn:tool:cooking:v2
            aiurn:var:name = "Max Mustermann"
            aiurn:var:role = "waiter"
            aiurn:var:lifeycle = "permanent"
            aiurn:var:events = "onRestaurantOpening"
          
        }

        agent "Waiter" {
            uid = aiurn:agent:waiter
            namespace = aiurn:ns:janes_diner:guestroom
            systemprompt = "Du bist ein freundlicher und aufmerksamer Kellner"
            llmref = aiurn:model:llm:geepeetee 
            toolref = aiurn:tool:cooking:v1
            aiurn:var:name = "Max Mustermann"
            aiurn:var:role = "waiter"
            aiurn:var:lifeycle = "permanent"
            aiurn:var:events = "onRestaurantOpening"
        }

        tool "CookingApi" {
            uid = aiurn:tool:cooking:v1
            endpoint = "http://localhost:8000/mcp"
            type = aiurn:tooltype:mcp
            description = "Tool for finding good cooking combinations"
            
        }

    }
}

