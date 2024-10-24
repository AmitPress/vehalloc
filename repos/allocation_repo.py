from fastapi import FastAPI, HTTPException
from conf.logger import logger
from optim.existance_checker import check_existance_employee
from schemas.allocation_schema import AllocationSchema
from bson import ObjectId
from datetime import date 
ALLOCATION_COLLECTION="allocations"

async def insert_allocation(app: FastAPI, allocation: AllocationSchema):
    try:
        if not (await check_existance_employee(app, allocation.employee_id)):
            logger.error(f"Employee or vehicle does not exist")
            raise HTTPException(status_code=400, detail="Employee or vehicle does not exist")
        if allocation.allocated_date <= date.today():
            raise HTTPException(status_code=400, detail="Allocated date cannot be in the past")
        # TODO: check if employee is already allocated to a vehicle on a date

        # TODO: get an available vehicle randomly

        allocation_dict = allocation.model_dump()
        result = await app.mongodb[ALLOCATION_COLLECTION].insert_one(allocation_dict)
    except Exception as e:
        logger.error(f"Error inserting allocation: {e}")
        return None
    data = {
        "id": result.inserted_id,
        **allocation_dict
    }
    return data

async def get_allocation(app: FastAPI, allocation_id: str):
    try:
        result = await app.mongodb[ALLOCATION_COLLECTION].find_one({"_id": ObjectId(allocation_id)})
    except Exception as e:
        logger.error(f"Error getting allocation: {e}")
        return None
    return result

async def get_allocations(app: FastAPI):
    try:
        results = app.mongodb[ALLOCATION_COLLECTION].find()
    except Exception as e:
        logger.error(f"Error getting allocations: {e}")
        return None
    return results

async def update_allocation(app: FastAPI, allocation_id: str, allocation: AllocationSchema):
    try:
        allocation_dict = allocation.model_dump()
        result = await app.mongodb[ALLOCATION_COLLECTION].update_one({"_id": ObjectId(allocation_id)}, {"$set": allocation_dict})
    except Exception as e:
        logger.error(f"Error updating allocation: {e}")
        return None
    if result.modified_count == 1:
        return True
    return False

async def delete_allocation(app: FastAPI, allocation_id: str):
    try:
        result = await app.mongodb[ALLOCATION_COLLECTION].delete_one({"_id": ObjectId(allocation_id)})
    except Exception as e:
        logger.error(f"Error deleting allocation: {e}")
        return None
    if result.deleted_count == 1:
        return True
    return False