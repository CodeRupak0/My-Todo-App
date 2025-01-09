import PySimpleGUI as sg
from ziptofile import extract_archive
sg.theme("Black")

label1= sg.Text("Select Archive to extract   ")
input1=sg.Input()
choose1=sg.FileBrowse("CHOOSE", key='Archive')

label2= sg.Text("Select a Destination Folder")
input2=sg.Input()
choose2=sg.FolderBrowse("CHOOSE", key='folder')

extract_button=sg.Button("EXTRACT")
output_label=sg.Text(key='output',text_color= "green")

window=sg.Window("ZIP EXTRACTOR", layout=[[label1, input1, choose1],
                                               [label2, input2, choose2],
                                               [extract_button,output_label]])
while True:
    event, values= window.read()
    print (event, values)
    file_path=values["Archive"]
    dest_directory=values["folder"]
    extract_archive(file_path, dest_directory)
    window["output"].update(value="Extraction Complete")
window.close()