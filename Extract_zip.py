import zipfile
import os

# Define the path to the uploaded zip file and the extraction directory
zip_file_path = './imagedata.zip'
extraction_dir = './imagedata'

# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_dir)

# List the contents of the extraction directory to understand its structure
extracted_files = []
for root, dirs, files in os.walk(extraction_dir):
    for file in files:
        extracted_files.append(os.path.join(root, file))

print(extracted_files)



