from pathlib import Path

def bulk_rename(folder_path):
    folder = Path(folder_path)

    if not folder.exists() or  not folder.is_dir():
        print("Invalid folder path")
        return
    
    files = [f for f in folder.iterdir() if f.is_file()]

    for index, file in enumerate( files, start=1):
        new_name = f"file_{index}{file.suffix}"
        new_path = file.with_name(new_name) 

        try: 
            file.rename(new_path)
            print(f"Renamed: {file.name} -> {new_name}")
        except Exception as e:
            print(f"failed to rename {file.name}: {e}")
    
if __name__ == "__main__":
    path = input("Enter the folder path: ").strip()
    bulk_rename(path)
