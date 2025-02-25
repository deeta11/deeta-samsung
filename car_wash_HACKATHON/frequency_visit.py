import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('deeta-samsung/car_wash_HACKATHON/car_wash_datasetcsv.csv')
heatmap_data = df.pivot_table(index='Customer Name', columns='Service', values='ID', aggfunc='count', fill_value=0)

plt.figure(figsize=(12, 10))
heatmap = sns.heatmap(
    heatmap_data,
    cmap='BuGn',
    annot=True,
    fmt='d',
    linecolor='black'
)

plt.title('Customer Visits by Service', fontsize=18, pad=20)
plt.xlabel('Service', fontsize=14, labelpad=10)
plt.ylabel('Customer Name', fontsize=14, labelpad=10)
plt.yticks(fontsize=12)
cbar = heatmap.collections[0].colorbar
cbar.set_label('Number of Visits', fontsize=10)
plt.tight_layout()
plt.show()

