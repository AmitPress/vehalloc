from fastapi import FastAPI
from conf.logger import logger
from schemas.driver_schema import DriverSchema
from bson import ObjectId

# Make a COLLECTION called driver
DRIVER_COLLECTION="drivers"

# insert driver data
async def insert_driver(app: FastAPI, driver: DriverSchema):
    try:
        driver_dict = driver.model_dump()
        result = await app.mongodb[DRIVER_COLLECTION].insert_one(driver_dict)
    except Exception as e:
        logger.error(f"Error inserting driver: {e}")
        return None
    data = {
        "id": result.inserted_id,
        **driver_dict
    }
    return data

async def get_driver(app: FastAPI, driver_id: str):
    try:
        result = await app.mongodb[DRIVER_COLLECTION].find_one({"_id": ObjectId(driver_id)})
    except Exception as e:
        logger.error(f"Error getting driver: {e}")
        return None
    return result

async def get_drivers(app: FastAPI):
    try:
        results = await app.mongodb[DRIVER_COLLECTION].find().to_list(length=100)
    except Exception as e:
        logger.error(f"Error getting drivers: {e}")
        return None
    return results