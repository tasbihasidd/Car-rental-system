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
