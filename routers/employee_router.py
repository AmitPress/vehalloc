from fastapi import FastAPI, APIRouter, Depends, Response

from schemas.employee_schema import EmployeeSchema
from repos.employee_repo import insert_employee
from conf.app import get_app_instance
from utils.response_builder import build_response

router = APIRouter()

# Insert a new employee
@router.post("/employees")
async def create_employee_endpoint(employee: EmployeeSchema, app: FastAPI = Depends(get_app_instance)):
    employee = await insert_employee(app, employee)
    return build_response(employee, status_code=201)