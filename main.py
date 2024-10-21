from fastapi import FastAPI
from conf.lifespan import lifespan
app = FastAPI(lifespan=lifespan)