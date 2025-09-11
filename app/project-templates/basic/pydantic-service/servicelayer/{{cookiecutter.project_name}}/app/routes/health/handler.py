from typing import Final
from fastapi import Request

async def handle_health(request: Request):
   return {"status": "healthy"}