import os
import platform

def open_file(file_path):
    print(f"Data has been successfully written to {file_path}")
    if platform.system() == "Darwin":  # macOS
        os.system(f"open {file_path}")
    elif platform.system() == "Windows":  # Windows
        os.system(f"start {file_path}")
    elif platform.system() == "Linux":  # Linux
        os.system(f"xdg-open {file_path}")
    else:
        print(f"Please manually open the file located at {file_path}")