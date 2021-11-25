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

    def part_time(self):
        """"
        Description: calculate wage for part time,
        hours of part time for day hour is 4 and per hour rate is 20
        Parameter: self
        Return: none
        """
       #try block contains operations
        try:
            # setting rate per hour is 20            
            rate_per_hour= 20
            part_time=1    
            #if emloyee is full time then set hours =8
            if part_time:
                    #hours for a day
                    hours = 4
                    #declare wage as protected variable
                    _wage = hours * rate_per_hour
                    print("Employee daily part time wage: " ,_wage)
                    print()            
            else:
                print("Employee is not part time ")            
        except Exception as e:
            print("Error :",e)  
 
    def switch_case(self):
        """"
        Description: Refactor calculate wage for fulltime and part time using switch case
        using hours for day is 8 and part time hour is 4 and per hour rate is 20
        Parameter: self
        Return: none
        """
        rate_per_hour = 20
        time=random.randint(0,1) 
        try: 
            match time:
            # if value of full_time is 1 then emplyee is full time
                case time if time==1 :
                    #hours for a day
                    hours = 8
                    #declare wage as protected variable
                    _wage = hours * rate_per_hour
                    print("Employee Wage for full time: " ,_wage)
                    print()
                    # if value of full_time is 0 then emplyee is part time   
                case time if time==0:
                    #hours for part time for a day
                    hours = 4
                    _wage = hours * rate_per_hour
                    print("Employee Wage for part time: " ,_wage)
                    print()    
        except Exception as e:
            print("Error :",e)

    def monthly_wage(Self):
        """"
        Description: calculate wage for fulltime and part time for a month
        using hours for day is 8 and part time hour is 4 and per hour rate is 20
        and no of working days for month are 20
        Parameter: self
        Return: none
        """
        rate_per_hour = 20
        working_day=20
        full_time=1
        part_time=2
        time=random.randint(1,2) 
        try: 
            match time:
            # if value of full_time is 1 then emplyee is full time
                case time if time==full_time :
                    #hours for a day
                    hours = 8
                    #declare _dwage for daily wage and _mwage for monthly wage as protected variable
                    _dwage = hours * rate_per_hour 
                    _mwage= _dwage*working_day
                    print("Employee daily Wage for full time for a month : " ,_mwage)
                    print()
                    # if value of full_time is 2 then emplyee is part time   
                case time if time==part_time:
                    #hours for part time for a day
                    hours = 4
                    _dwage = hours * rate_per_hour 
                    _mwage= _dwage*working_day
                    print("Employee daily Wage for part time for a month : " ,_mwage)
                    print()
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
            print("3. Part time wage") 
            print("4. Part time and Full time")
            print("5. Monthly wage")
            print("6. Hundred day wage")
            print("0. Exit")
            print("----------------")
            choice=int(input("Enter choice :"))
            #match case to choose function call
            match choice:
                case 1:
                    e.attendance()
                case 2:
                    e.daily_wage()
                case 3:
                    e.part_time() 
                case 4:
                    e.switch_case()
                case 5:
                    e.monthly_wage()
                case default:
                    print("please enter choice between 1 and 5")
                    print()    
    except:         
         print("Entered wrong value") 

    
