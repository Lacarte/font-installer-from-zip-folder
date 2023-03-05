# Readme file for font installation

This script is designed to automate the installation of fonts from zip files in a directory. 

## Usage

1. Place all the zip files containing fonts in a directory. 
2. Set the `zip_dir_path` variable to the path of the directory containing the zip files.
3. Set the `extracted_fonts_dir` variable to the name of the subdirectory to create for extracted fonts.
4. Set the `font_files_dir` variable to the name of the subdirectory to move extracted font files to.
5. Run the script.

The script will extract all font files from the zip files and move them to the `font_files_dir` subdirectory. It will then run the `font-installer.py` script to install the fonts on your system.

Note: You need to have Python 3 installed to run this script.

## Files

- `font-installer.py`: This script installs font files on your system.
- `font_installer_script.py`: This script extracts font files from zip files and installs them on your system.
- `README.md`: This file.

## License

This script is licensed under the MIT License. Feel free to use it, modify it, or distribute it.
