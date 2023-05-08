import pandas as pd

# Read the CSV file
file_path = '/Users/liukerui/Documents/CS598_DLH/Final_Project/data/CSVs/metadata 16.csv'
data = pd.read_csv(file_path)

# Delete the column
columns_to_delete = [
    'attribution', 'copyright_license', 'acquisition_day', 'anatom_site_general', 'clin_size_long_diam_mm',
    'dermoscopic_type', 'diagnosis_confirm_type', 'family_hx_mm', 'image_type', 'lesion_id',
    'mel_class', 'mel_mitotic_index', 'mel_thick_mm', 'mel_type', 'mel_ulcer', 'melanocytic',
    'nevus_type', 'personal_hx_mm', 'pixels_x', 'pixels_y'
]
for column_to_delete in columns_to_delete:
    if column_to_delete in data.columns:
        data = data.drop(column_to_delete, axis=1)
    else:
        print(f"Column '{column_to_delete}' not found.")

print("num of cols is: " + str(len(data.columns)))

# Save the modified CSV file
data.to_csv(file_path, index=False)
