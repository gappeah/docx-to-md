import os
import pypandoc
from docx import Document
from tkinter import Tk, filedialog

def convert_docx_to_md(docx_path, md_path):
    """
    Convert a .docx file to .md using pypandoc.
    """
    try:
        # Convert .docx to .md
        output = pypandoc.convert_file(docx_path, 'md', outputfile=md_path)
        print(f"Converted: {docx_path} -> {md_path}")
        return True
    except Exception as e:
        print(f"Failed to convert {docx_path}: {e}")
        return False

def process_folder(input_folder, output_folder):
    """
    Recursively process a folder to convert all .docx files to .md.
    """
    for root, dirs, files in os.walk(input_folder):
        # Create corresponding folder structure in the output folder
        relative_path = os.path.relpath(root, input_folder)
        current_output_folder = os.path.join(output_folder, relative_path)
        os.makedirs(current_output_folder, exist_ok=True)

        for file in files:
            if file.endswith(".docx"):
                # Define input and output paths
                docx_path = os.path.join(root, file)
                md_filename = os.path.splitext(file)[0] + ".md"
                md_path = os.path.join(current_output_folder, md_filename)

                # Convert .docx to .md
                convert_docx_to_md(docx_path, md_path)

def select_folder(title):
    """
    Open a dialog to select a folder.
    """
    root = Tk()
    root.withdraw()  # Hide the root window
    folder = filedialog.askdirectory(title=title)
    return folder

if __name__ == "__main__":
    # Prompt the user to select the input folder
    input_folder = select_folder("Select Input Folder")
    if not input_folder:
        print("No input folder selected. Exiting.")
        exit()

    # Prompt the user to select the output folder
    output_folder = select_folder("Select Output Folder")
    if not output_folder:
        print("No output folder selected. Exiting.")
        exit()

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process the input folder
    process_folder(input_folder, output_folder)
    print("Conversion complete!")