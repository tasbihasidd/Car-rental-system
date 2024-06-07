import datetime
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
        print("Car rented successfully")
        return rentals
        print(f"Total amount: {total_amount}")
    else:
        print("Car is not available for rent")