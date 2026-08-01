import csv
import os

from vehicle import Car


class RentalManager:

    def __init__(self):
        self.vehicles = []
        self.filename = "rental.csv"
        self.history_filename = "history.csv"
        self.rental_history = []
        self.total_revenue = 0

        self.load_vehicles()
        self.load_rental_history()

    # ------------------------
    # Add Vehicle
    # ------------------------

    def add_vehicle(self):
        vehicle_id = input("Enter Vehicle ID: ")
        name = input("Enter Vehicle Name: ")
        number = input("Enter Vehicle Number: ")

        while True:
            try:
                rent = float(input("Enter Rent Per Day: "))
                break
            except ValueError:
                print("Please enter a valid amount.")

        car = Car(vehicle_id, name, number, rent)
        self.vehicles.append(car)
        print("\nVehicle Added Successfully.\n")

    # ------------------------
    # Display Vehicles
    # ------------------------

    def display_vehicles(self):
        if not self.vehicles:
            print("\nNo vehicles found.\n")
            return

        for vehicle in self.vehicles:
            vehicle.display()

    # ------------------------
    # Search Vehicle
    # ------------------------

    def search_vehicle(self):
        vehicle_id = input("Enter Vehicle ID to search: ")

        for vehicle in self.vehicles:
            if vehicle.get_vehicle_id() == vehicle_id:
                print("\nVehicle Found!\n")
                vehicle.display()
                return

        print("\nVehicle not found.\n")

    # ------------------------
    # Update Vehicle
    # ------------------------

    def update_vehicle(self):
        vehicle_id = input("Enter Vehicle ID to update: ").strip()

        for vehicle in self.vehicles:
            if vehicle.get_vehicle_id() == vehicle_id:
                print("\nLeave blank if you don't want to change a field.\n")

                new_name = input("Enter New Vehicle Name: ").strip()
                new_number = input("Enter New Vehicle Number: ").strip()
                new_rent = input("Enter New Rent Per Day: ").strip()

                if new_name:
                    vehicle.set_name(new_name)

                if new_number:
                    vehicle.set_number(new_number)

                if new_rent:
                    try:
                        vehicle.set_rent_per_day(float(new_rent))
                    except ValueError:
                        print("Invalid rent value!")
                        return

                self.save_vehicles()
                print("\nVehicle Updated Successfully.\n")
                return

        print("\nVehicle not found.\n")

    # ------------------------
    # Rent Vehicle
    # ------------------------

    def rent_vehicle(self):
        vehicle_id = input("Enter Vehicle ID to Rent: ").strip()

        for vehicle in self.vehicles:
            if vehicle.get_vehicle_id() == vehicle_id:
                if not vehicle.is_available():
                    print("\nVehicle is already rented.\n")
                    return

                customer_name = input("Enter Customer Name: ")

                while True:
                    try:
                        days = int(input("Enter Number of Rental Days: "))
                        break
                    except ValueError:
                        print("Please enter a valid number.")

                total = vehicle.calculate_rent(days)
                self.total_revenue += total

                rental_record = {
                    "Customer": customer_name,
                    "Vehicle": vehicle.get_name(),
                    "Vehicle Number": vehicle.get_number(),
                    "Days": days,
                    "Charge": total,
                }
                self.rental_history.append(rental_record)
                self.save_rental_history()

                vehicle.set_available(False)

                print("\n========== RENTAL RECEIPT ==========")
                print(f"Customer Name : {customer_name}")
                print(f"Vehicle Name  : {vehicle.get_name()}")
                print(f"Vehicle No    : {vehicle.get_number()}")
                print(f"Days          : {days}")
                print(f"Total Charge  : ₹{total}")
                print("Status        : Rented")
                print("====================================")
                return

        print("\nVehicle not found.\n")

    # ------------------------
    # Return Vehicle
    # ------------------------

    def return_vehicle(self):
        vehicle_id = input("Enter Vehicle ID to Return: ").strip()

        for vehicle in self.vehicles:
            if vehicle.get_vehicle_id() == vehicle_id:
                if vehicle.is_available():
                    print("\nVehicle is already available.\n")
                    return

                vehicle.set_available(True)
                print("\nVehicle Returned Successfully.")
                return

        print("\nVehicle not found.")

    # ------------------------
    # Rental History
    # ------------------------

    def view_rental_history(self):
        if not self.rental_history:
            print("\nNo Rental History Found.\n")
            return

        print("\n========== RENTAL HISTORY ==========\n")

        for i, rental in enumerate(self.rental_history, start=1):
            print(f"Rental {i}")
            print(f"Customer       : {rental['Customer']}")
            print(f"Vehicle        : {rental['Vehicle']}")
            print(f"Vehicle Number : {rental['Vehicle Number']}")
            print(f"Days           : {rental['Days']}")
            print(f"Charge         : ₹{rental['Charge']}")
            print("-" * 35)

    # ------------------------
    # Total Revenue
    # ------------------------

    def show_total_revenue(self):
        print("\n========== TOTAL REVENUE ==========")
        print(f"Total Revenue : ₹{self.total_revenue}")

    # ------------------------
    # Save Vehicles
    # ------------------------

    def save_vehicles(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Number", "Rent", "Available"])

            for vehicle in self.vehicles:
                writer.writerow([
                    vehicle.get_vehicle_id(),
                    vehicle.get_name(),
                    vehicle.get_number(),
                    vehicle.get_rent_per_day(),
                    vehicle.is_available(),
                ])

        print("Vehicle data saved successfully.")

    def save_rental_history(self):
        with open(self.history_filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Customer", "Vehicle", "Vehicle Number", "Days", "Charge"])

            for record in self.rental_history:
                writer.writerow([
                    record["Customer"],
                    record["Vehicle"],
                    record["Vehicle Number"],
                    record["Days"],
                    record["Charge"],
                ])

    def load_rental_history(self):
        if not os.path.exists(self.history_filename):
            return

        with open(self.history_filename, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                if not row:
                    continue

                record = {
                    "Customer": row[0],
                    "Vehicle": row[1],
                    "Vehicle Number": row[2],
                    "Days": int(row[3]),
                    "Charge": float(row[4]),
                }
                self.rental_history.append(record)
                self.total_revenue += float(row[4])

    # ------------------------
    # Load Vehicles
    # ------------------------

    def load_vehicles(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                if not row:
                    continue

                vehicle = Car(
                    row[0],
                    row[1],
                    row[2],
                    float(row[3]),
                    row[4] == "True",
                )

                self.vehicles.append(vehicle)