import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('redditscraper_all.csv')

# Convert the createdAt field to datetime
df['createdAt'] = pd.to_datetime(df['createdAt'])

# Filter rows where the body field contains the word "thcp" (case insensitive)
df_filtered = df[df['body'].str.contains('thcp', case=False, na=False)]

# Extract the date part
df_filtered['date'] = df_filtered['createdAt'].dt.date

# Count the number of posts for each date
posts_per_date = df_filtered['date'].value_counts().sort_index()

# Plot the results
plt.figure(figsize=(10, 5))
posts_per_date.plot(kind='bar')
plt.xlabel('Date')
plt.ylabel('Number of Posts/Comments')
plt.title('Number of Posts/Comments Per Date')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()