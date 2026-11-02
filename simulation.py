import os
import time 
import requests

# ==========================================
# DOCKER-READY NETWORK CONFIGURATION
# ==========================================
# Inside Docker Compose, containers communicate using the service name as the domain name.
# We default to 'http://web:8000' but fall back to localhost if running outside Docker.
BASE_URL =  "http://localhost:8000"

# Using a Session is the industry standard for performance.
# It reuses the underlying TCP connection across all your route calls.
session = requests.Session()

ROUTES = {
    # Users
    "add_user": lambda data: session.post(f"{BASE_URL}/users", json=data),
    "get_user": lambda uid: session.get(f"{BASE_URL}/users/{uid}"),
    
    # Drivers
    "add_driver": lambda data: session.post(f"{BASE_URL}/drivers", json=data),
    "get_driver": lambda did: session.get(f"{BASE_URL}/drivers/{did}"),
    
    # Rides
    "estimate": lambda p, d: session.get(f"{BASE_URL}/rides/estimate", params={"pickup": p, "dropoff": d}),
    "request": lambda data: session.post(f"{BASE_URL}/rides", json=data),
    "list": lambda s="pending": session.get(f"{BASE_URL}/rides", params={"status": s}),
    "status": lambda rid: session.get(f"{BASE_URL}/rides/{rid}"),
    "cancel": lambda rid: session.delete(f"{BASE_URL}/rides/{rid}"),
    "accept": lambda rid, did: session.post(f"{BASE_URL}/rides/{rid}/accept", params={"driver_id": did}),
    "deny": lambda rid: session.post(f"{BASE_URL}/rides/{rid}/deny")
}



def simulation():
    for i in range(10):
        time.sleep(0.5)
        ROUTES["add_user"]({"name": f"user_{i}", "email": f"user_{i}@example.com"})
        time.sleep(0.5)
        ROUTES["add_driver"]({"name": f"driver_{i}", "email": f"driver_{i}@example.com"})

simulation()