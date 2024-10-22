from utils.timestamped_schema import TimeStampedSchemaMixin
from utils.common_options import AvailibiltyStatus
from pydantic import BaseModel
from enum import Enum

class VehicleType(Enum):
    car         = "car"
    # tempo       = "tempo"
    # bus         = "bus"
    # bike        = "bike"
    # microbus    = "microbus"

class VehicleSchema(TimeStampedSchemaMixin):
    name: str
    registration: str 
    vehicle_type: VehicleType