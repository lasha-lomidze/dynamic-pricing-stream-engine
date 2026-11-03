import random
from config import ONLINE_DRIVER_COUNT, ONLINE_USER_COUNT, ROUTES

API_CALLS = list(ROUTES)


def random_user_id():
    return random.randint(1, ONLINE_USER_COUNT)


def random_driver_id():
    return random.randint(1, ONLINE_DRIVER_COUNT)


def create_random_user():
    uid = random_user_id()
    return {"id": uid, "name": f"user_{uid}", "email": f"user_{uid}@example.com"}


def create_random_driver():
    did = random_driver_id()
    return {"id": did, "name": f"driver_{did}", "email": f"driver_{did}@example.com"}


def random_api_call():
    return random.choice(API_CALLS)