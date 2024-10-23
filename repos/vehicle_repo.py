from fastapi import FastAPI
from conf.logger import logger
from schemas.vehicle_schema import VehicleSchema
from bson import ObjectId

# Make a COLLECTION called vehicle
VEHICLE_COLLECTION = "vehicles"

# insert vehicle data
async def insert_vehicle(app: FastAPI, vehicle: VehicleSchema):
    try:
        vehicle_dict = vehicle.model_dump()
        result = await app.mongodb[VEHICLE_COLLECTION].insert_one(vehicle_dict)
    except Exception as e:
        logger.error(f"Error inserting vehicle: {e}")
        return None
    data = {
        "id": result.inserted_id,
        **vehicle_dict
    }
    return data

async def get_vehicle(app: FastAPI, vehicle_id: str):
    try:
        result = await app.mongodb[VEHICLE_COLLECTION].find_one({"_id": ObjectId(vehicle_id)})
    except Exception as e:
        logger.error(f"Error getting vehicle: {e}")
        return None
    return result

async def get_vehicles(app: FastAPI):
    try:
        results = await app.mongodb[VEHICLE_COLLECTION].find().to_list(length=100)
    except Exception as e:
        logger.error(f"Error getting vehicles: {e}")
        return None
    return results
