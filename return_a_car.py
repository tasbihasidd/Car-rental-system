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
            