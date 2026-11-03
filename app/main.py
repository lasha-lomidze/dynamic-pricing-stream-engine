from fastapi import FastAPI, HTTPException

app = FastAPI(title="dpse")


def not_implemented():
    raise HTTPException(status_code=501, detail="yet to implement")


# ================= users
@app.post("/users", status_code=201)
def register_user():
    not_implemented()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    not_implemented()


# ================= drivers
@app.post("/drivers", status_code=201)
def register_driver():
    not_implemented()


@app.get("/drivers/{driver_id}")
def get_driver(driver_id: int):
    not_implemented()


# ================= rides
# NOTE: /rides/estimate must stay ABOVE /rides/{ride_id},
# otherwise "estimate" gets matched as a ride_id.
@app.get("/rides/estimate")
def estimate_prices(pickup: str, dropoff: str):
    not_implemented()


@app.post("/rides", status_code=201)
def request_ride():
    not_implemented()


@app.get("/rides")
def list_ride_requests(status: str = "pending"):
    # used by drivers to see open requests
    not_implemented()


@app.get("/rides/{ride_id}")
def get_ride_status(ride_id: int):
    not_implemented()


@app.delete("/rides/{ride_id}")
def cancel_ride(ride_id: int):
    not_implemented()


@app.post("/rides/{ride_id}/accept")
def accept_ride(ride_id: int):
    not_implemented()


@app.post("/rides/{ride_id}/deny")
def deny_ride(ride_id: int):
    not_implemented()