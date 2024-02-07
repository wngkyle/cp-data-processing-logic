import os
import pandas as pd
from variables import fileDetail
from helper import run_Isc_20mA, run_Turn_off_80mA, run_Turn_off_80mA_HL, run_Rf, run_Rr
import openpyxl

####################################################################################################################################
#                                                           MAIN                                                                   #
####################################################################################################################################

# Agument : n/a
# Start processing data and creating new excel file with results stored in it
def reading_and_processing():
    fileDetail['all_files'] = os.listdir(fileDetail['selected_folder'])
    temp =  fileDetail['all_files'][:]
    index = 0
    for f in temp:
        if f == ".DS_Store":
            fileDetail['all_files'].pop(index)
            continue
        index += 1

    # Enumerating through each file in the folder
    count = 1
    image_x_pos = ['B', 'R', 'AH', 'AX', 'BN']
    image_x = image_x_pos[0]
    image_y = 3
    for fname in fileDetail['all_files']:
        print(f'Processing {fname}........{count}')

        image_x = image_x_pos[count % 5 - 1]
        if count % 5 == 1 and count != 1:
            image_y += 30

        # Setting variables
        fpath = f'{fileDetail["selected_folder"]}/{fname}'
        newfpath = f'{fileDetail["fdpath"]}/{fname}x'
        findex = fname.find('-')+1

        # Read in the file as a data frame using pandas
        fileDetail['first_df'] = pd.read_excel(fpath, sheet_name=0)
        fileDetail['second_df'] = pd.read_excel(fpath, sheet_name=1)
        fileDetail['df'] = pd.read_excel(fpath, sheet_name=2)

        # Write original data into a new file or just create a new file depneding on whether this is a rush processing
        if fileDetail['fast_track'] == True:
            wb = openpyxl.Workbook()
            wb.save(newfpath)
        else:
            with pd.ExcelWriter(newfpath, engine='openpyxl') as writer:
                fileDetail['first_df'].to_excel(writer, sheet_name='Summary Information', index=False)
                fileDetail['second_df'].to_excel(writer, sheet_name='Statistics Information', index=False)
                fileDetail['df'].to_excel(writer, sheet_name='DUT_Data', index=False)

        if (fileDetail['selected_column']['Isc_20mA'] == 1):
            run_Isc_20mA(fname, findex, newfpath, image_x, image_y)
            print('Isc_20mA Done')
        if (fileDetail['selected_column']['Turn_off_80mA_'] == 1):
            run_Turn_off_80mA(fname, findex, newfpath, image_x, image_y)
            print('Turn_off_20mA Done')
        if (fileDetail['selected_column']['Turn_off_80mA_HL'] == 1):
            run_Turn_off_80mA_HL(fname, findex, newfpath, image_x, image_y)
            print('Turn_off_20mA_HL Done')
        if (fileDetail['selected_column']['Rf'] == 1):
            run_Rf(fname, findex, newfpath, image_x, image_y)
            print('Rf Done')
        if (fileDetail['selected_column']['Rr'] == 1):
            run_Rr(fname, findex, newfpath, image_x, image_y)
            print('Rr Done')
        
        wb = openpyxl.Workbook(newfpath)
        
        count += 1
        break
        
