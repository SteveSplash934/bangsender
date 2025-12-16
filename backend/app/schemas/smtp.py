from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from uuid import UUID

# Shared properties
class SMTPBase(BaseModel):
    name: str = Field(..., description="Friendly name, e.g. 'Gmail Marketing'")
    host: str = Field(..., description="smtp.gmail.com")
    port: int = Field(587, description="Usually 587 or 465")
    username: str
    security: str = Field("TLS", pattern="^(TLS|SSL|NONE)$")
    is_active: bool = True

class SMTPCreate(SMTPBase):
    password: str 

class SMTPUpdate(BaseModel):
    name: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    username: Optional[str] = None
    password: Optional[str] = None
    security: Optional[str] = None
    is_active: Optional[bool] = None

class SMTPResponse(SMTPBase):
    id: UUID  # Changed from int to UUID
    created_at: datetime
    # No password returned

    model_config = ConfigDict(from_attributes=True)