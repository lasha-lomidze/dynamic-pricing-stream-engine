
from shared.schema import DriveTier

ONLINE_USER_COUNT = 10
ONLINE_DRIVER_COUNT = 10
DRIVE_TYPES = ["economy", "premium"]

drive_tier_weights = {
    DriveTier.ECONOMY: 0.7,
    DriveTier.PREMIUM: 0.3
}