from functions import get_todos, write_todos
import time 


while True:
  now = time.strftime("%H:%M:%S")
  now = time.strftime("%b %d %Y %I:%M %p")
  print(f'It is {now}')
  user_action = input("Type add, show, edit, complete or exit: ")
  user_action = user_action.strip().lower()

  if user_action.startswith('add'):
      todo = user_action[4:]
      
      todos = get_todos()
      
      todos.append(todo + '\n')
      
      write_todos(todos)

      print(f'Added {todo}')

  elif user_action.startswith('show'):
      todos = get_todos()

      for index, item in enumerate(todos):
          item = item.strip('\n')
          row = f'{index + 1}-{item}'
          print(row)
  
  elif user_action.startswith('edit'):
    try:
      todos = get_todos()
          
      edit_input = user_action[5:]
      edit_index = int(edit_input) - 1
    
      if 0 <= edit_index < len(todos):
          new_text = input("Enter the new text: ")
          todos[edit_index] = new_text + '\n'
          
          write_todos(todos)
          
          print("Item edited successfully.")
      else:
          print("Invalid index. Please try again.")
    except:
      print('Please enter the Index of the item.')
  
  elif user_action.startswith('complete'):
    try:
      todos = get_todos()
            
      number=(user_action[9:])
      if number == 'all':
        todos_remove = todos.copy()
        todos.clear()
        
        write_todos(' ')
      else:
        number = int(number)
        index = number - 1
        
        if 0 <= index < len(todos):
          todos_remove = todos.pop(index)
          
          write_todos(todos)
        else:
          print('Invlad index')
          continue
      if number == 'all':
        message = 'All items were removed.'
      else: 
        message = f'{todos_remove.strip()} was removed'
        
      print(message)
    except:
      print('Please enter the Index of the item.')
    
  elif user_action.startswith('exit'):
    break
  
  else:
    print("Command is not valid.")
  
print("Bye bye")