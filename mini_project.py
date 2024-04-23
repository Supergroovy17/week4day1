
list=[]

def Menu():
   print ('Welcome to the To-Do List App!')
   
   print('''
1. Menu
2. View tasks
3. Delete a task
4. Quit
  ''')
   
   
def add_to_list(item):
   list.append(item)
   print('{} was added to your To Do List!'.format(item))
   print('You have {} items on your list.'.format(len(list))) 

def show_list():
   print('My To Do List:')
   for item in list:
      print(item)

def delete_from_list():
   while True:
      try:
         delete_me = input('What item do you want to remove? ')
         if delete_me in list:
            list.remove(delete_me)
            print("{} has been removed from the list.".format(delete_me))
            Menu()
            break
         else:
            raise ValueError('an item')
      except ValueError as ve:
         if 'an item' in str(ve):
            print(f'Invalid item, no {delete_me}(s) in your list!')
         
         break
#my else block is not working 
def quit():
   print ('good bye!')
show_list()
Menu()
      
 #------------------------------------------------------------------------------------------  
while True:
   new_item = input('New Task>>> ')
   if new_item == '4':
      quit()
      break
   elif new_item == '3':
         show_list()
         delete_from_list()
         continue
   elif new_item == '2':
         show_list()
         continue
   elif new_item == '1':
         Menu()
   else:
      add_to_list(new_item)
      show_list()


