# Bulk File Renamer (Python CLI Tool)

A safe and flexible Python CLI tool to bulk rename files in a folder.
Designed with collision protection, dry-run mode, and extension filtering.

---

## Features
- Bulk rename files with numbering
- Optional prefix and suffix
- Custom starting number
- Rename only selected file extensions
- Dry-run mode (preview changes safely)
- Collision-safe (never overwrites files)
- Skips hidden files and folders
- Can be safely run multiple times

---

## Requirements
- Python 3.8+

---

## Installation
Clone or download the project, then navigate into the folder:

```bash
git clone https://github.com/kency07/bulk-file-renamer.git
cd bulk-file-renamer
```
---

## Usage
 
### Basic rename
```bash
python bulk_rename.py --path myfolder
```
### Prefix, Suffix, and Start number
```bash
python bulk_rename.py --path myfolder --prefix Img_  --suffix _v1  --start 10
```
### Rename only specific extensions
```bash
python bulk_rename.py --path myfolder  --ext jpg png
```
### Dry run (recommended)
```bash
python bulk_rename.py  --path myfolder  --dry-run
```
### CLI Options

| Flag | Description | Example |
|------|------------|---------|
| `--path` | Path to the folder containing files to rename | `--path myfolder` |
| `--prefix` | Add a prefix to each file name | `--prefix Img_` |
| `--suffix` | Add a suffix to each file name | `--suffix _v1` |
| `--start` | Starting number for numbering | `--start 10` |
| `--ext` | Rename only files with specific extensions | `--ext jpg png` |
| `--dry-run` | Preview changes without renaming | `--dry-run` |
| `--help` | Show help message | `--help` |

---
 
## Help

```bash
python bulk_rename.py --help
```
### Example output:
```
Usage: bulk_rename.py --path PATH [options]

Options:

  --path PATH       Folder containing files
  --prefix PREFIX   Add prefix to filenames
  --suffix SUFFIX   Add suffix to filenames
  --start N         Starting number
  --ext EXT [EXT]   Filter by file extensions
  --dry-run         Preview changes without renaming
  --help            Show this help message
```
---

## Examples

### Before:
```
file_10.jpg
file_11.jpg
file_12.png
```
### After:
```
Img_10_v1.jpg
Img_11_v1.jpg
Img_12_v1.png
```
---

## Safety Notes
- Files are never overwritten
- Name collisions are resolved automatically
- Script can be run multiple times without data loss

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
