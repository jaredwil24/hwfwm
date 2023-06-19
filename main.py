from fastapi import FastAPI
from controller.index import user
app = FastAPI()
app.include_router(user)
