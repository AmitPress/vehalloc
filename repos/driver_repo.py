from fastapi import FastAPI
from conf.settings import env
from conf.logger import logger
from schemas.driver_schema import DriverSchema

# Make a COLLECTION called driver
DRIVER_COLLECTION="drivers"

async def create_driver(app: FastAPI, driver: DriverSchema) -> None:
    try:
        result = await app.mongodb[DRIVER_COLLECTION].insertOne(driver.model_dump())
    except Exception as e:
        logger.exception(f"Failed To Create Driver With Exception: {str(e)}")
    inserted_driver = await app.mongodb[DRIVER_COLLECTION].find_one({"_id": result.inserted_id})
    return inserted_driver