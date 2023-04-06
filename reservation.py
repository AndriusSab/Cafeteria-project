from datetime import datetime, time
from reserved_table import reserved_tables


class TableReservation:
    def __init__(self):
        self.reserved_table = reserved_tables

    def reserve_table(self, fullname: str, num_guests: int, res_time: str) -> None:
        res_time = datetime.strptime(res_time, "%H:%M").time()

        if num_guests <= 2:
            table_size = "single"
        elif num_guests in range(2, 4):
            table_size = "double"
        elif num_guests in range(5, 7):
            table_size = "family"

        for tables in self.reserved_table.values():
            for table_name, table in tables.items():
                if table["fullname"] == fullname.upper():
                    print(
                        f"Congrats, {fullname} table for You is already reserved.See You soon!"
                    )
                    return

        for tables in self.reserved_table.values():
            for table_name, table in tables.items():
                if table["status"] == "Available" and table["num_guests"] == num_guests:
                    table["fullname"] = fullname.upper()
                    table["num_guests"] = num_guests
                    table["res_time"] = res_time
                    table["status"] = "Reserved"
                    print(
                        f"Table {table_size} {table_name} has been reserved for {fullname}."
                    )
                    return
                elif (
                    table["status"] == "Available" and table["num_guests"] > num_guests
                ):
                    print(f"Sorry, there are no {table_size} tables available.")
                    return

        print("Sorry, there are no tables available.")


if __name__ == "__main__":
    table_reservation = TableReservation()
    fullname = input("Please enter your full name: ").upper()
    num_guests = int(input("Please enter the number of guests: "))
    res_time = input("Please enter time for reservation (HH:MM): ")
    table_reservation.reserve_table(fullname, num_guests, res_time)
