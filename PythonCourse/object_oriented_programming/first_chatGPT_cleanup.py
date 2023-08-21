import os
import shutil

# Define the path of the Desktop
desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')

# Create a dictionary where keys are extensions and values are destination folders
file_types = {
    # Images
    ('.png', '.jpg', '.jpeg', '.gif', '.tiff', '.bmp', '.ico'): 'Images',
    # Documents
    ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'): 'Documents',
    # Archives
    ('.zip', '.rar', '.tar', '.gz', '.bz2'): 'Archives',
}

def organize_desktop(desktop_path, file_types):
    # Check each file on the Desktop
    for filename in os.listdir(desktop_path):
        file, ext = os.path.splitext(filename)
        
        # Check each type category
        for extensions, folder in file_types.items():
            # If this file has this extension
            if ext in extensions:
                folder_path = os.path.join(desktop_path, folder)

                # Create the folder if it doesn't exist
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Create the full old path and the full new path
                old_path = os.path.join(desktop_path, filename)
                new_path = os.path.join(folder_path, filename)

                # Move the file
                shutil.move(old_path, new_path)
                break

if __name__ == "__main__":
    organize_desktop(desktop_path, file_types)
