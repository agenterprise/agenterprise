import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.router import Router
from app.middleware.http import HttpMiddleware


app = FastAPI(title="AI-Environment {{cookiecutter.project_name}}", version="0.1.0")
middleware = HttpMiddleware(app)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
router = Router(app=app)

def main():
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=9000, env_file=".env", log_level="info")

if __name__ == "__main__":
    main()