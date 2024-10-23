from fastapi import FastAPI, APIRouter, Depends, Response

from schemas.employee_schema import EmployeeSchema
from repos.employee_repo import insert_employee, get_employee, get_employees
from conf.app import get_app_instance
from utils.response_builder import build_response

router = APIRouter()

# Insert a new employee
@router.post("/employees")
async def create_employee_endpoint(employee: EmployeeSchema, app: FastAPI = Depends(get_app_instance)):
    employee = await insert_employee(app, employee)
    return build_response(employee, status_code=201)
@router.get("/employees")
async def get_employees_endpoint(app: FastAPI = Depends(get_app_instance)):
    employees = await get_employees(app)
    return build_response(employees)
@router.get("/employees/{employee_id}") 
async def get_employee_endpoint(employee_id: str, app: FastAPI = Depends(get_app_instance)):
    employee = await get_employee(app, employee_id)
    return build_response(employee)