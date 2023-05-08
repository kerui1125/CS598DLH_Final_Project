import pandas as pd

# Read the modified CSV file
file_path = '/Users/liukerui/Documents/CS598_DLH/Final_Project/data/combined_data.csv'
data = pd.read_csv(file_path)

# Add a new column 'id' with incrementing values
data['id'] = range(len(data))

# Rename the 'isic_id' column to 'image_id'
data.rename(columns={'isic_id': 'image_id'}, inplace=True)

# Save the modified CSV file
data.to_csv(file_path, index=False)