import os
import shutil
import pandas as pd
from zipfile import ZipFile

# Assuming your DataFrame is df
# and 'filename' column contains PDF filenames

# Replace 'your_directory_path' with the actual path to your PDF directory
pdf_directory = 'your_directory_path'
output_directory = 'your_output_directory'
backup_directory = 'your_backup_directory'
log_file_path = 'your_log_file.txt'  # Path to the text file for logging
zip_file_path = 'your_output_zip.zip'  # Path to the zip file for copied files

# Create the output and backup directories if they don't exist
os.makedirs(output_directory, exist_ok=True)
os.makedirs(backup_directory, exist_ok=True)

# Function to copy or move PDF files based on the output directory existence
def process_pdf(filename):
    source_path = os.path.join(pdf_directory, filename)
    output_path = os.path.join(output_directory, filename)
    backup_path = os.path.join(backup_directory, filename)

    if os.path.exists(output_path):
        shutil.copy2(source_path, output_path)  # Copy to output directory
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"Copied: {filename}\n")
    else:
        shutil.move(source_path, backup_path)  # Move to backup directory
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"Moved: {filename}\n")

# Iterate through DataFrame rows
for index, row in df.iterrows():
    filename = row['filename'] + '.pdf'  # assuming filenames in DataFrame don't include extensions
    process_pdf(filename)

# Zip the files in the output directory
with ZipFile(zip_file_path, 'w') as zip_file:
    for file_name in os.listdir(output_directory):
        file_path = os.path.join(output_directory, file_name)
        zip_file.write(file_path, arcname=file_name)

print("PDF files processed successfully. Log written to", log_file_path)
print("Copied files zipped to", zip_file_path)