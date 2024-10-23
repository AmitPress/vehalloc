from fastapi import FastAPI, APIRouter, Depends, Response

from schemas.driver_schema import DriverSchema
from repos.driver_repo import insert_driver
from conf.app import get_app_instance
from utils.response_builder import build_response
router = APIRouter()

# insert a new driver
@router.post("/drivers")
async def create_driver_endpoint(driver: DriverSchema, response: Response, app: FastAPI = Depends(get_app_instance)):
    driver = await insert_driver(app, driver)
    return build_response(driver, status_code=201)