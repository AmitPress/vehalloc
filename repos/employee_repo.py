from fastapi import FastAPI
from conf.logger import logger
from schemas.employee_schema import EmployeeSchema
from bson import ObjectId

# Make a COLLECTION called employee
EMPLOYEE_COLLECTION = "employees"

# insert employee data
async def insert_employee(app: FastAPI, employee: EmployeeSchema):
    try:
        employee_dict = employee.model_dump()
        result = await app.mongodb[EMPLOYEE_COLLECTION].insert_one(employee_dict)
    except Exception as e:
        logger.error(f"Error inserting employee: {e}")
        return None
    data = {
        "id": result.inserted_id,
        **employee_dict
    }
    return data
async def get_employee(app: FastAPI, employee_id: str):
    try:
        result = await app.mongodb[EMPLOYEE_COLLECTION].find_one({"_id": ObjectId(employee_id)})
    except Exception as e:
        logger.error(f"Error getting employee: {e}")
        return None
    return result
async def get_employees(app: FastAPI):
    try:
        results = await app.mongodb[EMPLOYEE_COLLECTION].find().to_list(length=100)
    except Exception as e:
        logger.error(f"Error getting employees: {e}")
        return None
    return results