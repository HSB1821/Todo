# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:59:43 2021

@author: lenovo
"""
import taskdb as td
class Create:

    # create tasks with relevant parameters and add to database
    def __intit__ (self):
        self.task_name=""
        self.task_date=""
        self.prioirty_value=""
        self.task_state=""
   
    def task_create(self,task_name,task_date, prioirty_value, task_state):
        self.task_name=task_name
        self.task_date=task_date
        self.prioirty_value=prioirty_value
        self.task_state=task_state
        print("storing in database")
        self.add_todo()
        
    def add_todo(self):
        td.add_to_db(task_name,task_date, prioirty_value, task_state)

class Task_search:
    # Search task from database  with help of relevanr filters
    def __init__(self):
        self.task_data=[]
        
    def search_task(self,search_parameter):
        if(search_parameter=="1"):
              td.search_db(search_parameter)
        elif(search_parameter=="2"):
              td.search_db(search_parameter)
        elif(search_parameter=="3"):
              td.search_db(search_parameter)
        elif(search_parameter=="4"):
              td.search_db(search_parameter)
        else:
              print("Invalid  choice ! Please enter the correct choice..")
        pass
    pass

class Display_Task:
    #Display the tasks
    pass
      
if(__name__ =="__main__"):
    print(" ************ TO DO ************ ")
    print("1. Add task  ")
    print("2. Search tasks")
    print("3. Display tasks ")
    user_input=input("Enter your choice (1,2...) here : ")
    
    if(user_input=="1"):
      
        task_name=input(" Enter the name of task : ")
        task_date=input(" Enter the date of task : ")
        prioirty_value=input(" Enter Priority \(top,normal. low \) :")
        task_state=input(" Status of current task : ")
        input_handler = Create()
        input_handler.task_create(task_name,task_date, prioirty_value, task_state)
   
    elif(user_input=="2"):
      
        
        search_handler =Task_search()
        
        print(" ************ SEARCH ************ ")
        print("1. By name ")
        print("2. By status")
        print("3. By priority  ")
        print("4. By date ")
        search_parameter=input("Enter Parameter choice (1,2,3...) here : ")
        search_handler.search_task(search_parameter)
   
    elif(user_input=="3"):
       
        display_handler =Display_Task()
   
    else:
  
        print("Invalid  choice ! Please enter the correct choice..")