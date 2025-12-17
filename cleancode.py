import os
import pandas as pd

# Paths
image_folder = "images"
metadata_file = "metadata.xlsx"

# Load metadata
df = pd.read_excel(metadata_file)

# Column containing image file names
col = "image_file_name"

# List of image names in Excel
excel_files = set(df[col].astype(str))

# List of files actually present in the folder
folder_files = set(os.listdir(image_folder))

# 1. Excel entries that do NOT exist in images/
missing_in_folder = excel_files - folder_files

# 2. Files in images/ that are NOT in Excel
extra_in_folder = folder_files - excel_files

# Delete rows from Excel for entries missing in folder
if missing_in_folder:
    print("\nDeleting rows with missing image files:")
    for fname in missing_in_folder:
        print("  - Row deleted for:", fname)
    df = df[~df[col].isin(missing_in_folder)]

# Delete extra files from folder
if extra_in_folder:
    print("\nDeleting extra files from images/:")
    for fname in extra_in_folder:
        file_path = os.path.join(image_folder, fname)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print("  - File deleted:", fname)

# Save cleaned metadata
df.to_excel(metadata_file, index=False)
print("\nCleaning completed.")
