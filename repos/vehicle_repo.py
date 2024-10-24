from fastapi import FastAPI, HTTPException
from conf.logger import logger
from optim.existance_checker import check_existance_driver
from schemas.vehicle_schema import VehicleSchema
from bson import ObjectId

# Make a COLLECTION called vehicle
VEHICLE_COLLECTION = "vehicles"

# insert vehicle data
async def insert_vehicle(app: FastAPI, vehicle: VehicleSchema):
    try:
        if not await check_existance_driver(app, vehicle.driver_id):
            logger.error(f"Driver with id {vehicle.driver_id} does not exist")
            raise HTTPException(detail="Driver does not exist", status_code=404)
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
