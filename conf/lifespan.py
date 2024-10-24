from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI, HTTPException

# import the environment files
from conf.settings import env
# import the logger
from conf.logger import logger

# setup configuration before running the application
async def set_db_client(app: FastAPI):
    """
    Initializing db connection before the application starts
    taking requests.
    """
    try:
        client = AsyncIOMotorClient(env.CONNECTION_STRING)
        logger.info("Connected Successfully")
    except:
        raise HTTPException(status_code=500, detail="Failed To Connect To The MongoDB Server")
    app.mongodb_client = client
    app.mongodb        = app.mongodb_client.get_database(env.DB_NAME)
    logger.info(f"Database[{env.DB_NAME}] Created Successfully")

async def unset_db_client(app: FastAPI):
    """
    Destroying the connection to free up resources
    """
    app.mongodb_client.close()
    logger.info("Connection Closed Successfully")

async def lifespan(app: FastAPI):
    await set_db_client(app=app)
    yield
    await unset_db_client(app=app)
