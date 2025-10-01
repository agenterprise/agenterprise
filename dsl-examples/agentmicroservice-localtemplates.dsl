ai_environment "AgentMicroservice" {
    architecture{
        envid = "fb98001a0ce94c44ad091de3d2e78164"
        service-techlayer = aiurn:techlayer:local:..:templates:service-layer-fastapi-base
        ai-techlayer = aiurn:techlayer:local:..:templates:ai-layer-pydanticai
        
        }

    infrastructure {
        llm "My LLM" {
            uid = aiurn:model:id:geepeetee
            provider = aiurn:model:provider:azure 
            model = "gpt-4o"
            endpoint = "https://any.openai.azure.com/"
            version = "2025-01-01-preview"
            aiurn:var:temperature = 0.7
            aiurn:var:costid = "ewe3949" 
            aiurn:var:hello = True 
        }
    }


    functional{
        agent "Cook" {
            uid = aiurn:agent:cook
            namespace = aiurn:ns:janes_diner:kitchen
            systemprompt = "You're a four star rated metre"
            llmref = aiurn:model:id:geepeetee 
            toolref = aiurn:tool:cooking:v1
            toolref = aiurn:tool:freezer:v2
            aiurn:var:name = "Max Mustermann"
            aiurn:var:role = "waiter"
            aiurn:var:lifeycle = "permanent"
            aiurn:var:events = "onRestaurantOpening"
          
        }

        agent "Waiter" {
            uid = aiurn:agent:waiter
            namespace = aiurn:ns:janes_diner:guestroom
            systemprompt = "Du bist ein freundlicher und aufmerksamer Kellner"
            llmref = aiurn:model:id:geepeetee 
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
         tool "FreezerApi2" {
            uid = aiurn:tool:freezer:v2
            endpoint = "http://localhost:8000/mcp"
            type = aiurn:tooltype:mcp
            description = "Tool for inspecting contents of the freezer"
            
        }

    }
}


