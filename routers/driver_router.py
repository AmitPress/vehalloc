from typing import Annotated
from fastapi import FastAPI, APIRouter, Depends, Response

from schemas.driver_schema import DriverSchema
from repos.driver_repo import create_driver
from conf.app import get_app_instance
router = APIRouter()

# Create Driver
@router.post("/driver", response_model=DriverSchema)
async def create_driver_api(driver: DriverSchema, app: FastAPI = Depends(get_app_instance)):
    driver = await create_driver(app=app, driver=driver)
    return driver