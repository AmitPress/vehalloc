from utils.timestamped_schema import TimeStampedSchemaMixin
from utils.common_options import AvailibiltyStatus
from pydantic import BaseModel

class DriverSchema(BaseModel, TimeStampedSchemaMixin):
    name: str
    driving_license: str 
    verified: bool 
    availability_status: AvailibiltyStatus