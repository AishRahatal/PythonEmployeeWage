'''	
@Author: Aishwarya
@Date: 2021-11-24
@Title : Employee Wage Computation Problem
'''
########################################################################################################
#added random module to use random functions
import random

class Employee:
    #self parameter is a reference to current instance of class
    def __init__(self):
        """"
        Description: It is method to initialize object
        Parameter: self
        Return: none
        """
        #to avoid getting error cause class has defined with no content 
        pass

    def attendance(self):
        """"
        Description: checking  employee present or absent using random function
        Parameter: self
        Return: none
        """
        # p variable storing result of random function randint() which generates value 0 or 1
        p=random.randint(0,1)
        #try block contains operations
        try:
        #inline if case statement with match case to get result according to condition 
            match p :
                # if value of p is 1 then emplyee present
                case p if p == 1:
                    print("Employee present")
                # if value of p is 0 then emplyee absent
                case p if p==0:
                    print("Employee absent")
        #except block will execute if error occurs in try block             
        except Exception as e:
            print("Error :",e)

    def daily_wage(self):
        """"
        Description: checking  employee present and full time then calculating a day wage,
        using hours for day is 8 and per hour rate is 20
        Parameter: self
        Return: none
        """
        #try block contains operations
        try:
            # setting rate per hour is 20            
            rate_per_hour= 20
            full_time=1    
            #if emloyee is full time then set hours =8
            if full_time:
                    #hours for a day
                    hours = 8
                    #declare wage as protected variable
                    _wage = hours * rate_per_hour
                    print("Employee daily wage: " ,_wage)
                    print()            
            else:
                print("Employee is not full time ")            
        except Exception as e:
            print("Error :",e)  

            
# main for function call.
if __name__ == "__main__": 

    print("Employee Wage Computation Problem")
    print("------------------------------------")
    # created object e to access functions of class
    try:
        e=Employee()
        #calling a function using object e
        choice=None
        while choice !=0:
            #menu 
            print("---Menu----")
            print("1. Attendance")
            print("2. Daily wage")
            print("0. Exit")
            print("----------------")
            choice=int(input("Enter choice :"))
            #match case to choose function call
            match choice:
                case 1:
                    e.attendance()
                case 2:
                    e.daily_wage()     
                case default:
                    print("please enter value between 1 and 2")    
                    print()
            
    except:
         print("Entered wrong value") 

    
