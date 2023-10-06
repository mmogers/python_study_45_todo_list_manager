import os, time

todoList = []
#constants
ADD = 1
VIEW = 2
REMOVE = 3
EDIT = 4
VIEW_ALL = 1
VIEW_PRIORITY = 2


def printMenu():  #prints menu on clean screen
  os.system("clear")
  print("\033[1;32mTODO List Management System\033[0m\n")
  print("1: Add\n2: View\n3: Remove\n4: Edit\n\033[32m")
  result = int(input())
  print("\033[0m")
  if result == ADD or result == VIEW or result == REMOVE or result == EDIT:
    return result
  else:
    exit("Incorrect input. Bye!")


def myInputPrint(text):  #prints input text with green clolor
  result = input(f"{text} \033[32m")
  print("\033[0m", end="")
  return result


def addTodo():  #adds a new task with due date and priority to the list
  os.system("clear")
  print("Add\n")
  todo = [None, None, None]
  task = myInputPrint("What is it? ")
  due = myInputPrint("When is it due? ")
  priority = myInputPrint("How important (High/Low/Medium)? ")
  if priority.lower() != "high" and priority.lower(
  ) != "low" and priority.lower() != "medium":
    exit("Incorrect input. Bye")
  todo[0] = task.strip().capitalize()
  todo[1] = due.strip().capitalize()
  todo[2] = priority.strip().capitalize()
  print("\nAdded to list")
  time.sleep(2)
  return todo


def viewTodo(todoList):  #shows all the tasks or by priority (High/Medium/Low)
  os.system("clear")
  print("View\n")
  if len(todoList) == 0:
    print("The list is empty!")
    time.sleep(1)
    return
  print("1: View All\n2: View Priority\n")
  result = int(myInputPrint(""))
  if result == VIEW_ALL:
    os.system("clear")
    print("View All\n")
    for row in todoList:
      print(f"{row[0]: <60} | {row[1]: ^10} | {row[2]: ^10} | ")
      print()
  elif result == VIEW_PRIORITY:
    os.system("clear")
    print("View Priority\n")
    priority = myInputPrint("Which priority: ").strip().capitalize()
    print()
    if priority != "Low" and priority != "High" and priority != "Medium":
      exit("Incorrect input. Bye!")
    else:
      for row in todoList:
        if row[2] == priority:
          print(f"{row[0]: <60} | {row[1]: ^10} | {row[2]: ^10} | ")
          print()
      print()
  else:
    exit("Incorrect input. Bye!")
  time.sleep(2)


def removeTodo(todoList):  #removes a task if exists
  os.system("clear")
  print("Remove\n")
  if len(todoList) == 0:
    print("The list is empty!")
    time.sleep(1)
    return
  task = myInputPrint("What would you like to remove: ").strip().capitalize()
  for row in todoList:
    if row[0] == task:
      todoList.remove(row)
      print("\nThe task was removed ")
      time.sleep(1)
      return
  print("\nThe task is not in the list ")
  time.sleep(1)
  return


def editTodo():  #edits existing task
  os.system("clear")
  print("Edit\n")
  if len(todoList) == 0:
    print("The list is empty!")
    time.sleep(1)
    return
  task = myInputPrint("What would you like to edit: ").strip().capitalize()
  for row in todoList:
    if row[0] == task:
      row[0] = myInputPrint("New title: ").strip().capitalize()
      row[1] = myInputPrint("New due date: ").strip().capitalize()
      row[2] = myInputPrint("New priority: ").strip().capitalize()
      if row[2].lower() != "high" and row[2].lower() != "low" and row[2].lower(
      ) != "medium":
        exit("Incorrect input. Bye")
      print("\nUpdated.")
      time.sleep(1)
      return
  print("\nThe task is not in the list ")
  time.sleep(1)
  return


#---------------------START------------
while True:
  menuOption = printMenu()
  if menuOption == 0:  #none
    exit("Incorrect input. Bye!")
  if menuOption == ADD:
    todo = addTodo()
    todoList.append(todo)
    time.sleep(2)
  elif menuOption == VIEW:
    viewTodo(todoList)
  elif menuOption == REMOVE:
    removeTodo(todoList)
  else:  #EDIT
    editTodo()