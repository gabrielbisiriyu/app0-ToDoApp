import functions
import PySimpleGUI as gui
import time

gui.theme("Dark")
clock=gui.Text("",key="clock")
label=gui.Text("Type in a To-Do")
input_box=gui.InputText(tooltip="Enter ToDo",key="todo")
add_button=gui.Button("Add")
list_box=gui.Listbox(values=functions.get_todo(),key="todos",
enable_events=True,size=[45,10])
edit_button=gui.Button("Edit")
complete_button=gui.Button("Complete")
exit_button=gui.Button("Exit",button_color="red")
# LAYOUT EXPECTS A LIST OF LISTS
# NOTE A LIST INSIDE THE LIST REPRESENT A ROW
win=gui.Window("My ToDo App",
layout=[[clock],[label,input_box,add_button],[list_box,edit_button,complete_button],[exit_button]],
font=("Helvetica",15))
# WHEN A BUTTON IS PRESSED THE WINDOW IS CLOSE
#SO WE PUT win.read IN A WHILE LOOP
while True:
    # win.read RETURNS A TUPLE WITH TWO ELEMENTS
    #FIRST ELEMENT IS THE BUTTON NAME
    # 2ND ELEMENT IS A DICTIONARY WITH THE DEFAULT KEY=0 AND VALUE=TEXT IN THE InputText FIELD
    # WE CHANGE THE DEFAULT KEY TO todo
    event,values=win.read(timeout=200) 
    # WE ADDED THE TIMEOUT FEATURE SO THAT IT COULD DISPLAY THE TIME AS IT READS
    win["clock"].update(value=time.strftime("%d %b, %Y %H:%M:%S"))
    #print(event)
    #print(values)

# THIS
    if event == "Add":
        todos=functions.get_todo()
        new_todo=values["todo"]+'\n'
        todos.append(new_todo)
        functions.write_todos(todos)
        # TO UPDATE THE LIST BOX IMMEDIATELY
        win["todos"].update(values=todos)
    elif event == "Edit":
        try:
            edit=values["todos"][0]
        except:
            gui.popup("Please select a ToDo to edit")
            continue
        new_todo=values["todo"]
        todos=functions.get_todo()
        index=todos.index(edit)
        todos[index]=new_todo
        functions.write_todos(todos)
        win["todos"].update(values=todos)
    elif event=="todos":
        win["todo"].update(value=values["todos"][0])
    elif event=="Complete":
        todos=functions.get_todo()
        try:
            v=values["todos"][0]
        except:
            gui.popup("Please select a ToDo to complete")

        todos.remove(v)
        functions.write_todos(todos)
        win["todos"].update(values=todos)


    elif event=="Exit":
        break

    elif event== gui.WIN_CLOSED:
        break

win.close()
