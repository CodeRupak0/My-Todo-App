import functions
import PySimpleGUI as sg      # simple GUI third-party module

label = sg.Text("Type in a to-do")   #
input_box=sg.InputText(tooltip="Enter a Todo", key= "todo")   # creates an input box for typing with "enter a todoo" as prompt message at the input box
add_button= sg.Button("ADD")                # creates a button ADD
list_box= sg.Listbox(values=functions.get_todos(), key='todos',     # creates a list box of Todos and show in the list, key is used to assign dictionary values
                     enable_events=True, size=[45,10])              # key is later used to extract the values from the dictionary for further data manipulation
edit_button= sg.Button("EDIT")
complete_button=sg.Button("COMPLETE")
exit_button=sg.Button("EXIT")

""" This creates a window GUI with title as "My todo app", 
the layout is used to place the GUI commands in the window
placing the command in [" , "] separated by commas place the command in same line"""

window=sg.Window('My To-Do App',
                 layout=[[label],[input_box,add_button],
                         [list_box,edit_button],[complete_button,exit_button]],
                 font=('Helvetica',20))

""" Running the loop while true boolean and executing the command"""

while True:
    event, values= window.read()  #extracting event(ADD,EDIT,COMPLETE etc) and values from the window listbox as todos and inputbox as todo
    print(event)
    print(values)
    match event:
        case "ADD":
            """ When we click ADD button the following case is executed.
                First todos is extracted using gettodos function """
            todos= functions.get_todos()
            new_todo= values['todo']+'\n'  # extract the dictionary associated with values[todo]- typed at input box
            todos.append(new_todo)          # appending and writing to the file
            functions.write_todos(todos)
            list_box = window['todos'].update(values=todos)  #updating the values in the listbox at realtime


            """ when we click the list from the listbox it is assigned to the Values[todos] dictionary and
            as we type in the input box, the input is assigned to the dictionary values[todo]. 
            These are used for further data processing."""


        case "EDIT":
            todo_to_edit= values['todos'][0]   # extracting the dictionary associated to values[todos]- from the listbox
            newtodo=values['todo']              # newtodo is extracted from the input box
            todos=functions.get_todos()
            index=todos.index(todo_to_edit)        # index is extracted
            todos[index]= newtodo+'\n'              # data is override and written to file
            functions.write_todos(todos)
            list_box=window['todos'].update(values=todos)

            """when we click todo from the listbox, its is extracted from the list and is placed in the Input box
            as assigning the dictionary value[todo]= values[todos][0]. updating in realtime. """
        case "todos":
            input_box=window['todo'].update(value=values['todos'][0])

        case "COMPLETE":
            todo_complete= values['todos'][0]
            todos=functions.get_todos()
            todos.remove(todo_complete)
            functions.write_todos(todos)
            list_box=window['todos'].update(values=todos)
            input_box=window['todo'].update(value="")
        case "EXIT":
            break
        case sg.WIN_CLOSED:
            break

window.close()