# Import the RentalService class from your rental_service module
from rental_services import RentalService

def main():
    rental_system = RentalService()

    while True:
        print("\nCar Rental Service")
        print("1. Add Vehicle")
        print("2. Show Available Vehicles")
        print("3. Register Client")
        print("4. Rent a Vehicle")
        print("5. Return a Vehicle")
        print("6. Exit")

        try:
            option = int(input("Choose an option: "))
            if option == 1:
                vid = input("Enter Vehicle ID: ")
                model = input("Enter Model Name: ")
                brand = input("Enter Brand Name: ")
                rate = input("Enter Daily Rate: ")
                rental_system.add_vehicle(vid, model, brand, rate)
            elif option == 2:
                rental_system.show_vehicles()
            elif option == 3:
                cid = input("Enter Client ID: ")
                name = input("Enter Client Name: ")
                contact = input("Enter Contact Number: ")
                rental_system.register_client(cid, name, contact)
            elif option == 4:
                vid = input("Enter Vehicle ID: ")
                cid = input("Enter Client ID: ")
                days = int(input("Enter Rental Days: "))
                rental_system.rent_vehicle(vid, cid, days)
            elif option == 5:
                vid = input("Enter Vehicle ID to Return: ")
                rental_system.return_vehicle(vid)
            elif option == 6:
                print("Thank you for using the Car Rental Service. Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
