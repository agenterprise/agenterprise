import uuid

identifier = str(uuid.uuid4()).replace("-", "")

example = """ai_environment "AgentMicroservice" {
    architecture{
        envid = "$$IDENTIFIER$$"
        service-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:service-layer-fastapi-base
        ai-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:ai-layer-pydanticai
        data-techlayer = aiurn:techlayer:github:www.github.com:agenterprise:data-layer-pydantic

    }
    data{
        entity "Restaurant Query" {
            uid = aiurn:entity:id:restaurantquery
            element = aiurn:entity:var:question -> TEXT # "The question to the metre"
        }
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

        entity "BMI Query" {
            uid = aiurn:entity:id:bmiquery
            element = aiurn:entity:var:weight -> NUMBER # "The current weight of the person"
            element = aiurn:entity:var:height -> NUMBER # "The current height of the person in meters"
        }

        entity "BMI Result" {
            uid = aiurn:entity:id:bmiresult
            element = aiurn:entity:var:bmi -> NUMBER # "The calcualted bmi of the person"
        }
    }

    infrastructure {
        llm "My LLM" {
            uid = aiurn:model:id:geepeetee
            provider = aiurn:model:provider:azure 
            model = "gpt-4o"
            endpoint = "https://any.openai.azure.com/"
            version = "2025-01-01-preview"
            aiurn:global:var:temperature = 0.7
            aiurn:global:var:costid = "ewe3949" 
            aiurn:global:var:hello = True 
        }
    }


    functional{
        agent "Cook" {
            uid = aiurn:agent:id:cook
            namespace = aiurn:ns:moewe:kitchen
            systemprompt = "You're a four star rated metre working at restaurant https://moewe.agenterprise.ai/"
            llmref = aiurn:model:id:geepeetee 
            toolref = aiurn:tool:id:crawler:v2
            in = aiurn:entity:id:restaurantquery
            out = aiurn:entity:id:restaurantanswer 
            aiurn:global:var:name = "Max Mustermann"
            aiurn:global:var:role = "cook"
            aiurn:global:var:lifeycle = "permanent"
            aiurn:global:var:events = "onRestaurantOpening"
          
        }

        agent "Waiter" {
            uid = aiurn:agent:id:waiter
            namespace = aiurn:ns:moewe:guestroom
            systemprompt = "Du bist eine freundliche und aufmerksame Serviekraft und arbeitest im  Restaurant https://moewe.agenterprise.ai/"
            llmref = aiurn:model:id:geepeetee 
            toolref = aiurn:tool:id:bmi:v1
            toolref = aiurn:tool:id:crawler:v2
            aiurn:global:var:name = "Max Mustermann"
            aiurn:global:var:role = "waiter"
            aiurn:global:var:lifeycle = "permanent"
            aiurn:global:var:events = "onRestaurantOpening"
        }
        tool "bmicalculator" {
            uid = aiurn:tool:id:bmi:v1
            in = aiurn:entity:id:bmiquery
            out = aiurn:entity:id:bmiresult
            endpoint = "lambda bmiquery: ToolOutputType(bmi=round(bmiquery.weight / (bmiquery.height ** 2), 2))"
            type = aiurn:tooltype:code
            description = "Tool calculating the bmi by weight and height"
            
        }
        
         tool "Webcrawler" {
            uid = aiurn:tool:id:crawler:v2
            endpoint = "https://remote.mcpservers.org/fetch/mcp"
            type = aiurn:tooltype:mcp
            description = "Tool for fetching webpages"
            
        }

    }
}


""".replace("$$IDENTIFIER$$", identifier)
