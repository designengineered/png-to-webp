# PNG to WebP Converter

This is a Python script that converts PNG images to WebP format in bulk. The user selects a directory, and the script converts all PNG images in that directory. The converted images are saved in a `converted` subdirectory within the selected directory. After the conversion process, the `converted` subdirectory is automatically opened in the default file explorer.

## Prerequisites

- Python 3.x
- Pillow library

## Installation

For all these code snippets use your terminal of choice. You can honestly copy and paste in the presented order and it should work.
1. Clone the repository:

    ```bash
    git clone https://github.com/laztaxon/png-to-webp.git
    ```

2. Install Python:
   - For Windows and macOS, download and install Python from the official website: https://www.python.org/downloads/
   - For macOS, you can also use Homebrew: `brew install python` or 
   - For Linux, use your package manager, e.g., `sudo apt install python3`

3. Set up the virtual environment:
   - For Windows, use: `python -m venv venv`
   - For Unix or MacOS, use: `python3 -m venv venv`

4. Activate the virtual environment:
   - For Windows, use: `venv\Scripts\activate`
   - For Unix or MacOS, use: `source venv/bin/activate`

5. Install the required dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt

6. Running the script
After installing the dependencies, you can run the main.py script:
   ```python
   python main.py

7. Deactivating the Virtual Environment

   After you're done running the script, you can deactivate the virtual environment:

   ```bash
   deactivate
