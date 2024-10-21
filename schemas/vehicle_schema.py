from utils.timestamped_schema import TimeStampedSchemaMixin
from utils.common_options import AvailibiltyStatus
from pydantic import BaseModel
from enum import Enum

class VehicleType(Enum):
    car         = "car"
    tempo       = "tempo"
    bus         = "bus"
    bike        = "bike"
    microbus    = "microbus"

class VehicleSchema(BaseModel, TimeStampedSchemaMixin):
    name: str
    registration: str 
    driver_id: str = None
    vehicle_type: VehicleType
    availability_status: AvailibiltyStatus