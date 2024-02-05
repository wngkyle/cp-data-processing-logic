import os
import pandas as pd
from variables import fileDetail

####################################################################################################################################
#                                                          UTIL                                                                    #
####################################################################################################################################

# Argument : dataFrame 
# Prints out all available headers, mark each out starting from index 0
def display_all_column_names():
    index = 0
    fname = 'ES02459-02-AID_2023-08-15_02_07_17.xls'
    df = pd.read_excel(f'./{fileDetail["selected_folder"]}/{fname}', sheet_name=2)
    for col in df.columns:
        print(f'({index}) {col}')
        fileDetail['all_column_headers'].append(col)
        fileDetail['selected_column'][col] = 0
        index += 1
    user_input = ''
    while(user_input != 'q'):
        user_input = input('Enter index of the column you want to process (press "q" to quit): ')
        if (user_input != 'q'):
            fileDetail['selected_column'][fileDetail['all_column_headers'][int(user_input)]] = 1

def display_column_names():
    fileDetail['all_column_headers'] = ['Isc_20mA', 'Turn_off_80mA_', 'Turn_off_80mA_HL', 'Rf', 'Rr']
    fileDetail['selected_column'] = {
        'Isc_20mA': 0,
        'Turn_off_80mA_': 0,
        'Turn_off_80mA_HL': 0,
        'Rf': 0,
        "Rr": 0,
    }
    index = 0
    for col in fileDetail['all_column_headers']:
        print(f'({index}) {col}')
        index += 1
    user_input = ''
    count = 0
    while(user_input != 'q' and count != len(fileDetail['all_column_headers'])):
        user_input = input('Enter index of the column you want to process (press "q" to quit): ')
        if (user_input != 'q'):
            fileDetail['selected_column'][fileDetail['all_column_headers'][int(user_input)]] = 1
            count += 1

# Argument : n/a
# Prints out all available folders in current working directory
def folder_selection():
    listOfDirectories = os.listdir()
    temp = listOfDirectories[:]
    index = 0
    for f in temp:
        if f == '.DS_Store' or f.find('.') != -1 or f == '__pycache__':
            listOfDirectories.pop(index)
            continue
        print(f"({index}) {f}")
        index += 1
    folder = input('Select the folder by entering its index: ')
    fileDetail['selected_folder'] = listOfDirectories[int(folder)]
    fileDetail['fdpath'] = f'{fileDetail["selected_folder"]}_Processed'
    # Folder Creation
    # copy_directory_command = f'cp -r {fileDetail["selected_folder"]} {fileDetail["fdpath"]}'
    # os.popen(copy_directory_command)
    os.mkdir(fileDetail['fdpath'])

# Argument : n/a 
# Prompt the user to select the directory store processed files
def file_download_selection():
    print('(0) Desktop')
    print('(1) Downloads')
    temp = input('Select a location to store processed files by entering index: ')
    if temp == 0:
        fileDetail['file_download_path'] = os.path.join(os.path.expanduser('~'), 'Desktop')
    else:
        fileDetail['file_download_path'] = os.path.join(os.path.expanduser('~'), 'Downloads')