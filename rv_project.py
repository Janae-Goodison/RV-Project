"""[Janae Goodison] Each robot will be assigned some tasks based on their type."""


from typing import List, Dict
from pandas import DataFrame
import pandas as pd
import csv, time, datetime
from time import time
from tabulate import tabulate 
 

UNIPEDAL: str = "unipedal"
BIPEDAL: str = "bipedal"
QUADRUPEDAL: str = "quadrupedal"
ARACHNID: str = "arachnid"
RADIAL: str = "radial"
AERONAUTICAL: str = "aeronautical"

list_of_types: List[str] = [UNIPEDAL, BIPEDAL, QUADRUPEDAL, ARACHNID, RADIAL, AERONAUTICAL]

input_name: str = input("Hello! What's the name of your robot? ")
print(input_name)
print(" ")

print("There are 6 different type of robots to choose from:")
print(tabulate([list_of_types]))

tasks = ["mow the lawn", "rake the leaves", "give the dog a bath", "bake some cookies", "wash the car", 
        "do the dishes", "do the laundry", "take out the recycling", "make a sammich", "sweep the house"]

def add_task(list_of_tasks: List[Dict[str,str]]) -> None:
    """Adds another task to the already established list"""
    given_input = input(str("Would you like to assign an additional task to " + input_name + "? ")) 
    if given_input == "yes":
        key = input("Please input your wanted task: ")
        given_task = {"description": key, "eta": "25000"}
        list_of_tasks.append(given_task)
        add_task(list_of_tasks)
    if given_input == "no":
        print("Okay")

# Checks which robot the user chooses
for robot_type in list_of_types:
    input_type: str = input("What kind of robot is " + input_name +"? ")
    if input_type == UNIPEDAL.lower() or UNIPEDAL.upper(): 
        completed_tasks: List[Dict] = []
        # Assigned tasks
        uni_tasks: List[Dict] = [
            {"description": "mow the lawn", "eta": "20000"},
            {"description": "rake the leaves", "eta": "18000"},
            {"description": "give the dog a bath", "eta": "14500"},
            {"description": "bake some cookies", "eta": "8000"},
            {"description": "wash the car", "eta": "20000"}
            ] 
        # Gives the user the option to add tasks
        add_task(uni_tasks)
        # Prints all of the tasks the robot will complete 
        print(" ")
        print(input_name + " will complete the tasks below: ")
        for task_index in range(0, len(uni_tasks)):
            print("> " + uni_tasks[task_index]["description"])
        answer = input("Are all your tasks listed? (please answer yes or no) ")
        if answer == "yes":
            ...
        if answer == "no":
            add_task(uni_tasks)
        print(" ")
        # Starting the timer at when the robot starts it's tasks.
        start_time = time()
        total_eta: int = 0
        # Moves the indexed tasks from the original list to the completed task list
        for task_index in range(0, len(uni_tasks)):
            task_index = 0
            total_eta = total_eta + int(uni_tasks[task_index]["eta"]) 
            completed_tasks.append(uni_tasks[task_index])
            uni_tasks.pop(task_index) 
        # Ending the timer at when the robot completes all the tasks.
        end_time = time()
        #print(end_time)
        elapsed_time = end_time - start_time
        milliseconds = elapsed_time * 1000
        # create a table 
        print(" ")
        print("      Completed Tasks       ")
        print("**************************")
        print(tabulate(completed_tasks, headers="keys"))
        print(" ")
        print("Done! Thank you for choosing " + input_name + ", have a nice day.")
        print("Tasks completed in: " + str(milliseconds) + " milliseconds")
        print("Total eta of tasks: " + str(total_eta) + "  milliseconds")
        break

    elif input_type == BIPEDAL.lower() or BIPEDAL.upper():
        total_eta: int 
        completed_tasks: List[Dict] = []
        bi_tasks: List[Dict] = [
            {"description": "do the dishes", "eta": "1000"}, 
            {"description": "sweep the house", "eta": "3000"},
            {"description": "do the laundry", "eta": "10000"},
            {"description": "take out the recycling", "eta":"4000"},
            {"description": "make a sammich", "eta": "7000"},
            ]
        # Gives the user the option to add tasks
        add_task(bi_tasks)
        # Prints all of the tasks the robot will complete 
        print(" ")
        print(input_name + " will complete the tasks below: ")
        for task_index in range(0, len(bi_tasks)):
            print("> " + bi_tasks[task_index]["description"])
        answer = input("Are all your tasks listed? (please answer yes or no) ")
        if answer == "yes":
            ...
        if answer == "no":
            add_task(bi_tasks)
        print(" ")
        # Starting the timer at when the robot starts it's tasks.
        start_time = time()
        total_eta: int = 0
        for task_index in range(0, len(bi_tasks)):
            task_index = 0
            total_eta = total_eta + int(bi_tasks[task_index]["eta"]) 
            completed_tasks.append(bi_tasks[task_index])
            bi_tasks.pop(task_index) 
        # Ending the timer at when the robot completes all the tasks.
        end_time = time()
        # print(end_time)
        elapsed_time = end_time - start_time
        milliseconds = elapsed_time * 1000
        # create a table 
        print(" ")
        print("      Completed Tasks       ")
        print("**************************")
        print(tabulate(completed_tasks, headers="keys"))
        print(" ")
        print("All done. Thank you for choosing " + input_name + ", have a nice day!")
        print("total eta: " + str(total_eta) )
        print("Tasks completed in: " + str(milliseconds) + " milliseconds")
        print("Total eta of tasks: " + str(total_eta) + "  milliseconds")
        break

    elif input_type == QUADRUPEDAL.upper() or QUADRUPEDAL.lower():
        total_eta: int 
        completed_tasks: List[Dict] = []
        quad_tasks: List[Dict] = [
            {"description": "do the dishes", "eta": "1000"},
            {"description": "do the laundry", "eta": "10000"},
            {"description": "make a sammich", "eta": "7000"},
            {"description": "rake the leaves", "eta": "18000"},
            {"description": "bake some cookies", "eta": "8000"},
            ]
        # Gives the user the option to add tasks
        add_task(quad_tasks)
        # Prints all of the tasks the robot will complete 
        print(" ")
        print(input_name + " will complete the tasks below: ")
        for task_index in range(0, len(quad_tasks)):
            print("> " + quad_tasks[task_index]["description"])
        answer = input("Are all your tasks listed? (please answer yes or no) ")
        if answer == "yes":
            ...
        if answer == "no":
            add_task(quad_tasks)
        print(" ")
        # Starting the timer at when the robot starts it's tasks.
        start_time = time()
        total_eta: int = 0
        for task_index in range(0, len(quad_tasks)):
            task_index = 0
            total_eta = total_eta + int(quad_tasks[task_index]["eta"]) 
            completed_tasks.append(quad_tasks[task_index])
            quad_tasks.pop(task_index) 
        # Ending the timer at when the robot completes all the tasks.
        end_time = time()
        print(end_time)
        elapsed_time = end_time - start_time
        milliseconds = elapsed_time * 1000
        # create a table 
        print("      Completed Tasks       ")
        print("**************************")
        print(tabulate(completed_tasks, headers="keys"))
        print("All done. Thank you for choosing " + input_name + ", have a nice day!")
        print("total eta: " + (str(total_eta)))
        print("Tasks completed in: " + str(milliseconds) + " milliseconds")
        print("Total eta of tasks: " + str(total_eta) + "  milliseconds")
        break
        
    elif input_type == ARACHNID.upper() or ARACHNID.lower():
        total_eta: int 
        completed_tasks: List[Dict] = []
        ara_tasks: List[Dict] = [ 
            {"description": "sweep the house", "eta": "3000"},
            {"description": "take out the recycling", "eta":"4000"},
            {"description": "mow the lawn", "eta": "20000"},
            {"description": "give the dog a bath", "eta": "14500"},
            {"description": "wash the car", "eta": "20000"}
            ]
        # Gives the user the option to add tasks
        add_task(ara_tasks)
        # Prints all of the tasks the robot will complete 
        print(" ")
        print(input_name + " will complete the tasks below: ")
        for task_index in range(0, len(ara_tasks)):
            print("> " + ara_tasks[task_index]["description"])
        answer = input("Are all your tasks listed? (please answer yes or no) ")
        if answer == "yes":
            ...
        if answer == "no":
            add_task(ara_tasks)
        print(" ")
        # Starting the timer at when the robot starts it's tasks.
        start_time = time()
        total_eta: int = 0
        for task_index in range(0, len(ara_tasks)):
            task_index = 0
            total_eta = total_eta + int(ara_tasks[task_index]["eta"]) 
            completed_tasks.append(ara_tasks[task_index])
            ara_tasks.pop(task_index) 
        # Ending the timer at when the robot completes all the tasks.
        end_time = time()
        print(end_time)
        elapsed_time = end_time - start_time
        milliseconds = elapsed_time * 1000
        # create a table 
        print("      Completed Tasks       ")
        print("**************************")
        print(tabulate(completed_tasks, headers="keys"))
        print("All done! Thank you for choosing " + input_name + ", have a nice day. ARA")
        print("total eta: " + str(total_eta))
        print("Tasks completed in: " + str(milliseconds) + " milliseconds")
        print("Total eta of tasks: " + str(total_eta) + "  milliseconds")
        break

    elif input_type == RADIAL.upper() or RADIAL.lower():
        total_eta: int 
        completed_tasks: List[Dict] = []
        rad_tasks: List[Dict] = [
            {"description": "do the dishes", "eta": "1000"}, 
            {"description": "sweep the house", "eta": "3000"},
            {"description": "give the dog a bath", "eta": "14500"},
            {"description": "bake some cookies", "eta": "8000"},
            {"description": "wash the car", "eta": "20000"}
            ]
        # Gives the user the option to add tasks
        add_task(rad_tasks)
        # Prints all of the tasks the robot will complete 
        print(" ")
        print(input_name + " will complete the tasks below: ")
        for task_index in range(0, len(rad_tasks)):
            print("> " + rad_tasks[task_index]["description"])
        answer = input("Are all your tasks listed? (please answer yes or no) ")
        if answer == "yes":
            ...
        if answer == "no":
            add_task(rad_tasks)
        print(" ")
        # Starting the timer at when the robot starts it's tasks.
        start_time = time()
        total_eta: int = 0
        for task_index in range(0, len(rad_tasks)):
            task_index = 0
            total_eta = total_eta + int(rad_tasks[task_index]["eta"]) 
            completed_tasks.append(rad_tasks[task_index])
            rad_tasks.pop(task_index) 
        # Ending the timer at when the robot completes all the tasks.
        end_time = time()
        print(end_time)
        elapsed_time = end_time - start_time
        milliseconds = elapsed_time * 1000
        # create a table 
        print("      Completed Tasks       ")
        print("**************************")
        print(tabulate(completed_tasks, headers="keys"))
        print("All done! Thank you for choosing " + input_name + ", have a nice day. RAD")
        print("total eta: " + str(total_eta) )
        print("Tasks completed in: " + str(milliseconds) + " milliseconds")
        print("Total eta of tasks: " + str(total_eta) + "  milliseconds")
        break 

    elif input_type == AERONAUTICAL.upper() or AERONAUTICAL.lower():
        total_eta: int 
        completed_tasks: List[Dict] = []
        aero_tasks: List[Dict] = [
            {"description": "do the laundry", "eta": "10000"},
            {"description": "take out the recycling", "eta": "4000"},
            {"descirption": "rake the leaves", "eta": "18000"},
            {"description": "give the dog a bath", "eta": "14500"},
            {"description": "wash the car", "eta": "20000"}
            ]
        # Gives the user the option to add tasks
        add_task(aero_tasks)
        # Prints all of the tasks the robot will complete 
        print(" ")
        print(input_name + " will complete the tasks below: ")
        for task_index in range(0, len(aero_tasks)):
            print("> " + aero_tasks[task_index]["description"])
        answer = input("Are all your tasks listed? (please answer yes or no) ")
        if answer == "yes":
            ...
        if answer == "no":
            add_task(aero_tasks)
        print(" ")
        # Starting the timer at when the robot starts it's tasks.
        start_time = time()
        total_eta: int = 0
        for task_index in range(0, len(aero_tasks)):
            task_index = 0
            total_eta = total_eta + int(aero_tasks[task_index]["eta"]) 
            completed_tasks.append(aero_tasks[task_index])
            aero_tasks.pop(task_index) 
        # Ending the timer at when the robot completes all the tasks.
        end_time = time()
        print(end_time)
        elapsed_time = end_time - start_time
        milliseconds = elapsed_time * 1000   
        # create a table 
        print("      Completed Tasks       ")
        print("**************************")
        print(tabulate(completed_tasks, headers="keys"))
        print("All done! Thank you for choosing " + input_name + ", have a nice day. AERO")
        print("total eta: " + str(total_eta))
        print("Tasks completed in: " + str(milliseconds) + " milliseconds")
        print("Total eta of tasks: " + str(total_eta) + "  milliseconds")
        break

    else:
        print("Invalid robot type: please choose from the list given.")
    continue
