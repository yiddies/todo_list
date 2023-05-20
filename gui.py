from functions import get_todos, write_todos
import PySimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip='Enter Todo', key='todo')
list_box = gui.Listbox(values=[todo.strip() for todo in get_todos()], key='todos',
                       enable_events=True, size=[45, 10])

add_button = gui.Button("Add")
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")

window = gui.Window('To-Do App', 
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()

    if event == "Add":
        todos = get_todos()
        new_todo = values['todo']
        todos.append(new_todo + '\n')
        write_todos(todos)

        input_box.update(value="")
        list_box.update(values=[todo.strip() for todo in todos])

    elif event == "Edit":
        todo_to_edit = values['todos'][0]
        new_todo = values['todo']

        todos = get_todos()
        index = todos.index(todo_to_edit  + '\n')
        todos[index] = new_todo + '\n'
        write_todos(todos)

        input_box.update(value="")
        list_box.update(values=[todo.strip() for todo in todos])

    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])

    elif event == "Complete":
        pass

    elif event == "Exit" or event == gui.WINDOW_CLOSED:
        break

window.close()
