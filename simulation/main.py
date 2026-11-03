import random
import time 
import simulation.lib as lib
import requests
from enum import StrEnum
from shared.schema import DriveTier
import simulation.config as config

drive_tier_weights = config.drive_tier_weights




BASE_URL =  "http://localhost:8000"
ROUTES = config.ROUTES
ONLINE_USER_COUNT = config.ONLINE_USER_COUNT
ONLINE_DRIVER_COUNT = config.ONLINE_DRIVER_COUNT
DRIVE_TYPES = config.DRIVE_TYPES


class DriveTier(StrEnum):
    ECONOMY = "economy"
    PREMIUM = "premium"


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