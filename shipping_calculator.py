def calculate_shipping_cost(weight, zone):
    base_price = 5.0
    zone_multipliers = {
        'A': 1.0,
        'B': 1.5,
        'C': 2.0
    }
    if zone not in zone_multipliers:
        raise ValueError("Invalid shipping zone.")
    return base_price + (weight * zone_multipliers[zone])

if __name__ == "__main__":
    weight = float(input("Enter package weight (kg): "))
    zone = input("Enter shipping zone (A, B, or C): ").upper()
    try:
        cost = calculate_shipping_cost(weight, zone)
        print(f"Shipping cost: ₹{cost:.2f}")
    except ValueError as e:
        print(e)
