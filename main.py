import sqlite3
import os
from time import sleep

con = sqlite3.connect("app.db")
cur = con.cursor()


def getTasks(order=None):

    if order == "status":
        resData = cur.execute("SELECT * FROM tasks WHERE status = 'incomplete';")

    else:
        resData = cur.execute("SELECT * FROM tasks;")

    return resData


def checkEmpty():
    tasks = getTasks().fetchall()
    if len(tasks) < 1:
        return True


def showTasks(
    showOrder="standard",
):  # function to fetch all tasks from database and print them on console
    os.system("cls")

    if checkEmpty() == True:
        input("The list is empty...")
        mainMenu()

    tasksToList = getTasks(showOrder).fetchall()

    for task in tasksToList:
        print(f"{task[0]}. {task[1]} | Status: {task[2]}")
    input("")


def addTask():  # function to basically add user specified task to the database
    os.system("cls")
    task_name = input("Task name: ")
    cur.execute(f"INSERT INTO tasks (name) VALUES ('{task_name}')")
    con.commit()
    input("Task added successfuly!")


def removeTask():  # function to remove task entry in database based on its id
    showTasks()
    try:
        task_id = int(input("\nTask to remove (ID): "))
    except TypeError:
        print("Must be a number!")
        input("...")
        removeTask()

    cur.execute(f"DELETE FROM tasks WHERE id = {task_id}")
    con.commit()
    input(f"Task {task_id} Deleted Successfuly")


def completeTask():  # function to change status of task to completed based on id
    showTasks()
    try:
        task_id = int(input("\nTask to complete (ID): "))
    except TypeError:
        print("Must be a number!")
        input("...")
        removeTask()

    cur.execute(f"UPDATE tasks SET status = 'completed' WHERE id = {task_id}")
    con.commit()
    input(f"Task completed successfuly!")


def orderMenu():  # Function to handle the option to list entries by specific orer

    os.system("cls")
    print("Order entries by:")
    print("1. Standard\n2. Incomplete")

    try:
        user_input = int(input("Option: "))
    except TypeError:
        print("Option must be a number!")
        orderMenu()

    if user_input == 1:
        showTasks()

    else:
        showTasks("status")


def optionHandler(opt=None):  # handler of mainMenu function options

    match opt:
        case 1:
            addTask()
        case 2:
            orderMenu()
        case 3:
            completeTask()
        case 4:
            removeTask()


def mainMenu():  # Main Menu basically

    while True:
        os.system("cls")
        print("To-do App")
        print("What do you want to do:\n1. Add\n2. Show\n3. Complete\n4. Remove")

        try:
            option = int(input("Option: "))

        except TypeError:
            print("It must be a number!")
            sleep(2)
            continue

        optionHandler(option)


mainMenu()
