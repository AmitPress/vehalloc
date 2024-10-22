from fastapi import FastAPI
from conf.lifespan import lifespan
from routers import driver_router
app = FastAPI(lifespan=lifespan)
app.include_router(driver_router.router, prefix="/v1")