#why python
#simple syntax,rich ecosystem
#cross-platform suport
#use cases:
#-batch files 
#-web development
#-data analysis
#-artificial intelligence

#the os module

import os 
for file in os.listdir("."):
    if file.endswith(".py"):
        print(file)
#making a copy of a file
import shutil
shutil.copy("pythonforautomation.py","pythonforautomation_copy.py")
from datetime import date, datetime
now=datetime.now()
print(f"Current date and time: {now}")
#backup script

#creating a folder
def create_folder(backup_dir):
    import os
    #folder should be created on desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    backup_dir = os.path.join(desktop_path, backup_dir)
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"Folder '{backup_dir}' created successfully.")
    else:
        print(f"Folder '{backup_dir}' already exists.")
create_folder("backup_folder")
#make file in backup folder
def create_file_in_backup_folder(backup_dir, file_name):
    import os
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    backup_dir = os.path.join(desktop_path, backup_dir)
    file_path = os.path.join(backup_dir, file_name)
    with open(file_path, 'w') as file:
        file.write("This is a backup file.")
    print(f"File '{file_name}' created in '{backup_dir}'.")
create_folder("backup_folder")
create_file_in_backup_folder("backup_folder", "backup_file.txt")