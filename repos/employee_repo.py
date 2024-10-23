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