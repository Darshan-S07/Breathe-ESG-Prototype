def normalize_unit(quantity, unit):

    unit = unit.lower()

    conversions = {
        "gal": ("liters", 3.785),
        "gallons": ("liters", 3.785),
        "mwh": ("kwh", 1000),
    }

    if unit in conversions:

        target_unit, factor = conversions[unit]

        return quantity * factor, target_unit

    return quantity, unit


def classify_scope(activity_type):

    if activity_type == "fuel":
        return "SCOPE1"

    elif activity_type == "electricity":
        return "SCOPE2"

    return "SCOPE3"


def calculate_emissions(activity_type, quantity):

    factors = {
        "fuel": 2.31,
        "electricity": 0.82,
        "flight": 0.15,
        "hotel": 10,
    }

    factor = factors.get(activity_type, 1)

    return factor, quantity * factor


def is_suspicious(activity_type, quantity):

    thresholds = {
        "fuel": 5000,
        "electricity": 50000,
        "flight": 15000,
        "hotel": 30,
    }

    threshold = thresholds.get(activity_type, 10000)

    return quantity > threshold