# Todo
Nothing beats the thrill of writing code  one day before exam.Even though my To Do for the day was to revise the Theory of Computation ,I almost ended up  making a To do backend.
This  is my initial code to make a Todo app. The basic purpose is to Create a database of tasks and have the feature to perform CRUD operations on the Postgres Database.

## Main components
1. To enable user to add/delete/update tasks.
2. To enable user to search existing tasks on the basis of name/priority/status/date.
3. To enable user to update the priority of existing tasks.

## Current State
1. User is able to add tasks to database.
2. User is able to know whether task exist in database.

## Work needed to be done
1. Add ability to update database.
2. Add ability to change priority of tasks.
3. Optimize search mechanism.
4. Refine the way data is displayed.

## Assumption
1. User follows the instructions in correct manner.
2. User is a workaholic who has long todo list which requires database to store it.

## Approach 
 My approach is to take input from the user in a structured manner and so as to eliminate the need of preprocess data to a certain extent.

## DB Schema
The relation "Todo" consists of 4 attributes:
   1. Task list- contains name of tasks.
   2. Status - Contains status of tasks (complete/incomplete).
   3. Priority - Contains Priority of the tasks.
   4. Date - Contains the date of the task created or to be completed.

## How to run this in current state
 The taskdb.py requires a running postgresdb server.
 
 The module todbkeys.py contains the credentials to access database.
 
      Note- todbkeys.py is hidden since its contains database credentials.
      
  One can replace dbkeys.connect_todb() with  psycopg2.connect("dbname= user= ")
  One must start from Oye.py and follow along.
