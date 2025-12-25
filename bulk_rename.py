import argparse
from pathlib import Path

def bulk_rename(folder_path, prefix="", suffix="", start_index=1, dry_run=False, extensions=None):
    folder = Path(folder_path)

    if not folder.exists() or  not folder.is_dir():
        print("Invalid folder path")
        return
    files=[]
    for f in folder.iterdir():
        if not f.is_file():
            continue
        if f.name.startswith("."):
            continue
        if extensions and f.suffix.lower() not in extensions:
            continue
        files.append(f)

    files = sorted(files, key=lambda f:f.name.lower())

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

def parse_args ():
    parser = argparse.ArgumentParser(description="Bulk File Rename")

    parser.add_argument("--path", type=str, default=".", help="Target directory (Default: current directory)")
    parser.add_argument("--prefix", type=str, default="", help="Prefix for new filename")
    parser.add_argument("--suffix", type=str, default="", help="Suffix for new  filename")
    parser.add_argument("--start", type=int, default=1, help="Starting number (default:1)")
    parser.add_argument("--ext", nargs="*", type=str, default=None, help="File extensions to rename (e.g. jpg png)")
    parser.add_argument("--dry-run", action="store_true", help="preview changes without renaming files")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    
    extensions = None
    if args.ext:
        extensions = {f".{e.lower().lstrip('.')}" for e in args.ext}

    bulk_rename (folder_path = args.path,
    prefix = args.prefix,
    suffix = args.suffix,
    start_index = args.start, 
    dry_run = args.dry_run,
    extensions= extensions)

