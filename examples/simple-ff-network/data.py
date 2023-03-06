import numpy as np


def load_data(csv_path):
        # Load data from the CSV file.
        data = np.loadtxt(csv_path, delimiter=",")
        
        # Split data between input (first 8 columns) and output (last column).
        # Input.
        X = data[:, 0:8]
        # Output.
        y = data[:, 8]

        return X, y
