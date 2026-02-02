from pathlib import Path

def get_directory(dumpname):
    # Create a Path object for the new folder
    folder_path = Path(dumpname)

    # Use the mkdir() method
    try:
        # parents=True creates any missing parent directories
        # exist_ok=True prevents an error if the directory already exists
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Directory '{folder_path}' ensured to exist in current directory.")
        return folder_path
    except OSError as e:
        print(f"Error creating directory {folder_path}: {e}")
