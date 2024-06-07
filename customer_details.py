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