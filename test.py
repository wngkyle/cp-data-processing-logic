import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import openpyxl
import os

def main():
    user_input = ''
    selected_folder = ''
    while user_input != 'q':
        current_working_dir = os.getcwd()
        print('Current Directory Path:', current_working_dir)
        all_files = os.scandir()
        all_files = list(filter(check_files, all_files))
        for index in range(len(all_files)):
            print(f'({index}) {all_files[index].name}')
        user_input = input('Enter command: ')

        if user_input == 'l':
            os.chdir(f'{current_working_dir}/..')
        elif user_input == 'r':
            directory = input('Choose a directory to forward to: ')
            directory = all_files[int(directory)].name
            os.chdir(f'{current_working_dir}/{directory}')
        elif user_input != 'q':
            selected_folder = all_files[int(user_input)].name
            break
    print(selected_folder)

def check_files(file):
    if file.is_dir() == False or file.name == '.git' or file.name == '__pycache__' or file.name == '$RECYCLE.BIN' or file.name == '.ipynb_checkpoints' or file.name == '.jpeg File':
        return False
    return True

def check_folder(file):
    if file.is_dir() == True:
        return True
    return False

main()


