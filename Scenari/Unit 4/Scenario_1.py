import numpy as np
import pandas as pd

# Create NumPy array of treatment costs
costs = np.array([15000, 25000, 18000, 30000, 22000, 12000])

# Calculate statistics
mean_cost = np.mean(costs)
max_cost = np.max(costs)
min_cost = np.min(costs)

print("Mean Treatment Cost:", mean_cost)
print("Maximum Treatment Cost:", max_cost)
print("Minimum Treatment Cost:", min_cost)

# Create Pandas DataFrame
patients = ["Patient 1", "Patient 2", "Patient 3",
            "Patient 4", "Patient 5", "Patient 6"]

df = pd.DataFrame({
    "Patient": patients,
    "Treatment Cost": costs
})

print("\nPatient Treatment Details:")
print(df)

# Display patients whose cost exceeds ₹20,000
print("\nPatients with treatment cost above ₹20,000:")
print(df[df["Treatment Cost"] > 20000])