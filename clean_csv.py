# import libraries 
import PySimpleGUI as sg

import pandas as pd  

# FIRST WINDOW - select CSV file
file_path = sg.popup_get_file('Select the CSV file you would like to clean')

# convert file_path into pd dataframe
file = pd.read_csv(file_path, sep=',', header=0)

# define window function for windows to keep or delete columns
def new_window(column_name):
    # layout is everything inside the window
    layout = [
        [sg.Text('Would you like to keep column ' + column_name + '?')], # ask user if they want to keep columns
        [sg.Button('Yes'), sg.Button('No')]
    ]

    # create a window
    window = sg.Window('Ampry - CSV Cleaner', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Yes': # if user closes window or if user selects 'yes' to keep
            break
        elif event == 'No':
            global file
            file = file.drop(column_name, axis=1)
            break

    window.close()

# which columns to keep
new_window('subid') 
new_window('created_at')
new_window('fname')
new_window('lname')
new_window('phone')
new_window('email')
new_window('website')

# clean CSV file
for column in file:
    for i in range(len(file)):
        file[column][i] = file[column][i][2:-1]

# get folder where user wants to save file
folder_path = sg.popup_get_folder('Where would you like this new file to be stored?')

# name the new file
new_file_name = sg.popup_get_text('What would you like the new file to be called?')

# export cleaned CSV file to designated folder
file.to_csv(folder_path + '/' + new_file_name + '.csv', sep=',', header=True)

sg.popup('Thanks for using this program! If you had any issues, get mad at Cameron!')