# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 09:48:58 2025

@author: Planet
"""

class Car:
    def __init__(self, color, model, company, price):
        self.color = color
        self.model = model
        self.company = company
        self.price = price

    def __str__(self):
        return f"Color: {self.color}, Model: {self.model}, Company: {self.company}, Price: {self.price}"


class CarManager:
    def __init__(self):
        self.car_list = []  # List to store car objects

    def add_car(self):
        color = input("Enter color: ")
        model = input("Enter model: ")
        company = input("Enter company: ")
        price = input("Enter price: ")
        car = Car(color, model, company, price)
        self.car_list.append(car)
        print("Car added successfully!\n")

    def delete_car(self):
        self.list_cars()
        index = int(input("Enter the index of the car to delete: "))
        if 0 <= index < len(self.car_list):
            removed = self.car_list.pop(index)
            print(f"Deleted car: {removed}\n")
        else:
            print("Invalid index!\n")

    def edit_car(self):
        self.list_cars()
        index = int(input("Enter the index of the car to edit: "))
        if 0 <= index < len(self.car_list):
            car = self.car_list[index]
            print("Enter new details (leave blank to keep current):")
            color = input(f"Color ({car.color}): ") or car.color
            model = input(f"Model ({car.model}): ") or car.model
            company = input(f"Company ({car.company}): ") or car.company
            price = input(f"Price ({car.price}): ") or car.price
            self.car_list[index] = Car(color, model, company, price)
            print("Car updated successfully!\n")
        else:
            print("Invalid index!\n")

    def list_cars(self):
        if not self.car_list:
            print("No cars available.\n")
            return
        print("\nList of Cars:")
        for idx, car in enumerate(self.car_list):
            print(f"{idx}: {car}")
        print()


def main():
    manager = CarManager()

    while True:
        print("1. Add Car")
        print("2. Delete Car")
        print("3. Edit Car")
        print("4. List Cars")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manager.add_car()
        elif choice == '2':
            manager.delete_car()
        elif choice == '3':
            manager.edit_car()
        elif choice == '4':
            manager.list_cars()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
