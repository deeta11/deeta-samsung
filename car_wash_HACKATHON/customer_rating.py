import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('car_wash_analytics_dataset_with_maintenance_frequency.csv')

# Plot histogram of customer ratings
plt.figure(figsize=(10, 6))
plt.hist(df['Customer Rating'], bins=5, color='orange', edgecolor='black')
plt.title('Customer Ratings Distribution', fontsize=16)
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.xticks(range(1, 6))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
