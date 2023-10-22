# 💻 Simplenote Backup
This Python script takes a backup of your Simplenote notes and saves each note as a separate text file locally on your computer in a specified directory.

## ⚙️ Requirements
- Python 3.x
- The simplenote package (install via `pip install simplenote`)
## 🔥 Usage
1. Run the `mail-pass_encoder.py` file and encode your Simplenote account email and password.
2. Open simplenote_local_backup.py file and paste the encoded email and password in the vars list.
3. Set the path to the directory where you want to save the backup. The default path is the Desktop. You can change it by modifying the main_path variable.
4. Set the name of the root folder where the backup will be saved. The default name is "Simplenote Backup". You can change it by modifying the root_folder_name variable.
5. Run the `simplenote_backup.pyw` script.

The script will create a new folder in the specified directory with the name simplenote_backup_<date>, where <date> is the current date in the format dd-mm-yyyy. It will then save each note in the folder as a separate text file with the first line of the note as the filename. The script will also remove any invalid characters from the filename and shorten it if it exceeds 260 characters.

### 📝Note
This script is intended for personal use only. 
