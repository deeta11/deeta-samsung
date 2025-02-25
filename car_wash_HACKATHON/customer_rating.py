import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('deeta-samsung/car_wash_HACKATHON/car_wash_datasetcsv.csv')

rating_counts = df['Customer Rating'].value_counts().reindex(range(1, 6), fill_value=0).sort_index(ascending=False)
total_ratings = rating_counts.sum()
rating_percentages = (rating_counts / total_ratings) * 100
average_rating = df['Customer Rating'].mean()
labels = ['5 Stars', '4 Stars', '3 Stars', '2 Stars', '1 Star']

plt.figure(figsize=(10, 6))
bars = plt.barh(labels, rating_percentages, color='orange', edgecolor='black')

plt.text(0.5, 1.1, f'Average Rating: {average_rating:.1f} out of 5', fontsize=16, ha='center', transform=plt.gca().transAxes)
plt.title('Customer Ratings Distribution', fontsize=16, pad=20)
plt.xlabel('Percentage of Customers', fontsize=12)
plt.ylabel('Rating', fontsize=12)

plt.show()
