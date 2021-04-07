from fastapi import FastAPI
from src.routers import health
import uvicorn

app = FastAPI()
app.include_router(health.router)

if __name__ == '__main__':
    uvicorn.run(app, port=8080)
