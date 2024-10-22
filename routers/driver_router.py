from fastapi import FastAPI, APIRouter

from schemas.driver_schema import DriverSchema

router = APIRouter()

# Create Driver
@router.post("/driver", response_model=DriverSchema)
async def create_driver(app: FastAPI, driver: DriverSchema):
    driver = create_driver(app=app, driver=driver)
    return driver