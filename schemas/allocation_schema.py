from utils.timestamped_schema import TimeStampedSchemaMixin
from datetime import date
class AllocationSchema(TimeStampedSchemaMixin):
    employee_id: str
    vehicle_id: str = None
    allocated_date: date