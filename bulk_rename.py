from pathlib import Path

def bulk_rename(folder_path, prefix="", suffix="", start_index=1, dry_run=False):
    folder = Path(folder_path)

    if not folder.exists() or  not folder.is_dir():
        print("Invalid folder path")
        return
    
    files = sorted([f for f in folder.iterdir() if f.is_file()], key=lambda f:f.name.lower())

    for index, file in enumerate( files, start=start_index):
        new_name = f"{prefix}{index}{suffix}{file.suffix}"
        new_path = file.with_name(new_name) 

        try:
            if new_path.exists():
                print(f"skipped (exists): {new_name}")
                continue
            if dry_run:
                print(f"dry_run: {file.name} -> {new_name}")
            else:     
                file.rename(new_path)
                print(f"Renamed: {file.name} -> {new_name}")
        except Exception as e:
            print(f"failed to rename {file.name}: {e}")
    
if __name__ == "__main__":
    path = input("Enter the folder path: ").strip()
    prefix = input("Enter the prefix (optional): ").strip()
    suffix = input("Enter the suffix (optional): ").strip()
    start = input("Enter the starting number (default 1): ").strip()
    dry = input("dry_run? (y/n): ").strip().lower()
    dry_run = dry == "y"
    start_index = int(start) if start.isdigit() else 1
    bulk_rename(path, prefix, suffix, start_index, dry_run)
