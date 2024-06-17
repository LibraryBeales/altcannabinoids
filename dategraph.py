import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('redditscraper_all.csv')

df['createdAt'] = pd.to_datetime(df['createdAt'])

df['date'] = df['createdAt'].dt.date

posts_per_date = df['date'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
posts_per_date.plot(kind='bar')
plt.xlabel('Date')
plt.ylabel('Number of Posts')
plt.title('Number of Posts Per Date')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()