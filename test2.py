import pandas as pd

# Load the dataset (adjust the path as needed)
df = pd.read_csv(r'C:\Users\Administrator\OneDrive\Desktop\python\CodeWithHarry\chatgpt\data_eng\Railway_info.csv')

# Total number of trains
num_trains = df.shape[0]
print(f"Total number of trains: {num_trains}")

# Unique source and destination stations
unique_sources = df['Source_Station_Name'].nunique()
unique_destinations = df['Destination_Station_Name'].nunique()
print(f"Unique source stations: {unique_sources}")
print(f"Unique destination stations: {unique_destinations}")

# Most common source station
most_common_source = df['Source_Station_Name'].value_counts().idxmax()
most_common_source_count = df['Source_Station_Name'].value_counts().max()
print(f"Most common source station: {most_common_source} ({most_common_source_count} trains)")

# Most common destination station
most_common_destination = df['Destination_Station_Name'].value_counts().idxmax()
most_common_destination_count = df['Destination_Station_Name'].value_counts().max()
print(f"Most common destination station: {most_common_destination} ({most_common_destination_count} trains)")
