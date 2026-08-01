from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_id, name, number, rent_per_day, available=True):
        self.__vehicle_id = vehicle_id
        self.__name = name
        self.__number = number
        self.__rent_per_day = rent_per_day
        self.__available = available

    # Getters
    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def get_rent_per_day(self):
        return self.__rent_per_day

    def is_available(self):
        return self.__available

    # Setter
    def set_available(self, status):
        self.__available = status
        
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def set_rent_per_day(self, rent):
        self.__rent_per_day = rent

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def set_rent_per_day(self, rent):
        self.__rent_per_day = rent

    @abstractmethod
    def calculate_rent(self, days):
        pass

    def display(self):
        status = "Available" if self.__available else "Rented"

        print(f"""
Vehicle ID      : {self.__vehicle_id}
Vehicle Name    : {self.__name}
Vehicle Number  : {self.__number}
Rent Per Day    : ₹{self.__rent_per_day}
Status          : {status}
""")


class Car(Vehicle):

    def calculate_rent(self, days):
        return self.get_rent_per_day() * days