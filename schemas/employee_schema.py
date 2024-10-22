from utils.timestamped_schema import TimeStampedSchemaMixin
from pydantic import Field
from datetime import datetime
from enum import Enum
# from uuid import UUID, uuid4

class Position(Enum):
    developer   = "developer"
    admin       = "admin"
    manager     = "manager"
    peon        = "peon"
    finance     = "finance"
class AllocationStatus(Enum):
    unallocated = "unallocated"
    allocated   = "allocated"

class EmployeeSchema(TimeStampedSchemaMixin):
    # service_id: UUID = Field(default_factory=uuid4) # as of now lets ignore this for simplicity
    name: str
    age: int = Field(..., gt=0, le=100)
    inducted: datetime
    position: Position
    vehicle_alloc_status: AllocationStatus
