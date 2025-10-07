ai_environment "AgentMicroservice" {
    architecture{
        envid = "fb98001a0ce94c44ad091de3d2e78164"
        service-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:service-layer-fastapi-base
        ai-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:ai-layer-pydanticai
    }
    data{
        entity "Restaurant Answer" {
            uid = aiurn:entity:id:restaurantanswer 
            element = aiurn:entity:var:answer -> TEXT # "The answer of the metre"
            element = aiurn:entity:var:restaurant -> aiurn:entity:id:restaurant  # "The restaurant of the metre"
        }
        entity "Restaurant" {
            uid = aiurn:entity:id:restaurant 
            element = aiurn:entity:var:name -> TEXT # "The name of the restaurant"
            element = aiurn:entity:var:street -> TEXT # "The street where the restaurant is located"
            element = aiurn:entity:var:city -> TEXT # "The city where the restaurant is located"
            element = aiurn:entity:var:rating -> NUMBER # "The rating of the restaurant"
        }
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
            systemprompt = "You're a four star rated metre working at https://www.mcdonalds.com/de/de-de/restaurant-suche.html/l/mannheim/willy-brandt-platz-17/1271"
            llmref = aiurn:model:id:geepeetee 
            toolref =aiurn:tool:crawler:v2
            out = aiurn:agentvar:answer # "The answer of the metre"
            out = aiurn:agentvar:restaurant # "The restaurant the metre is answering for"
            aiurn:var:name = "Max Mustermann"
            aiurn:var:role = "waiter"
            aiurn:var:lifeycle = "permanent"
          
            aiurn:var:events = "onRestaurantOpening"
          
        }

        agent "Waiter" {
            uid = aiurn:agent:waiter
            namespace = aiurn:ns:kkweinhauschen:guestroom
            systemprompt = "Du bist ein freundlicher und aufmerksamer Oberkellner und managed das Restaurant https://www.mcdonalds.com/de/de-de/restaurant-suche.html/l/mannheim/willy-brandt-platz-17/1271"
            llmref = aiurn:model:id:geepeetee 
            toolref = aiurn:tool:bmi:v1
            aiurn:var:name = "Max Mustermann"
            aiurn:var:role = "waiter"
            aiurn:var:lifeycle = "permanent"
            aiurn:var:events = "onRestaurantOpening"
        }
        tool "bmicalculator" {
            uid = aiurn:tool:bmi:v1
            in = aiurn:toolvar:weight # "The weight of the person"
            in = aiurn:toolvar:height # "The heigt of ther person"
            out = aiurn:toolvar:bmi # "The calculated BMI (Body Mass Index)"
            endpoint = "lambda weight, height: round(weight / (height ** 2), 2)"
            type = aiurn:tooltype:code
            description = "Tool calculating the bmi by weight and height"
            
        }
        
         tool "Webcrawler" {
            uid = aiurn:tool:crawler:v2
            endpoint = "https://remote.mcpservers.org/fetch/mcp"
            type = aiurn:tooltype:mcp
            description = "Tool for fetching webpages"
            
        }

    }
}


