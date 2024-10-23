from fastapi import FastAPI, APIRouter, Depends, Response

from schemas.vehicle_schema import VehicleSchema
from repos.vehicle_repo import get_vehicles, insert_vehicle, get_vehicle
from conf.app import get_app_instance
from utils.response_builder import build_response

router = APIRouter()

# Insert a new vehicle
@router.post("/vehicles")
async def create_vehicle_endpoint(vehicle: VehicleSchema, app: FastAPI = Depends(get_app_instance)):
    vehicle = await insert_vehicle(app, vehicle)
    return build_response(vehicle, status_code=201)

@router.get("/vehicles")
async def get_vehicles_endpoint(response: Response, app: FastAPI = Depends(get_app_instance)):
    vehicles = await get_vehicles(app)
    return build_response(vehicles, status_code=200)

@router.get("/vehicles/{vehicle_id}")
async def get_vehicle_endpoint(vehicle_id: str, response: Response, app: FastAPI = Depends(get_app_instance)):
    vehicle = await get_vehicle(app, vehicle_id)
    return build_response(vehicle, status_code=200)