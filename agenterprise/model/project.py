import os
from typing import List
import uuid

from agenterprise.model.listener.AIURN import AIURN
from agenterprise.model.listener.agent.listener import BaseAIAgentListener
from agenterprise.model.listener.llm.listener import BaseAILLMListener
from agenterprise.model.listener.nonfunctional.listener import NonFunctionalListener
from agenterprise.model.listener.service.listener import BasicServiceListener
from agenterprise.model.listener.tool.listener import BaseAIToolListener
from agenterprise.model.listener.entity.listener import BaseAIEntityListener


class Project():

    def __init__(self, ai_techstack: AIURN, service_techstack: AIURN, data_techstack: AIURN, target_dir: str, envid: str = None, dsl_file: str = None):
        self.ai_techstack = ai_techstack
        self.service_techstack = service_techstack
        self.data_techstack = data_techstack
        self.project_layer = service_techstack
        self.project_build_id = envid
        self.target_dir = target_dir
        self.dsl_file = dsl_file

        self.projectlistener = NonFunctionalListener
        self.agentlistener = BaseAIAgentListener
        self.llmlistener = BaseAILLMListener
        self.servicelistener = BasicServiceListener
        self.toollistener = BaseAIToolListener
        self.entitylistener = BaseAIEntityListener

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
    def get_entitylayer(self):
        return self.data_techstack.to_url()    
