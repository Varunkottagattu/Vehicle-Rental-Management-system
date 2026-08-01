from rental_manager import RentalManager

manager = RentalManager()

while True:

    print("\n========== VEHICLE RENTAL SYSTEM ==========")
    print("1. Add Vehicle")
    print("2. Display Vehicles")
    print("3. Save Data")
    print("4. Search Vehicle")
    print("5. Update Vehicle")
    print("6. Rent Vehicle")
    print("7. Return Vehicle")
    print("8. View Rental History")
    print("9. Show Total Revenue")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_vehicle()

    elif choice == "2":
        manager.display_vehicles()

    elif choice == "3":
        manager.save_vehicles()

    elif choice == "4":
        manager.search_vehicle()


    elif choice == "5":
        manager.update_vehicle()

    elif choice == "6":
        manager.rent_vehicle()

    elif choice == "7":
        manager.return_vehicle()

    elif choice == "8":
        manager.view_rental_history()

    elif choice == "9":
        manager.show_total_revenue()

    elif choice == "10":
        manager.save_vehicles()
        manager.save_rental_history()
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
