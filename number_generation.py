import random
import pandas as pd

def generate_random_parameters(num_samples=100000):
    """
    Generates a dataset of random values based on the given parameter ranges.
    
    Parameters:
    num_samples (int): Number of samples to generate.
    
    Returns:
    pd.DataFrame: A DataFrame containing parameter names and their corresponding random values.
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
    
    data = []
    for _ in range(num_samples):
        sample = {param: round(random.uniform(low, high), 3) for param, (low, high) in ranges.items()}
        data.append(sample)
    
    return pd.DataFrame(data)

# Example usage:
if __name__ == "__main__":
    num_samples = int(input("Enter number of samples to generate: "))
    save_path = input("Enter file path to save dataset (including filename): ")
    dataset = generate_random_parameters(num_samples)
    dataset.to_csv(save_path, index=False)
    print(f"Generated dataset with {num_samples} samples saved as '{save_path}'")
