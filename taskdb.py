# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:06:03 2021

@author: lenovo
"""

import psycopg2
import todbkeys as dbkeys



def add_to_db(task_name,task_date, prioirty_value, task_state):
    conn = dbkeys.connect_todb()
    cur = conn.cursor()
    print("all fine")
    cur.execute("INSERT INTO \"Todo\" VALUES (%s,%s,%s,%s)",(task_name,task_state, prioirty_value, task_date))
    conn.commit()
    print("Inserted")
    cur.close()
    conn.close()
    
def update_db():
    pass

def delete_task():
    pass
def search_db(search_parameter):
    conn =  dbkeys.connect_todb()
    cur = conn.cursor()
    
    if(search_parameter=="1"):
        word=input("Enter keyword : ")
        cur.execute("Select * FROM \"Todo\" WHERE \"Task List\" =(%s)",(word))
        conn.commit()
        
    elif(search_parameter=="2"):
        word=input("Enter keyword : ")
        cur.execute("Select * FROM \"Todo\" WHERE  \"Status\"=(%s)",(word))
        conn.commit()
        
    elif(search_parameter=="3"):
        word=input("Enter keyword : ")
        cur.execute("Select * FROM \"Todo\" WHERE  \"Priority\"=(%s)",(word))
        conn.commit()
        
    elif(search_parameter=="4"):
        word=input("Enter keyword : ")
        cur.execute("Select * FROM \"Todo\" WHERE  \"Date\"=(%s)",(word))
        conn.commit()
      
    else:
        print("Invalid  choice ! Please enter the correct choice..")
                                                                   
              
    tab = cur.fetchmany()
    cur.close()
    conn.close()
    if(tab != []):
        print("Data found",tab) 
    else:
        print("No such task found ")
    
if(__name__ =="__main__"):
    conn =  dbkeys.connect_todb()
    cur = conn.cursor()
    #print("all fine")
    cur.execute(" SELECT * FROM \"Todo\" ")
    tab = cur.fetchone()
    print(tab)
    
    #print("Inserted")
    cur.close()
    conn.close()
