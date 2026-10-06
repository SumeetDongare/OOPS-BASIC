import numpy as np
import pandas as pd

# Create NumPy array of mobile prices
prices = np.array([15000, 25000, 32000, 45000, 28000, 55000])

# Calculate statistics
mean_price = np.mean(prices)
median_price = np.median(prices)
max_price = np.max(prices)
min_price = np.min(prices)

print("Mean Price:", mean_price)
print("Median Price:", median_price)
print("Maximum Price:", max_price)
print("Minimum Price:", min_price)

# Create Pandas DataFrame
mobiles = ["Mobile 1", "Mobile 2", "Mobile 3",
           "Mobile 4", "Mobile 5", "Mobile 6"]

df = pd.DataFrame({
    "Mobile": mobiles,
    "Price": prices
})

print("\nMobile Details:")
print(df)

# Display mobiles costing more than ₹30,000
print("\nMobiles costing more than ₹30,000:")
print(df[df["Price"] > 30000])

"""
Output:-
Mean Price: 33333.333333333336
Median Price: 30000.0
Maximum Price: 55000
Minimum Price: 15000

Mobile Details:
     Mobile  Price
0  Mobile 1  15000
1  Mobile 2  25000
2  Mobile 3  32000
3  Mobile 4  45000
4  Mobile 5  28000
5  Mobile 6  55000

Mobiles costing more than ₹30,000:
     Mobile  Price
2  Mobile 3  32000
3  Mobile 4  45000
5  Mobile 6  55000
"""