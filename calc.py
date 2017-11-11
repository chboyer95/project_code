def wind_speed(u, v, w):
    """Calculates wind speed from u, v, and w components."""
    w = 0
    return (u * u + v * v + w * w)

def calc():
    return 5

def get_wind_direction(u, v):
    return 90 - atan2(u, v)
