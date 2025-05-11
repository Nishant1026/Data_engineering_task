import pandas as pd

# Load the dataset
df = pd.read_csv('C:/Users/Administrator/OneDrive/Desktop/python/CodeWithHarry/chatgpt/data_eng/Railway_info.csv')
 
# Display the first 10 rows using iloc
print("First 10 rows:")
print(df.iloc[:10])

# Get data types and non-null count using describe(include='all')
print("\nBasic statistics (structure, data types, etc.):")
print(df.describe(include='all'))

# Show data types directly
print("\nData types of each column:")
print(df.dtypes)

# Count total missing values using isnull and sum
print("\nMissing values per column:")
print(df.isnull().sum())
