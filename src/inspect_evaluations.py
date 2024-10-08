import numpy as np
import pandas as pd

# Load the .npz file
file_path = 'logs/results/evaluations.npz'
data = np.load(file_path)

# Inspect the contents
print("Keys in the .npz file:", data.files)

# Export each key's data to a separate CSV file
for key in data.files:
    print(f"\nData for key '{key}':")
    
    # Convert the data to a DataFrame
    df = pd.DataFrame(data[key])
    
    # Save the DataFrame to a CSV file
    csv_file_path = f'logs/results/{key}.csv'
    df.to_csv(csv_file_path, index=False)
    print(f"Data for key '{key}' exported to {csv_file_path}")