class Reservation:
    """Self tables dictionary key stands for table type "single", "double" and "family", and values
    stands for number of tables available"""

    def __init__(self):
        self.reservations = {}
        self.tables = {"single": 2, "double": 4, "family": 6}

    def check_reservation(self, name):
        if name in self.reservations:
            print(f"Your table is reserved for table {self.reservations[name]}.")
        else:
            self.assign_table(name)

    def assign_table(self, name):
        if name in self.reservations:
            return
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
        else:
            print("Sorry, there are no free tables available.")


def main():
    reservation = {"Andrius Sabaliauskas": "family"}
    name = input("Hello, what is your full name? ")
    type = input("What size table would you like? (single, double, or family) ")
    while type not in reservation.tables:
        type = input("Invalid size. Please choose single, double, or family. ")
    reservation.check_reservation(name)


if __name__ == "__main__":
    main()
