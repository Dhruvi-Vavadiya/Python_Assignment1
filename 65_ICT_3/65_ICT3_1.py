# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 08:53:38 2025

@author: Planet
"""

class InvalidPriceException(Exception):
    "Raised when the input value is less than 1000"
    pass

class Car:
    def __init__(self):
        self.color = input("Enter color :-")
        self.model = input("Enter model :-")
        self.company = input("Enter company :-")
        self.price = int(input("Enter price :-"))
        self.PF = input("Enter PF :-")

class CustomerDetail :
    def __init__(self):
        self.cname = input("Enter c name :-")
        self.cgender = input("Enter c gender :-")
        self.cdob = input("Enter c dob :-")
       
        
        while True:
            age = input("Enter c age :-")
            try:
                self.cage = int(age)
                break
            except ValueError:
                print("invalid age")

class ShowDetail(Car,CustomerDetail):
    def __init__(self):
       # super().__init__()
        Car.__init__(self)
        CustomerDetail.__init__(self)
    
    def PurchaseCar(self):
        
        try:
            if self.price>1000:
                raise InvalidPriceException()
            else:
                print(f"{self.cname} You are eligible to Buy this car")
        except InvalidPriceException:
            print(f"{self.cname} Exception occured: Invalid Price")
       
                
                
s =ShowDetail();
s.PurchaseCar();
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        