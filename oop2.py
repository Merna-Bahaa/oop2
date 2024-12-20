# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 20:12:26 2023

@author: ascom
"""
###Constructors explanations

class Customer:
     def __init__(self, name, balance):  
        self.name = name
        self.balance = balance
        print("The	init	method was called")
     cust = Customer("Lara de Silva" , 100)   
     print(cust.name) 
     print(cust.balance) 
class Customer:
    def	__init__(self, name, balance=0):  
         self.name = name
         self.balance = balance
         print("The	init	method was called")
         cust = Customer("Lara de Silva") 
    print(cust.balance) 
class Customer:
     def	__init__(self, name, balance=0):  
         self.name = name
         self.balance = balance
         print("The	init	method was called")
             def __str__(self):
         return 'Customer : ' +str(self.name)+ ' , balance: ' + str(self.balance) 
         def __add__(self, other): # On "self + other"
         return Customer("Test_Customer",self.balance + other)
 cust = Customer("Lara de Silva") # <-- don't specify balance explicitly  print(cust.name)
  print(cust.balance) # <-- attribute is created anyway
 print(cust)
 c2 = cust + 230
 print(c2.balance)
class Employee:
	def __init__(self):
		print('Employee created.')
	def __del__(self):
		print('Destructor called, Employee deleted.')
obj = Employee()
del obj

