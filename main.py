import json
import os
import filemanager as fm


with open('C://Users//egrli//File_manager//settings.json') as f:
    d = json.load(f)
    
fm.change_directory(d['working directory'])


d = ["1. Create Folder",
     "2. Delete Directory",
     "3. Create File", 
    "4. Add Text To File",
    "5. Change Directory", 
    "6. Show Text File",
    "7. Delete File", 
    "8. Move File",
    "9. Copy Files",
    "10. Rename File",
    "11. STOP"]


intro = input('Log In or Registration \n')
if intro == "Log In":
    fm.log_in()
if intro == "Registration":
    name = input('Input login\n')
    password = input('password\n')
    
    
print('LIST OF COMMANDS\n','\n\n'.join(d))

command = input("Input Command")

while command != 'STOP':
    fm.processing(command)
    command = input("Input Command")
    
    
print("The work of a filemanager is finished!")