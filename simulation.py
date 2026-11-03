import random
import time 
import requests
from enum import StrEnum

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



# ^ CONSTANTS AND CONFIGURATION

ONLINE_USER_COUNT = 10
ONLINE_DRIVER_COUNT = 10
DRIVE_TYPES = ["economy", "premium"]

class DriveTier(StrEnum):
    ECONOMY = "economy"
    PREMIUM = "premium"

drive_tier_weights = {
    DriveTier.ECONOMY: 0.7,
    DriveTier.PREMIUM: 0.3
}



# ^ HELPER FUNCTIONS

def random_user_id():
    return random.randint(1, ONLINE_USER_COUNT)

def random_driver_id():
    return random.randint(1, ONLINE_DRIVER_COUNT)

def create_random_user():
    uid = random_user_id()
    return {"name": f"user_{uid}", "email": f"user_{uid}@example.com"}

def create_random_driver():
    did = random_driver_id()
    return {"name": f"driver_{did}", "email": f"driver_{did}@example.com"}

def random_api_call():
    api_calls = list(ROUTES.keys())
    return random.choice(api_calls)



# ^ SIMULATION FUNCTION

# def simulation():
#     while True:
#         time.sleep(10 / (ONLINE_USER_COUNT + ONLINE_DRIVER_COUNT/2))

#         api_call = random_api_call()
#         if api_call == "add_user":
#             ROUTES["add_user"]({"name": f"user_{random.randint(1, ONLINE_USER_COUNT)}", "email": f"user_{random.randint(1, ONLINE_USER_COUNT)}@example.com"})
#         elif api_call == "add_driver":
#             ROUTES["add_driver"]({"name": f"driver_{random.randint(1, ONLINE_DRIVER_COUNT)}", "email": f"driver_{random.randint(1, ONLINE_DRIVER_COUNT)}@example.com"})
#         elif api_call == "get_user":
#             ROUTES["get_user"](random_user_id())
#         elif api_call == "get_driver":
#             ROUTES["get_driver"](random_driver_id())
#         elif api_call == "estimate":
#             ROUTES["estimate"](f"pickup_{random.randint(1, 100)}", f"dropoff_{random.randint(1, 100)}")
#         elif api_call == "request":
#             ROUTES["request"]({"user_id": random_user_id(), "pickup": f"pickup_{random.randint(1, 100)}", "dropoff": f"dropoff_{random.randint(1, 100)}"})
#         elif api_call == "list":
#             ROUTES["list"]()
#         elif api_call == "status":
#             ROUTES["status"](random.randint(1, 100))
#         elif api_call == "cancel":
#             ROUTES["cancel"](random.randint(1, 100))
#         elif api_call == "accept":
#             ROUTES["accept"](random.randint(1, 100), random_driver_id())
#         elif api_call == "deny":
#             ROUTES["deny"](random.randint(1, 100))

# simulation()