import os
from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

class AIURN(str):
    def __init__(self, urn: str):
        self.urn = urn
        self.parts = urn.split(':')
        if len(self.parts) < 3 or self.parts[0] != 'aiurn':
            raise ValueError(f"Invalid AIURN format: {urn}")
        self.namespace = self.parts[2]
        self.resource = self.parts[3] if len(self.parts) > 3 else None
        self.subresource = self.parts[4] if len(self.parts) > 4 else None

    def to_filepath(self):
        path = os.path.join(*self.parts[2:])
        return path
    
    def to_varname(self):
        return '_'.join(self.parts[2:]).replace('-', '_')
    
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: type, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        # Validate as string, then convert to aiurn instance
        return core_schema.no_info_after_validator_function(
            cls,  # Constructor
            core_schema.str_schema(),  # Expect string input
        )
    
