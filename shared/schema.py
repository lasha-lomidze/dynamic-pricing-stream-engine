from shared.schema import BaseModel

# ^ pydantic-like schema 

class Location(BaseModel):
    latitude: float
    longitude: float

class User(BaseModel):
    id: int
    location: Location

class Driver(BaseModel):
    id: int
    location: Location
    drive_tier: str

# ^ enums and other 

from enum import StrEnum

class DriveTier(StrEnum):
    ECONOMY = "economy"
    PREMIUM = "premium"