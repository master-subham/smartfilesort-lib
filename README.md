# smartfilesort

**smartfilesort** is an AI-powered file organizer that automatically sorts, renames, and organizes your files based on type, size, and creation date.

## Features

- **File Type Organization:** Automatically categorizes files (e.g., Documents, Images, Videos, Music, Code).
- **Size-Based Sorting:** Separates files into large, medium, and small categories.
- **Date-Based Organization:** Groups files by creation date.
- **AI-Based Auto-Rename:** Uses NLP (via spaCy) to intelligently rename files based on their content.
- **Manual File Move:** Easily move files to custom folders.
- **Clean Empty Folders:** Automatically removes empty folders after organizing.

## Installation

Install the package via pip:

```bash
pip install smartfilesort
Usage
You can use the library either as a command-line tool or import its functions in your Python code.

Command-Line
After installing, run the default organizer on the current directory:

bash
Copy
Edit
smartfilesort
In Python
python
Copy
Edit
from smartfilesort import organize_files, organize_by_size, organize_by_date, move_file, auto_rename, clean_empty_folders

# Organize files by type (with auto-renaming)
organize_files("path/to/your/directory")

# Organize files by size
organize_by_size("path/to/your/directory")

# Organize files by creation date
organize_by_date("path/to/your/directory")

# Manually move a file to a custom folder
move_file("example.py", "path/to/your/directory/CustomFolder")

# Auto-rename a specific file
auto_rename("path/to/your/directory/example.docx")

# Clean empty folders
clean_empty_folders("path/to/your/directory")
Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any changes.