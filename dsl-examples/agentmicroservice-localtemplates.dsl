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
            systemprompt = "You're a four star rated metre working at https://www.mcdonalds.com/de/de-de/restaurant-suche.html/l/mannheim/willy-brandt-platz-17/1271"
            llmref = aiurn:model:id:geepeetee 
            toolref = aiurn:tool:cooking:v1
            toolref =aiurn:tool:crawler:v2
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
            toolref = aiurn:tool:crawler:v2
            toolref = aiurn:tool:bmi:v1
            aiurn:var:name = "Max Mustermann"
            aiurn:var:role = "waiter"
            aiurn:var:lifeycle = "permanent"
            aiurn:var:events = "onRestaurantOpening"
        }
        tool "bmicalculator" {
            uid = aiurn:tool:bmi:v1
            endpoint = "lambda weight, height: round(weight / (height ** 2), 2)"
            type = aiurn:tooltype:code
            description = "Tool calculating the bmi by weight and height"
            
        }
        tool "Mealdb" {
            uid = aiurn:tool:cooking:v1
            endpoint = "https://www.themealdb.com/api/json/v1/1/search.php?s=$INPUT"
            type = aiurn:tooltype:ressource
            description = "Tool for finding meal. Replace the $INPUT with the meal you like"
            
        }
         tool "Webcrawler" {
            uid = aiurn:tool:crawler:v2
            endpoint = "https://remote.mcpservers.org/fetch/mcp"
            type = aiurn:tooltype:mcp
            description = "Tool for fetching webpages"
            
        }

    }
}


