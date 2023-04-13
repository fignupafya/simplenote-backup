# Simplenote Backup
This Python script allows you to backup your Simplenote notes to your computer, by creating a folder on your desktop and saving each note as a text file.

## Requirements
- Python 3.x
- The simplenote package (install via `pip install simplenote`)
## Usage
1. Open the script and edit the `mail` and `passw` variables with your Simplenote email and password, respectively.
2. Run the script in a Python environment (e.g., IDLE, PyCharm) or via the command line (python simplenote_backup.py).
3. The script will create a folder named "Simplenote Backup" on your desktop and a subfolder with today's date (e.g., "simplenote_backup_13-04-2023").
4. Each note will be saved as a text file in the subfolder, using the first line of the note's content as the filename (after removing invalid characters and trimming leading/trailing whitespace).
