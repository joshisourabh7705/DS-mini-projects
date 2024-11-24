import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# Load the dataset
file_path = "C:/Users/joshi/OneDrive/Desktop/DS mini projects/books_of_the_decade_dataset/books_of_the_decade.csv"
data = pd.read_csv(file_path)

# Handle missing values
# Convert 'Rating' to numeric, handling non-numeric values (if any)
data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')

# Convert 'Number of Votes' to numeric, handling non-numeric values (if any)
data['Number of Votes'] = pd.to_numeric(data['Number of Votes'], errors='coerce')

# Fill missing values
data['Rating'].fillna(data['Rating'].median(), inplace=True)
data['Number of Votes'].fillna(0, inplace=True)


# Plot histogram for 'Rating'
plt.figure(figsize=(10, 5))
plt.hist(data['Rating'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Histogram of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# Bar chart for average 'Number of Votes' per 'Rating'
avg_votes_per_rating = data.groupby('Rating')['Number of Votes'].mean()

plt.figure(figsize=(12, 6))
avg_votes_per_rating.plot(kind='bar', color='teal', alpha=0.8, edgecolor='black')
plt.title('Average Number of Votes by Rating')
plt.xlabel('Rating')
plt.ylabel('Average Number of Votes')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# Violin Plot for 'Number of Votes'
plt.figure(figsize=(10, 6))
sns.violinplot(data=data, y='Number of Votes', color='lightcoral', inner="quartile", linewidth=1.5)
plt.title('Distribution of Number of Votes', fontsize=16, fontweight='bold')
plt.ylabel('Number of Votes', fontsize=12)
plt.xlabel('Density', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5)
sns.despine()
plt.show()


