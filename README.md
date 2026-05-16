# File Collector Utility

A simple, dependency-free Python script designed to aggregate the contents of multiple text or source code files from a directory tree into a single, structured text file (`collected.txt`). This is especially useful for bundling code context for LLMs (Large Language Models), conducting code reviews, or creating consolidated text backups.

## Features

- **Zero Dependencies**: Runs entirely on the Python Standard Library (requires Python 3.x).
- **Recursive Search**: Automatically traverses all subdirectories from the specified path.
- **Flexible Extensions**: Accept multiple file extensions at once (e.g., `.py`, `.md`, `js`). It handles them case-insensitively and works whether or not you include the leading dot.
- **Overwrite Protection**: Safely checks if `collected.txt` already exists in the execution directory and prompts you for confirmation before overwriting it.
- **Encoding & Error Robustness**: Gracefully skips binary files, incompatible encodings, or unreadable files without crashing the process.
- **Clean Structure**: Clearly delimits each file's boundaries with standardized headers and footers containing the absolute path.

## Requirements

- Python 3.0 or higher

## Usage

Run the script from your terminal by passing the target directory path followed by one or more file extensions:

```bash
python collect.py <directory_path> <ext1> [ext2 ...]
```

### Examples

Collect all Python and Markdown files from a `projects` folder in your home directory:

```bash
python collect.py ~/projects .py .md

```

Collect all JavaScript, TypeScript, and JSON files from the current folder:

```bash
python collect.py . js ts json

```

## Output Format

The script creates a file named `collected.txt` in the folder where it was executed. The contents are structured identically to the format below:

```text
=====================
BEGIN: /absolute/path/to/file1.py
=====================
def hello_world():
    print("Hello, world!")
=====================
END: /absolute/path/to/file1.py
=====================

=====================
BEGIN: /absolute/path/to/notes.md
=====================
# Project Notes
- Item 1
- Item 2
=====================
END: /absolute/path/to/notes.md
=====================
```
The `README.md` file has been generated. It provides a clean overview of the utility, its core features, usage instructions with practical examples, and an explicit breakdown of the output formatting structural rules you provided.

```
