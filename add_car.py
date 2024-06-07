def add_car(carId, model, year, color, rental_status, rental_price_per_day, cars):
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