from functions import get_todos, write_todos
import PySimpleGUI as gui

label=gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip='Enter Todo', key='todo')

add_button = gui.Button("Add")
edit_button = gui.Button("Edit")
compete_button = gui.Button("Complete")

window = gui.Window('To-Do App', 
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos(todos)
        case gui.WIN_CLOSED:
            break
            
window.close() 