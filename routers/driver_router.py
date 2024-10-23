from fastapi import FastAPI, APIRouter, Depends, Response

from schemas.driver_schema import DriverSchema
from repos.driver_repo import get_drivers, insert_driver, get_driver
from conf.app import get_app_instance
from utils.response_builder import build_response
router = APIRouter()

# insert a new driver
@router.post("/drivers")
async def create_driver_endpoint(driver: DriverSchema, app: FastAPI = Depends(get_app_instance)):
    driver = await insert_driver(app, driver)
    return build_response(driver, status_code=201)

@router.get("/drivers")
async def get_drivers_endpoint(response: Response, app: FastAPI = Depends(get_app_instance)):
    drivers = await get_drivers(app)
    return build_response(drivers, status_code=200)
@router.get("/drivers/{driver_id}")
async def get_driver_endpoint(driver_id: str, response: Response, app: FastAPI = Depends(get_app_instance)):
    driver = await get_driver(app, driver_id)
    return build_response(driver, status_code=200)