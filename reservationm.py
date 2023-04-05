from datetime import time
from reserved_table import reserved_tables


class TableReservation:
    def __init__(self):
        self.reserved_tables = reserved_tables

    def check_table_by_name(
        self, fullname: str, num_guests: int, res_time: time
    ) -> None:
        for table_type, tables in self.reserved_tables.items():
            for table_name, table in tables.items():
                if table["name"] == fullname:
                    print(f"Sorry, {fullname} already has a table reserved.")
                    return

    def reserve_table(self, fullname: str, num_guests: int, res_time: time) -> None:
        if num_guests <= 2:
            table_type = "small"
        elif num_guests <= 4:
            table_type = "double"
        else:
            table_type = "family"

        for table_type, tables in self.reserved_tables.items():
            for table_name, table in tables.items():
                if table["status"] == "Available":
                    table["name"] = fullname
                    table["num_guests"] = num_guests
                    table["res_time"] = res_time
                    table["status"] = "Reserved"
                    print(
                        f"Table {table_type, table_name} has been reserved for {fullname}."
                    )
                    return
        print("Sorry, there are no tables available.")

    def get_table_status(self, name: str) -> str:
        for table_type, tables in self.reserved_tables.items():
            for table_name, table in tables.items():
                if table["name"] == name:
                    return table["status"]
        return "Table not found."

    def get_table_num_guests(self, name: str) -> int:
        for table_type, tables in self.reserved_tables.items():
            for table_name, table in tables.items():
                if table["name"] == name:
                    return table["num_guests"]
        raise (f"Table with name {name} not found")

    def get_table_name(self, name: str) -> str:
        for table_type, tables in self.reserved_tables.items():
            for table_name, table in tables.items():
                if table["name"] == name:
                    return table_name
        return "Table not found."

    def get_table_reserved_time(self, name: str) -> time:
        for table_type, tables in self.reserved_tables.items():
            for table_name, table in tables.items():
                if table["name"] == name and table["status"] == "Reserved":
                    return table["res_time"]


if __name__ == "__main__":
    table_reservation = TableReservation()
    fullname = input("Please enter your full name: ").upper()
    num_guests = int(input("Please enter the number of guests: "))
    res_time = int(input("Please enter time for reservation: "))
    # table_reservation.reserve_table(fullname, num_guests, res_time)


print(table_reservation.get_table_name(fullname))

table_reservation.reserve_table(fullname, num_guests, res_time)
