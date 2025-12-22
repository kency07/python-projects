from pathlib import Path

def bulk_rename(folder_path, prefix="", suffix="", start_index=1):
    folder = Path(folder_path)

    if not folder.exists() or  not folder.is_dir():
        print("Invalid folder path")
        return
    
    files = [f for f in folder.iterdir() if f.is_file()]

    for index, file in enumerate( files, start=start_index):
        new_name = f"{prefix}{index}{suffix}{file.suffix}"
        new_path = file.with_name(new_name) 

        try: 
            file.rename(new_path)
            print(f"Renamed: {file.name} -> {new_name}")
        except Exception as e:
            print(f"failed to rename {file.name}: {e}")
    
if __name__ == "__main__":
    path = input("Enter the folder path: ").strip()
    prefix = input("Enter the prefix (optional): ").strip()
    suffix = input("Enter the suffix (optional): ").strip()
    start = input("Enter the starting number (default 1): ").strip()
    start_index = int(start) if start.isdigit() else 1
    bulk_rename(path, prefix, suffix, start_index)
