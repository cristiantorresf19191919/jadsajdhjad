from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Property(BaseModel):
    id: Optional[int] = None
    name: str
    address: str
    price_range: str
    rooms: int
    bathrooms: int
    area_m2: float
    location: str
    description: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class PropertyCreate(BaseModel):
    name: str
    address: str
    price_range: str
    rooms: int
    bathrooms: int
    area_m2: float
    location: str
    description: str

class PropertyUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    price_range: Optional[str] = None
    rooms: Optional[int] = None
    bathrooms: Optional[int] = None
    area_m2: Optional[float] = None
    location: Optional[str] = None
    description: Optional[str] = None 