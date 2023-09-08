from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.index import user
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:8000',
        'http://localhost:5173',
        ],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


app.include_router(user)

#if __name__ == '__main__':
#    uvicorn.run(app, host="127.0.0.1", port=5049)
