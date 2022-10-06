import shutil
import os
import json

def check(name, login = ''):
    with open('C://Users//egrli//File_manager//settings.json') as f:
        root_dir = json.load(f)
    if login:
        if '\\'.join(name.split('\\')[:4]) == root_dir['working directory'] +'\\' + login:
            return True
    else:
        if '\\'.join(name.split('\\')[:3]) == root_dir['working directory'] :
            return True
        else:
            return False
    

def create_directory(name = '', login = ''):
    try:
        os.mkdir(name)
        change_directory(os.getcwd() + '\\' + login)
        print('Done!')
    except FileExistsError:
        print('Directory with a such name is already exists!')

        
def delete_directory(name):
    try:
        try:
            os.rmdir(os.getcwd() + '\\' + name)
            print('Done!')
        except OSError:
            shutil.rmtree(os.getcwd() + '\\' + name)
        print('Done!')
    except FileNotFoundError:
        print("This directory does not exists!")

        
        
def create_file(name, text = None):
    with open(os.getcwd() + '\\' + name, 'w', encoding = 'utf-8') as f:
        if text:
            f.write(text)

            
def add_text_to_file(name, text):
    try:
        with open(os.getcwd() + '\\' + name, mode='a', encoding='utf8') as f:
            f.write(text)
        print('Done!')
    except FileNotFoundError:
        print("This directory does not exists!")
        
        

def change_directory(new_directory, login = ''):
    if check(new_directory + '\\' + login) == 1:
        try:
            os.chdir(new_directory)
            print('Done!')
        except FileNotFoundError:
            print('Such directory does not exists!')
    else:
        print('You went olut of the root directory!')
    

        
        
def show_text_file(file_name):
    try:
        with open(os.getcwd() + '\\' + file_name, mode='r', encoding='utf8') as f:
            print(f.read())
        print('Done!')
    except FileNotFoundError:
        print("This directory does not exists!")

        
def delete_file(file_name):
    try:
        os.remove(os.getcwd() + '\\' + file_name)
        print('Done!')
    except FileNotFoundError:
        print("This directory does not exists!")

        
def move_file(file_name, destination_path):
    try:
        os.replace(os.getcwd() + '\\' + file_name, destination_path)
        print('Done!')
    except FileNotFoundError:
        print("This directory does not exists!")
    
    
    
def copy_files(name, new_name, new_dir = None):
    try:
        if os.path.isdir(name):
            try:
                shutil.copytree(os.getcwd() + '\\' + name, os.getcwd() + '\\' + new_name)
                print('Done!')
            except FileExistsError:
                print('Error! Folder with this name is existed')
        else:
            shutil.copy(os.getcwd() + '\\' + name, os.getcwd() + '\\' + new_name)
        if new_dir:
            move_file(os.getcwd() + '\\'  + new_name, new_dir)
        print('Done!')
    except FileNotFoundError:
        print("This file doesn't exist!")
        

def rename_file(name, new_name):
    try:
        os.rename(os.getcwd() + '\\' + name, os.getcwd() + '\\' + new_name)
        print('Done!')
    except FileNotFoundError:
        print("This directory does not exists!")
        
        

def processing(command):
    if command == "Create Folder":
        folder_name = input('Input the folder name\n')
        create_directory(folder_name)
        
    elif command == "Delete Directory":
        folder_name = input('Input the folder name\n')
        delete_directory(folder_name)
        
    elif command == "Create File":
        file_name = input('Input the file name\n')
        create_file(file_name)
        
    elif command == "Add Text To File":
        file_name = input('Input the file name\n')
        text_ = input('Input text\n')
        add_text_to_file(file_name, text_)
        
    elif command == "Change Directory":
        new_dir = input('Input the new directory\n')
        print(new_dir)
        change_directory(new_dir)
        
    elif command == "Show Text File":
        file_name = input('Input the file name\n')
        show_text_file(file_name)
        
    elif command == "Delete File":
        file_name = input('Input the file name\n')
        delete_file(file_name)
        
    elif command == "Move File":
        source_path = input('Input source path\n')
        destination_path = input('Input destination path\n')
        move_file(source_path, destination_path)
        
    elif command == "Copy Files":
        name = input('Input name\n')
        new_name = input('Input NEW name\n')
        new_dir = input('Input new_dir (Do not enter anything if you want to create copy in temporary folder) \n')
        copy_files(name, new_name, new_dir)
        
    elif command == "Rename File":
        name = input('Input name\n')
        new_name = input('Input NEW name\n')
        rename_file(name, new_name)
      
    
def new_user(login_, password):
    d = {}
    with open("D:\\Python_projects\\Root_File_Manager\\users.txt", 'r') as f:
        for row in f:
            print(row)
            a, b = row.split(':')
            d[a] = b.rstrip()
    if login_ in d.keys():
        print('User with this name already exists!')
    else:
        with open("D:\\Python_projects\\Root_File_Manager\\users.txt", 'a') as f:
            line = str(login_) + ':' + str(password) + '\n'
            f.writelines(line)
        create_directory(name = login_, login = login_)
        

def log_in():
    d = {}
    with open("D:\\Python_projects\\Root_File_Manager\\users.txt", 'r') as f:
        for row in f:
            a, b = row.split(':')
            d[a] = b.rstrip()
    count = 0
    login_ = input('Input Login \n')
    while True:
        password = input('Input password \n')
        if password == d[login_]:
            change_directory("D:\\Python_projects\\Root_File_Manager" + "\\" + login_)
            break
        else:
            print('Wrong password')
            continue