import os
import shutil
import zipfile
import subprocess


# Set the path to the directory containing the zip files
zip_dir_path = r"D:\@Workspace\@Design\@fonts"

# Set the name of the subdirectory to create for extracted fonts
extracted_fonts_dir = "temp_extracted_fonts"

# Set the name of the subdirectory to move extracted font files to
font_files_dir = "all-fonts"

# Create the subdirectory for extracted fonts
extracted_fonts_path = os.path.join(zip_dir_path, extracted_fonts_dir)
os.makedirs(extracted_fonts_path, exist_ok=True)

# Create the subdirectory for font files
font_files_path = os.path.join(zip_dir_path, font_files_dir)
os.makedirs(font_files_path, exist_ok=True)

# Loop through all the files in the zip directory
for filename in os.listdir(zip_dir_path):
    # Check if the file is a zip file
    if filename.endswith(".zip"):
        # Open the zip file
        zip_path = os.path.join(zip_dir_path, filename)
        with zipfile.ZipFile(zip_path, "r") as zip_file:
            # Extract all the files in the zip file to the extracted fonts subdirectory
            zip_file.extractall(extracted_fonts_path)

            # Loop through all the extracted files and subdirectories recursively
            for root, dirs, files in os.walk(extracted_fonts_path):
                for extracted_filename in files:
                    extracted_filepath = os.path.join(root, extracted_filename)
                    # Check if the extracted file is a font file and doesn't start with "._"
                    if (extracted_filename.endswith(".otf") or extracted_filename.endswith(".ttf")) and not extracted_filename.startswith("._"):
                        # Move the font file to the font files subdirectory
                        font_filepath = os.path.join(font_files_path, extracted_filename)
                        shutil.move(extracted_filepath, font_filepath)


# Get the path to the font installation script relative to this script's directory
font_script_path = os.path.join(os.path.dirname(__file__), "font-installer.py")


# Run the font installation script with the font path as an argument
subprocess.run(["python", font_script_path, font_files_dir])


