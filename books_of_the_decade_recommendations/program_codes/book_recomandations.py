import pandas as pd 

# Load the dataset
file_path = "C:/Users/joshi/OneDrive/Desktop/DS mini projects/books_of_the_decade_dataset/books_of_the_decade.csv"
data = pd.read_csv(file_path)

# Preview the dataset
print("Dataset Preview:")
print(data.head())

# Drop unnecessary columns (data cleaning)
data = data.drop(columns=['Index'])

# Handle missing values
# Convert 'Rating' to numeric, handling non-numeric values (if any)
data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')

# Convert 'Number of Votes' to numeric, handling non-numeric values (if any)
data['Number of Votes'] = pd.to_numeric(data['Number of Votes'], errors='coerce')

# Fill missing values
data['Rating'].fillna(data['Rating'].median(), inplace=True)
data['Number of Votes'].fillna(0, inplace=True)

# Function to recommend books based on rating and votes
def recommend_books(data, top_n=10, min_votes=100):
    
    # Ensure the dataset has numeric values for sorting
    numeric_data = data.copy()
    numeric_data['Rating'] = pd.to_numeric(numeric_data['Rating'], errors='coerce')
    numeric_data['Number of Votes'] = pd.to_numeric(numeric_data['Number of Votes'], errors='coerce')

    # Drop rows with missing or invalid numeric data
    numeric_data.dropna(subset=['Rating', 'Number of Votes'], inplace=True)

    # Filter books with at least min_votes
    filtered_data = numeric_data[numeric_data['Number of Votes'] >= min_votes]
    
    # Sort by Rating (descending) and then by Number of Votes (descending)
    sorted_data = filtered_data.sort_values(by=['Rating', 'Number of Votes'], ascending=False)
    
    # Return the top N books
    return sorted_data.head(top_n)

# Recommend books
top_books = recommend_books(data, top_n=10, min_votes=100)

print("\nTop Recommended Books:")
print(top_books[['Book Name', 'Author', 'Rating', 'Number of Votes']])

