import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('car_wash_analytics_dataset_with_maintenance_frequency.csv')

# Count repeat vs new customers
visit_counts = df['Frequency of Visit'].value_counts()

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(visit_counts, labels=visit_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.title('Frequency of Visits', fontsize=16)
plt.show()
