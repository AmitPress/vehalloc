from fastapi import FastAPI

async def check_existance_employee(app: FastAPI, employee_id: str):
    result = await app.mongodb["employees"].find_one({"employee_id": employee_id})
    if result:
        return True
    else:
        return False
async def check_existance_vehicle(app: FastAPI, vehicle_id: str):
    result = await app.mongodb["vehicles"].find_one({"vehicle_id": vehicle_id})
    if result:
        return True
    else:
        return False
async def check_existance_driver(app: FastAPI, driver_id: str):
    result = await app.mongodb["drivers"].find_one({"driver_id": driver_id})
    if result:
        return True
    else:
        return False
async def check_existance_allocation(app: FastAPI, allocation_id: str):
    result = await app.mongodb["allocations"].find_one({"allocation_id": allocation_id})
    if result:
        return True
    else:
        return False