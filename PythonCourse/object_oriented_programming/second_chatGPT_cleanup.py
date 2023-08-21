import os
import shutil

def organize_files_on_desktop():
    desktop_path = os.path.expanduser("~/Desktop")
    file_extensions_mapping = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
        "Zip Archives": [".zip", ".rar", ".7z"],
        # Add more categories and extensions if needed
    }
    
    for file in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            for folder_name, extensions in file_extensions_mapping.items():
                if file_extension in extensions:
                    folder_path = os.path.join(desktop_path, folder_name)
                    if not os.path.exists(folder_path):
                        os.mkdir(folder_path)
                    new_file_path = os.path.join(folder_path, file)
                    shutil.move(file_path, new_file_path)
                    print(f"Moved '{file}' to '{folder_name}' folder.")
                    break

if __name__ == "__main__":
    organize_files_on_desktop()
