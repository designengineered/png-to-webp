import os
import subprocess
from tkinter import filedialog, Tk
from PIL import Image

def convert_images():
    # Create a hidden Tkinter window
    root = Tk()
    root.withdraw()

    # Ask the user to select a directory
    folder_path = filedialog.askdirectory()

    # Create a new 'converted' subdirectory inside the selected directory
    converted_folder_path = os.path.join(folder_path, 'converted')
    os.makedirs(converted_folder_path, exist_ok=True)

    # Iterate over all files in the selected folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            img = Image.open(os.path.join(folder_path, filename))
            # Save the converted image in the 'converted' subdirectory
            img.save(os.path.splitext(os.path.join(converted_folder_path, filename))[0] + ".webp")

    # Open the 'converted' subdirectory
    if os.name == 'nt':  # For Windows
        os.startfile(converted_folder_path)
    elif os.name == 'posix':  # For Unix-based systems (like Linux and macOS)
        subprocess.run(['open', converted_folder_path])

convert_images()