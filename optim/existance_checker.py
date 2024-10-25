from fastapi import FastAPI
from bson import ObjectId
async def check_existance_employee(app: FastAPI, employee_id: str):
    result = await app.mongodb["employees"].find_one({"_id": ObjectId(employee_id)})
    if result:
        return True
    else:
        return False
async def check_existance_vehicle(app: FastAPI, vehicle_id: str):
    result = await app.mongodb["vehicles"].find_one({"_id": ObjectId(vehicle_id)})
    if result:
        return True
    else:
        return False
async def check_existance_driver(app: FastAPI, driver_id: str):
    result = await app.mongodb["drivers"].find_one({"_id": ObjectId(driver_id)})
    if result:
        return True
    else:
        return False
async def check_existance_allocation(app: FastAPI, allocation_id: str):
    result = await app.mongodb["allocations"].find_one({"_id": ObjectId(allocation_id)})
    if result:
        return True
    else:
        return False