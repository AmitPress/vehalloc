from pydantic import BaseModel
from datetime import datetime

class TimeStampedSchemaMixin(BaseModel):
    created_at: datetime
    updated_at: datetime 