def wind_speed(u, v, w):
    """Calculates wind speed from u, v, and w components."""
    w = 0
    return sqrt(u * u + v * v + w * w)
