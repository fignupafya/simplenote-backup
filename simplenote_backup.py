import simplenote
import os
import re
import datetime


root_folder_name = "Simplenote Backup"
mail = "e-mail"
passw = "password"


sub_folder_name = "simplenote_backup_"+datetime.date.today().strftime('%d-%m-%Y')






sn = simplenote.Simplenote(mail, passw)
note_list = sn.get_note_list()

def clean_file_name(name):
    # Remove invalid characters
    cleaned_name = re.sub('[\\/:\*\?"<>\|]', '', name)
    # Remove leading and trailing whitespace
    cleaned_name = cleaned_name.strip()
    # Shorten the string if it exceeds 260 characters
    if len(cleaned_name) > 260:
        cleaned_name = cleaned_name[:260]
    return cleaned_name


desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') # Gets path to desktop directory
root_folder_path = os.path.join(desktop_path, root_folder_name) # Creates new path to folder on desktop
if not os.path.exists(root_folder_path):
    os.makedirs(root_folder_path)
desktop_path=root_folder_path

if (sn):
    new_folder_path = os.path.join(desktop_path, sub_folder_name)  # Creates new path to folder on desktop
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    for note in note_list[0]:
        if (note.get("deleted") == 0):
            content = note.get("content").rstrip('\r\n') + "\n\n"
            title = clean_file_name(content.split('\n')[0])
            file = open(os.path.join(new_folder_path, title) + ".txt", "w", encoding="utf-8")
            file.write(content)
            file.close()






