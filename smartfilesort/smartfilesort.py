import os
import shutil
import spacy
import random
import datetime
import magic  # For file type detection

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Default categories (users can customize)
CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Code": [".py", ".js", ".java", ".cpp", ".html"],
    "Archives": [".zip", ".rar", ".tar"],
    "Executables": [".exe", ".msi"],
}

SIZE_CATEGORIES = {
    "Large Files": 100 * 1024 * 1024,  # >100MB
    "Medium Files": 10 * 1024 * 1024,  # 10MB - 100MB
    "Small Files": 0,  # <10MB
}

def get_file_category(filename):
    """Categorizes a file based on extension and NLP."""
    ext = os.path.splitext(filename)[-1].lower()
    
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category

    doc = nlp(filename.replace("_", " ").replace("-", " "))
    keywords = [token.lemma_ for token in doc if not token.is_stop]

    if "report" in keywords or "document" in keywords:
        return "Documents"
    if "photo" in keywords or "image" in keywords:
        return "Images"
    
    return "Others"

def auto_rename(file_path):
    """Renames a file using AI-based NLP and context."""
    directory, filename = os.path.split(file_path)
    name, ext = os.path.splitext(filename)

    doc = nlp(name.replace("_", " ").replace("-", " "))
    words = [token.lemma_ for token in doc if not token.is_stop]
    
    if words:
        new_name = "-".join(words[:3])  # Use first 3 key words
    else:
        new_name = f"file_{random.randint(1000, 9999)}"

    timestamp = datetime.datetime.now().strftime("%Y%m%d")
    new_filename = f"{new_name}-{timestamp}{ext}"
    new_filepath = os.path.join(directory, new_filename)

    os.rename(file_path, new_filepath)
    print(f"Renamed: {filename} → {new_filename}")
    return new_filename

def organize_files(directory):
    """Organizes files into categories and renames them automatically."""
    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)
        
        if os.path.isfile(filepath):
            new_filename = auto_rename(filepath)
            new_filepath = os.path.join(directory, new_filename)

            category = get_file_category(new_filename)
            target_folder = os.path.join(directory, category)
            
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(new_filepath, os.path.join(target_folder, new_filename))
            print(f"Moved: {new_filename} → {category}")

def organize_by_size(directory):
    """Organizes files based on size."""
    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)

        if os.path.isfile(filepath):
            category = "Large Files" if os.path.getsize(filepath) >= SIZE_CATEGORIES["Large Files"] else "Medium Files" if os.path.getsize(filepath) >= SIZE_CATEGORIES["Medium Files"] else "Small Files"
            target_folder = os.path.join(directory, category)

            os.makedirs(target_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(target_folder, file))
            print(f"Moved: {file} → {category}")

def organize_by_date(directory):
    """Organizes files by creation date."""
    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)

        if os.path.isfile(filepath):
            created_time = datetime.datetime.fromtimestamp(os.path.getctime(filepath)).strftime("%Y-%m-%d")
            folder_name = os.path.join(directory, f"Created_{created_time}")

            os.makedirs(folder_name, exist_ok=True)
            shutil.move(filepath, os.path.join(folder_name, file))
            print(f"Moved: {file} → {folder_name}")

def move_file(filename, target_folder):
    """Moves a file to a custom folder."""
    filepath = os.path.abspath(filename)
    
    if os.path.exists(filepath):
        os.makedirs(target_folder, exist_ok=True)
        shutil.move(filepath, os.path.join(target_folder, os.path.basename(filepath)))
        print(f"Moved {filename} → {target_folder}")
    else:
        print("File not found!")

def clean_empty_folders(directory):
    """Deletes empty folders after sorting."""
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path) and not os.listdir(folder_path):
            os.rmdir(folder_path)
            print(f"Deleted empty folder: {folder}")

if __name__ == "__main__":
    organize_files(os.getcwd())  # Default action: organize by type
