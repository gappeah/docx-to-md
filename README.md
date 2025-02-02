# DOCX to Markdown Converter

This repository contains Python scripts to batch convert `.docx` files to `.md` (Markdown) format while preserving the folder structure. Two versions of the script are provided:

1. **With Pandoc**: Uses `pypandoc` for accurate Markdown conversion (supports headings, lists, tables, etc.).
2. **Without Pandoc**: Uses `python-docx` for plain text extraction (no advanced Markdown formatting).

---

## Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.x
- Required Python libraries (install via `pip`):
  ```bash
  pip install python-docx pypandoc
  ```

For the **Pandoc version**, you also need to install `pandoc`:
- Download and install `pandoc` from [https://pandoc.org/installing.html](https://pandoc.org/installing.html).
- Ensure `pandoc` is added to your system's PATH.

---

## Scripts

### 1. `main_with_pandoc.py`
This script uses `pypandoc` to convert `.docx` files to `.md` with proper Markdown formatting.

#### Features:
- Preserves folder structure.
- Supports advanced Markdown formatting (headings, lists, tables, etc.).
- Requires `pandoc` to be installed.

#### Usage:
1. Run the script:
   ```bash
   python main_with_pandoc.py
   ```
2. A popup window will prompt you to select the input folder (containing `.docx` files).
3. Another popup window will prompt you to select the output folder (where `.md` files will be saved).
4. The script will convert all `.docx` files in the input folder (and subfolders) to `.md` files in the output folder.

---

### 2. `main_without_pandoc.py`
This script uses `python-docx` to extract plain text from `.docx` files and save it as `.md`.

#### Features:
- Preserves folder structure.
- Does not require `pandoc`.
- Outputs plain text (no advanced Markdown formatting).

#### Usage:
1. Run the script:
   ```bash
   python main_without_pandoc.py
   ```
2. A popup window will prompt you to select the input folder (containing `.docx` files).
3. Another popup window will prompt you to select the output folder (where `.md` files will be saved).
4. The script will convert all `.docx` files in the input folder (and subfolders) to `.md` files in the output folder.

---

## Folder Structure

The scripts preserve the folder structure of the input folder. For example:

```
input_folder/
├── file1.docx
├── file2.docx
└── subfolder/
    ├── file3.docx
    └── file4.docx
```

Will be converted to:

```
output_folder/
├── file1.md
├── file2.md
└── subfolder/
    ├── file3.md
    └── file4.md
```

---

## Which Script to Use?

- Use **`main_with_pandoc.py`** if:
  - You need accurate Markdown formatting (headings, lists, tables, etc.).
  - You have `pandoc` installed on your system.

- Use **`main_without_pandoc.py`** if:
  - You only need plain text extraction.
  - You don't want to install `pandoc`.

---

## Example

### Input Folder
```
input_folder/
├── document1.docx
└── notes/
    ├── note1.docx
    └── note2.docx
```

### Output Folder (After Conversion)
```
output_folder/
├── document1.md
└── notes/
    ├── note1.md
    └── note2.md
```

---

## Contributing

If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.
