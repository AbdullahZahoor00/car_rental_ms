class Vehicle:
    def __init__(self, vehicle_id, model_name, brand_name, daily_rate, is_available=True):
        self.vehicle_id = vehicle_id
        self.model_name = model_name
        self.brand_name = brand_name
        self.daily_rate = daily_rate
        self.is_available = is_available

    def __str__(self):
        status = "Available" if self.is_available else "Rented"
        return f"{self.vehicle_id}: {self.brand_name} {self.model_name} - ${self.daily_rate}/day - {status}"


class Client:
    def __init__(self, client_id, full_name, phone_number):
        self.client_id = client_id
        self.full_name = full_name
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.client_id}: {self.full_name} - Phone: {self.phone_number}"


class RentalService:
    def __init__(self):

        self.vehicles = []  # Start with an empty list of vehicles
        self.clients = {}
        self.rentals = []

    # Adding a vehicle
    def add_vehicle(self, vehicle_id, model_name, brand_name, daily_rate):
        # Check if the vehicle ID already exists
        for car in self.vehicles:
            if car.vehicle_id == vehicle_id:
                print(f"Error: Vehicle ID {vehicle_id} is already in use. Try another ID.")
                return

        # checking the validity of daily rate
        if not self.is_valid_number(daily_rate):
            print("Error: Invalid daily rate. Please enter a valid number.")
            return

        # Converting daily rate to float and add the vehicle
        daily_rate = float(daily_rate)
        new_vehicle = Vehicle(vehicle_id, model_name, brand_name, daily_rate)
        self.vehicles.append(new_vehicle)  # Add the new vehicle to the list
        print(f"Vehicle {brand_name} {model_name} has been added successfully.")

    # Displaying vehicles based on availability
    def show_vehicles(self, only_available=True):
        print("\nAvailable Vehicles:" if only_available else "\nAll Vehicles:")
        for car in self.vehicles:
            if not only_available or car.is_available:
                print(car)

    # Registering a new client
    def register_client(self, client_id, name, contact):
        if client_id in self.clients:
            print(f"Client ID {client_id} is already registered.")
        else:
            new_client = Client(client_id, name, contact)
            self.clients[client_id] = new_client
            print(f"Client {name} has been added.")

    # Renting a vehicle
    def rent_vehicle(self, vehicle_id, client_id, rental_days):
        vehicle = self._find_vehicle(vehicle_id)
        client = self.clients.get(client_id)
        if not vehicle or not client:
            print("Error: Invalid vehicle or client ID.")
            return

        # Checking if rental_days is a valid number
        if not self.is_valid_number(rental_days):
            print("Error: Invalid rental days. Please enter a valid number.")
            return

        rental_days = int(rental_days)  # in order to Convert to integer
        if vehicle.is_available:
            vehicle.is_available = False
            total_cost = vehicle.daily_rate * rental_days
            self.rentals.append((vehicle_id, client_id, rental_days, total_cost))
            print(
                f"Vehicle {vehicle.brand_name} {vehicle.model_name} rented by {client.full_name} for {rental_days} days. Total: ${total_cost}.")
        else:
            print(f"Vehicle {vehicle.brand_name} {vehicle.model_name} is currently rented.")

    # Helper function to find a vehicle
    def _find_vehicle(self, vehicle_id):
        for car in self.vehicles:
            if car.vehicle_id == vehicle_id:
                return car
        return None

    # Returning a vehicle
    def return_vehicle(self, vehicle_id):
        vehicle = self._find_vehicle(vehicle_id)
        if vehicle and not vehicle.is_available:
            vehicle.is_available = True
            print(f"Vehicle {vehicle.brand_name} {vehicle.model_name} has been returned.")
        else:
            print("Error: Vehicle is not rented or does not exist.")

    # Helper function to check if a value is a valid number
    def is_valid_number(self, value):
        # This helper function checks if the value can be converted to a valid float or integer
        try:
            float(value)  # Tries to convert to float
            return True
        except ValueError:
            return False


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

        option = input("Choose an option: ")

        # Check if the option is a valid number
        if not rental_system.is_valid_number(option):
            print("Error: Invalid option. Please enter a valid number.")
            continue

        option = int(option)

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
            days = input("Enter Rental Days: ")
            rental_system.rent_vehicle(vid, cid, days)
        elif option == 5:
            vid = input("Enter Vehicle ID to Return: ")
            rental_system.return_vehicle(vid)
        elif option == 6:
            print("Thank you for using the Car Rental Service. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
