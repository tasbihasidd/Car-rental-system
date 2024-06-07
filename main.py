
# import json
from add_car import *
from available_cars import available_cars
from customer_details import *
from rent_a_car import *
from return_a_car import *
from rental_history import *
from load import load_json
from write import write_json

# def load_json(filename):
#     try:
#         with open(filename, 'r') as file:
#             return json.load(file.read())
#     except FileNotFoundError:
#         return "exception during reading of json file"
    
# def save_json(data, filename):
#     with open(filename, 'w') as file:
#         json.dump(data, file, indent=4)

 

def main():
    cars = load_json('cars.json')
    rentals=load_json('rentals.json')
    customers = load_json('customers.json')
    # print(cars,rentals,customers)
    print("**** Welcome to car rental system *****")
    print("What do you want to do? \n1)Add a car\n2)Available cars\n3)Add a customer\n4)Rent a car\n4)Return a car\n5)View rental history")
    while True:
        user_choice = input("Enter your choice: ")
        if user_choice == '1':
            while True:
                carId = input("Enter car ID: ")
                if carId not in cars:
                    break
                else:
                    print("Car ID already exists. Please choose a different ID.")
            model = input("Enter model: ")
            year = input("Enter year of year made: ")
            rental_price_per_day = input("Enter rent price/day: ")
            color = input("Enter color of car: ")
            while True:
                rental_status = input("Enter status of available/Unavailable: ")
                if rental_status.lower() in ['available','unavailable']:
                    break
                else:
                    print("Invalid rental status.Please input 'available' or 'unavailable'")
            add_car(carId,model,year,color,rental_status,rental_price_per_day,cars)
            
        elif user_choice == '2':
            available_cars(cars)
            
        elif user_choice == '3':
            customer_id = int(input('Enter customer Id: '))
            name = input("Enter name of customer: ")
            email= input("Enter email: ")
            address = input("Enter address: ")
            phone_number = input("Enter phone number: ")
            customer_details(customer_id,name,phone_number,email,address,customers)
            
        elif user_choice=='4':
            car_id = input("Enter car id: ")
            customer_id = int(input("Enter customer id: "))
            start_date = input("Enter date rented: ")
            end_date = input("Enter end date: ")
            rental_price_per_day = cars[car_id]['rental_price_per_day']
            rent_a_car(car_id,customer_id,rental_price_per_day,end_date,start_date,cars,rentals)
            
        elif user_choice == '5':
            car_id = input("Enter car id: ")
            return_a_car(car_id,cars,rentals)
            
        elif user_choice=='6':
            rental_history(cars,rentals)
        
        
            
        elif user_choice == '7':
            write_json(cars, 'cars.json')
            write_json(rentals, 'rentals.json')
            write_json(customers, 'customers.json')
            print("Exiting..")
            break

main()