import zipfile
import os

# Set the path to the zip file
zip_path = "44k.zip"

# Set the path to the directory where you want to extract the images
extract_path = "images"

# Set the number of images you want to extract
num_images = 12000

# Create the extract directory if it doesn't exist
if not os.path.exists(extract_path):
    os.makedirs(extract_path)

# Open the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_file:
    # Get the list of all files in the zip file
    all_files = zip_file.namelist()
    # Filter the list to only include image files
    image_files = [file for file in all_files if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png')]
    # Sort the image files alphabetically
    image_files.sort()
    # Extract the specified number of images
    for i in range(num_images):
        image_file = image_files[i]
        # Extract the image file to the extract directory
        zip_file.extract(image_file, extract_path)

          
