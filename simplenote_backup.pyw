import simplenote
import os
import re
import datetime
import base64


# 1. string encoded mail    2. string encoded password
vars =["encoded mail here", "encoded password here="]

# Path to desktop directory
main_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Root folder name
root_folder_name = "Simplenote Backup"


















sn = simplenote.Simplenote(base64.b64decode(vars[0].encode()).decode('utf-8'), base64.b64decode(vars[1].encode()).decode('utf-8'))
note_list = sn.get_note_list()


if (sn):

    def clean_file_name(name):
        # Remove invalid characters
        cleaned_name = re.sub('[\\/:\*\?"<>\|]', '', name)
        # Remove leading and trailing whitespace
        cleaned_name = cleaned_name.strip()
        # Shorten the string if it exceeds 260 characters
        if len(cleaned_name) > 260:
            cleaned_name = cleaned_name[:260]
        return cleaned_name




    root_folder_path = os.path.join(main_path, root_folder_name)  # Creates new path to folder on desktop
    if not os.path.exists(root_folder_path):
        os.makedirs(root_folder_path)
    main_path = root_folder_path
    files_not_to_delete=[os.path.basename(__file__)]
    if not os.path.exists(main_path):
        os.makedirs(main_path)

    for note in note_list[0]:
        if (note.get("deleted") == 0):
            content = note.get("content").rstrip('\r\n') + "\n\n"
            title = clean_file_name(content.split('\n')[0])
            filename = os.path.join(main_path, title) + ".txt"
            file = open(filename, "w", encoding="utf-8")
            file.write(content)
            file.close()
            files_not_to_delete.append(title+".txt")

    for i in os.listdir(main_path):
        if i not in files_not_to_delete:
            os.remove(os.path.join(main_path,i))
