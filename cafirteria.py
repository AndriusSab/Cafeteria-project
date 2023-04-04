# #Cafeteria project : Create an live menu and payment system (a.k.a console program) :
# First the program should ask if table was reserved/ not (Providing your full name) .
# And then if not would assign you a table (there is a specific number single, double or family tables) .
# After table is assigned to you, system should show how many free tables are and how which are reserved/occupied.
# The system must be able to show name/surname of the person of the reserved table (CLI option : enter reserved table nuber ; OUTCOME: Name/Surname/Time Reserved)
# After assigning table, system should show different menu options for breakfast, lunch , dinner , drinks (alcohol. alcohol free), to choose from. Special menu for vegetarian and vegan must be included too in the special menu. All menu items should have weight, preparation time in minutes, calories, and price.
# I have to have an option to change the order before the payment section.
# Thus I can delete, add more, update amount of the same order.
# I should be able to choose whatever I want from all menus in one ordering.
# After I finish, I need to see what I chosen, the full payable amount and approx waiting time for the food to be served
# Add an option to add tips (% from the full cost) to the final bill.
# After the payment , system should generate the receipt (logging).
from main import get_name

class Reservation:
    def __init__(self):
        self.reservations = {"Andrius"}
        self.tables = {"single": 5, "double": 7, "family": 10}

    def check_reservation(self):
        name = get_name
        if name in self.reservations:
            print(f"Your table is reserved for {self.reservations[name]}")
        else:
            self.assign_table()

    def assign_table(self):
        print("Sorry, there are no reservations under that name.")
        size = input("What size table would you like? (single, double, or family) ")
        while size not in self.tables:
            size = input("Invalid size. Please choose single, double, or family. ")
        for table in range(1, 11):
            if table not in self.reservations.values():
                self.reservations[name] = table
                print(
                    f"You have been assigned table {table} for a party of {self.tables[size]}."
                )
                break

    def show_table_status(self):
        free_tables = [
            table for table in range(1, 11) if table not in self.reservations.values()
        ]
        reserved_tables = [
            table for table in range(1, 11) if table in self.reservations.values()
        ]
        print(f"There are {len(free_tables)} free tables:")
        for table in free_tables:
            size = [
                k
                for k, v in self.tables.items()
                if v == self.tables[self.get_size(table)]
            ][0]
            print(f"Table {table} (size: {size})")
        print(f"There are {len(reserved_tables)} reserved tables:")
        for table in reserved_tables:
            name = [k for k, v in self.reservations.items() if v == table][0]
            time = self.reservations[name]
            size = [
                k
                for k, v in self.tables.items()
                if v == self.tables[self.get_size(table)]
            ][0]
            print(f"Table {table} (size: {size}) - {name} reserved for {time}")

    def show_reservation_details(self):
        table = int(input("What table ID would you like to see details for? "))
        if table in self.reservations.values():
            name = [k for k, v in self.reservations.items() if v == table][0]
            time = self.reservations[name]
            size = [
                k
                for k, v in self.tables.items()
                if v == self.tables[self.get_size(table)]
            ][0]
            print(f"Table {table} (size: {size}) - {name} reserved for {time}")
        else:
            print(f"Table {table} is currently unreserved.")

    def get_size(self, table):
        for name, t in self.reservations.items():
            if t == table:
                return self.get_size_by_name(name)
        return None

    def get_size_by_name(self, name):
        for size, t in self.tables.items():
            if t == self.tables[self.get_size_table_by_name(name)]:
                return size
        return None

    def get_size_table_by_name(self, name):
        return self.reservations.get(name)


# example usage
reservation = Reservation()
reservation.check_reservation()
reservation.show_table_status()
reservation.show_reservation_details()
