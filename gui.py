import functions
import PySimpleGUI as gui


label=gui.Text("Type in a To-Do")
input_box=gui.InputText(tooltip="Enter ToDo")
add_button=gui.Button("Add")
# LAYOUT EXPECTS A LIST OF LISTS
# NOTE A LIST INSIDE THE LIST REPRESENT A ROW
win=gui.Window("My ToDo App",
layout=[[label,input_box,add_button]],
font=("Helvetica",15))
# WHEN A BUTTON IS PRESSED THE WINDOW IS CLOSE
#SO WE PUT win.read IN A WHILE LOOP
while True:
    # win.read RETURNS A TUPLE WITH TWO ELEMENTS
    #FIRST ELEMENT IS THE BUTTON NAME
    # 2ND ELEMENT IS A DICTIONARY WITH THE DEFAULT KEY=0 AND VALUE=TEXT IN THE InputText FIELD
    # WE CAN CHANGE THE DEFAULT KEY IF WE WANT
    event,values=win.read() 
    print(event)
    print(values) 

# THIS
    if event == "Add":
        todos=functions.get_todo()
        new_todo=values[0]+'\n'
        todos.append(new_todo) 
        functions.write_todos(todos) 

    else:
        break

win.close()