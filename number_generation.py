import random

def generate_random_parameters():
    """
    Generates a set of 9 random values based on the given parameter ranges.
    
    Returns:
    dict: A dictionary containing parameter names and their corresponding random values.
    """
    ranges = {
        "Ammonia": (0.00, 5.00),
        "Nitrite": (0.00, 5.00),
        "pH": (0, 12),
        "Alkalinity": (0, 18),
        "Magnesium": (800, 1500),
        "Calcium": (200, 500),
        "Phosphate": (0.00, 3.00),
        "Nitrate": (0.00, 200.00),
        "Salinity": (1.000, 1.050)
    }
    
    generated_values = {}
    for param, (low, high) in ranges.items():
        generated_values[param] = round(random.uniform(low, high), 3)
    
    return generated_values

# Example usage:
if __name__ == "__main__":
    random_parameters = generate_random_parameters()
    print("Generated parameters:")
    for param, value in random_parameters.items():
        print(f"{param}: {value}")
