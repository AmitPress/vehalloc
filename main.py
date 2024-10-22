from fastapi import FastAPI
from conf.lifespan import lifespan
from routers import base
app = FastAPI(lifespan=lifespan)
# app.include_router(base.router, prefix="/v1")