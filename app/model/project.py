import os
from typing import List
import uuid

from app.model.listener.AIURN import AIURN
from app.model.listener.agent.listener import BaseAIAgentListener
from app.model.listener.llm.listener import BaseAILLMListener
from app.model.listener.nonfunctional.listener import NonFunctionalListener
from app.model.listener.service.listener import BasicServiceListener
from app.model.listener.tool.listener import BaseAIToolListener



class Project():

    def __init__(self, ai_techstack: AIURN, service_techstack: AIURN, target_dir: str, envid: str = None):
        self.ai_techstack = ai_techstack
        self.service_techstack = service_techstack
        self.project_layer = service_techstack
        self.project_build_id = envid
        self.target_dir = target_dir

        self.projectlistener = NonFunctionalListener
        self.agentlistener = BaseAIAgentListener
        self.llmlistener = BaseAILLMListener
        self.servicelistener = BasicServiceListener
        self.toollistener = BaseAIToolListener

    def get_projectlayer(self):
        return self.project_layer.to_url()
    def get_agentlayer(self):
        return self.ai_techstack.to_url()
    def get_servicelayer(self):
        return self.service_techstack.to_url()    
    def get_llmlayer(self):
        return self.ai_techstack.to_url()      
    def get_toollayer(self):
        return self.ai_techstack.to_url()    
