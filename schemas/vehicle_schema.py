from utils.timestamped_schema import TimeStampedSchemaMixin
from enum import Enum

class VehicleType(str, Enum):
    car         = "car"
    # tempo       = "tempo" # lets keep it simple for now
    # bus         = "bus"
    # bike        = "bike"
    # microbus    = "microbus"

class VehicleSchema(TimeStampedSchemaMixin):
    name: str
    registration: str 
    vehicle_type: VehicleType
    driver_id: str # this will be filled when driver is just created above in the same context