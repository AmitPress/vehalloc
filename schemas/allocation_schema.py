from utils.timestamped_schema import TimeStampedSchemaMixin
from datetime import date
class AllocationSchema(TimeStampedSchemaMixin):
    employee_id: str
    vehicle_id: str 
    driver_id: str
    allocated_date: date