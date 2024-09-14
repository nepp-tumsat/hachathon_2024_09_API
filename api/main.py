from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import task, done

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# @app.get("/hello")
# async def hello():
#     return {"Hello": "World"}
