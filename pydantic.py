from pydantic import BaseModel

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
