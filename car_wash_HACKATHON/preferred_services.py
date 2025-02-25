import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('deeta-samsung/car_wash_HACKATHON/car_wash_datasetcsv.csv')

service_counts = df['Service'].value_counts()

plt.figure(figsize=(10, 6))
ax = service_counts.plot(kind='bar', color=['skyblue', 'lightcoral', 'lightgreen', 'lightpink', 'lightskyblue'], edgecolor='black')

plt.title('Preferred Services', fontsize=16)
plt.xlabel('Service Type', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()
