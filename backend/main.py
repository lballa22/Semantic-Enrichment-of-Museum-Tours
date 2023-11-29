from fastapi import FastAPI
from routers import artwork_router

app = FastAPI()

app.include_router(artwork_router.router)
