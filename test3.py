import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\Administrator\OneDrive\Desktop\python\CodeWithHarry\chatgpt\data_eng\Railway_info.csv')

# Step 1: Check missing values before cleaning
print("Missing values before cleaning:\n", df.isnull().sum())

# Step 2: Drop rows with missing values (or use fillna if you prefer)
df_cleaned = df.dropna()

# Step 3: Standardize station names to uppercase
df_cleaned['Source_Station_Name'] = df_cleaned['Source_Station_Name'].str.upper()
df_cleaned['Destination_Station_Name'] = df_cleaned['Destination_Station_Name'].str.upper()

# Step 4: Check missing values after cleaning
print("\nMissing values after cleaning:\n", df_cleaned.isnull().sum())

# Step 5: View cleaned data
print("\nCleaned Data Preview:")
print(df_cleaned.head())
