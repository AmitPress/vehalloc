from pydantic import BaseModel, Field
from datetime import datetime

class TimeStampedSchemaMixin(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
