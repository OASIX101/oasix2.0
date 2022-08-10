from pip import main
from bike_rental import BikeRental, Customer

def bike_rent():
    shop = BikeRental(100)
    customer = Customer()

    while True:
        print("""
        ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $20
        4. Request a bike on weekly basis $60
        5. Return a bike
        6. Exit
        """)
        
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        
        if choice == 1:
            shop.display_stock()
        
        elif choice == 2:
            customer.rentalTime = shop.rent_on_hourly_basis(customer.requestBike())
            customer.rentalBasis = "hourly"

        elif choice == 3:
            customer.rentalTime = shop.rent_on_daily_basis(customer.requestBike())
            customer.rentalBasis = "daily"

        elif choice == 4:
            customer.rentalTime = shop.rent_on_weekly_basis(customer.requestBike())
            customer.rentalBasis = "weekly"

        elif choice == 5:
            customer.bill = shop.returnBike(customer.returnBike())
            customer.rentalBasis, customer.rentalTime, customer.bikes = 0,0,0        
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")        
    print("Thank you for using the bike rental system.")


bike_rent()

# if __name__=="__main__":
#     bike_rent()