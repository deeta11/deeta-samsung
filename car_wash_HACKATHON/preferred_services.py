import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('deeta-samsung/car_wash_HACKATHON/car_wash_datasetcsv.csv')

service_counts = df['Preferred Service'].value_counts()

plt.figure(figsize=(10, 6))
service_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Preferred Services', fontsize=16)
plt.xlabel('Service Type', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
