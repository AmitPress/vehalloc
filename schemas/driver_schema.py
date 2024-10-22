from utils.timestamped_schema import TimeStampedSchemaMixin
from pydantic import BaseModel

class DriverSchema(BaseModel, TimeStampedSchemaMixin):
    name: str
    driving_license: str 
    verified: bool 