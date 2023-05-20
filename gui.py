from functions import get_todos, write_todos
import PySimpleGUI as gui

label=gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip='Enter Todo', key='todo')
list_box = gui.Listbox(values=get_todos(), key='todos',
                       enable_events=True, size=[45, 10])

add_button = gui.Button("Add")
edit_button = gui.Button("Edit")
compete_button = gui.Button("Complete")

window = gui.Window('To-Do App', 
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            write_todos(todos)
            
            input_box.update(value="")
            list_box.Update(values=todos)
            
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'
            
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            write_todos(todos)
            
            input_box.update(value="")
            list_box.Update(values=todos)
        case "Complete":
            pass
        
        case "Exit":
            break
        
        case gui.WIN_CLOSED:
            break
            
window.close() 