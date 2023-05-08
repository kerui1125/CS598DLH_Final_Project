import pandas as pd
import glob

# List of CSV files to combine
input_files = glob.glob('/Users/liukerui/Documents/CS598_DLH/Final_Project/data/CSVs/*.csv')

# Read and concatenate the CSV files
dataframes = []
for file in input_files:
    df = pd.read_csv(file)
    dataframes.append(df)

combined_data = pd.concat(dataframes, axis=0, ignore_index=True)

# Save the combined data as a new CSV file
output_file = '/Users/liukerui/Documents/CS598_DLH/Final_Project/data/combined_data.csv'
combined_data.to_csv(output_file, index=False)

# Modify the first column of the combined CSV file
# Read the combined CSV file
file_path = '/Users/liukerui/Documents/CS598_DLH/Final_Project/data/combined_data.csv'
data = pd.read_csv(file_path)

# Modify the 'isic_id' column
column_name = 'isic_id'
if column_name in data.columns:
    data[column_name] = data[column_name].apply(lambda x: f"{x}.JPG")
else:
    print(f"Column '{column_name}' not found.")

# Save the modified CSV file
data.to_csv(file_path, index=False)