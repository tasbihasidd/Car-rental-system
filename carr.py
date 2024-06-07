import datetime

def add_car(carId, model, year, color, rental_status, rental_price_per_day, cars):
    # try:
    #     model = str(model)
    #     year = int(year)
    #     rental_price = float(rental_price)
    # except ValueError:
    #     print("Invalid input format for year or rental price.")
    #     return cars
    
    # if rental_status.lower() not in ["available", "unavailable"]:
    #     print("Invalid rental status. Please enter 'available' or 'unavailable'.")
    #     return cars
    
    
    # if carId in cars:
    #     print("Car ID already exists. Please choose a different ID.")
    #     return cars
    try:
        try:
            model=str(model)
            year=int(year)
            rental_price_per_day = float(rental_price_per_day)
        except:
            print("Invalid input format")
        if rental_status.lower() not in ['available','unavailable']:
            raise ValueError("Invalid rental status")
        if carId in cars:
            raise ValueError("Car Id already exists. Please choose a different one")
        
    except ValueError as e:
        print("Please re anater the correct values")
    
    # Add the car details if all conditions are met
    
    cars[carId] = {
        "model": model.title(),
        "year": year,
        "color": color.lower(),
        "rental_status": rental_status,
        "rental_price_per_day": rental_price_per_day
    }
    print("Car added successfully")
    return cars



def available_cars(cars):
    print("Available cars are: ", cars)
    
    
    
def customer_details(customer_id,name,phone_number,email,address,customers):
    # customers = {}
    customers[customer_id] = {
        "name": name,
        "phone_number":phone_number,
        "email": email,
        "address": address
    }
    print("Customer added successfully")
    print(customers)
    return customers 

def rent_a_car(car_id,customer_id,rental_price_per_day,end_date,start_date,cars,rentals):
    if car_id not in cars:
        print("Car Id doesn't exist: ")
        return 
    
    if cars[car_id]['rental_status'] == 'available':
        start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        rental_days = (end_date_obj - start_date_obj).days
        total_amount = rental_days * rental_price_per_day
        
        cars[car_id]['rental_status'] == 'unavailable'
        rentals[car_id]={
            "customer_id" :customer_id,
            "start_date" : start_date_obj,
            "end_date":end_date_obj,
            "total_amount":total_amount
        }
        print("Car rented successfully by")
        print(f"Total amount: {total_amount}")
    else:
        print("Car is not available for rent")
        
def return_a_car(car_id,cars,rentals):
    if car_id not in cars:
        print("Car Id doesnt exist")
    if car_id in rentals:
        cars[car_id].update({"rental_status":"available"})
        rentals.pop(car_id)
        print("Car returned successfully")
        print(rentals)
        return rentals
    else:
        print("Car is not rented currently")
            
        
def rental_history(cars,rentals):
    if not rentals:
        print("No rental history available.")
        return
    
    print("Rental History:")
    for car_id, rental_info in rentals.items():
        print(f"Car ID: {car_id}")
        print(f"Customer ID: {rental_info['customer_id']}")
        print(f"Start Date: {rental_info['start_date'].strftime('%Y-%m-%d')}")
        print(f"End Date: {rental_info['end_date'].strftime('%Y-%m-%d')}")
        print(f"Total Amount: {rental_info['total_amount']}")
        print("-------------------------------")

def filter_cars_by_price_range(cars, min_price, max_price):
    print(f"Cars available in the price range ${min_price} - ${max_price}:")
    for car_id, car_details in cars.items():
        if car_details['rental_status'] == 'available' and min_price <= car_details['rental_price_per_day'] <= max_price:
            print(f"ID: {car_id}, Model: {car_details['model']}, Year: {car_details['year']}, Color: {car_details['color']}, Rental Price per Day: {car_details['rental_price_per_day']}")
    


def main():
    cars = {}
    rentals={}
    customers = {}
    print("**** Welcome to car rental system *****")
    print("What do you want to do? \n1)Add a car\n2)Available cars\n3)Add a customer\n4)Rent a car\n4)Return a car\n5)View rental history")
    while True:
        user_choice = input("Enter your choice: ")
        if user_choice == '1':
            while True:
                carId = int(input("Enter car ID: "))
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
            car_id = int(input("Enter car id: "))
            customer_id = int(input("Enter customer id: "))
            start_date = input("Enter date rented: ")
            end_date = input("Enter end date: ")
            rent_a_car(car_id,customer_id,rental_price_per_day,end_date,start_date,cars,rentals)
            
        elif user_choice == '5':
            car_id = int(input("Enter car id: "))
            return_a_car(car_id,cars,rentals)
            
        elif user_choice=='6':
            rental_history(cars,rentals)
            
        elif user_choice=='7':
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price:  "))
        
        
            
        elif user_choice == '8':
            print("Exiting..")
            break

main()