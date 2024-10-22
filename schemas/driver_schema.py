from utils.timestamped_schema import TimeStampedSchemaMixin

class DriverSchema(TimeStampedSchemaMixin):
    name: str
    driving_license: str 
    verified: bool 