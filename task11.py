import datetime
import os

rooms = []

def create_file_if_not_exists():
    filename = "LHMS_80002996.txt"
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            print(f"{filename} created.")
    return filename


def add_room():
    room_number = input("Enter room number: ")
    room_type = input("Enter room type (single/double/suite): ")
    price = float(input("Enter room price: "))
    description = input("Enter room description: ")
    
    room = {
        "room_number": room_number,
        "room_type": room_type,
        "price": price,
        "description": description,
        "status": "Available",
        "customer": None,
        "check_in_date": None,
        "check_out_date": None
    }
    rooms.append(room)
    print(f"Room {room_number} added successfully!")


def display_rooms():
    for room in rooms:
        print(f"Room Number: {room['room_number']}, Type: {room['room_type']}, Price: {room['price']}, Status: {room['status']}, Description: {room['description']}")


def allocate_room():
    room_number = input("Enter room number to allocate: ")
    for room in rooms:
        if room["room_number"] == room_number and room["status"] == "Available":
            customer_name = input("Enter customer name: ")
            check_in_date = input("Enter check-in date (YYYY-MM-DD HH:MM): ")
            check_out_date = input("Enter check-out date (YYYY-MM-DD HH:MM): ")
            
            room["customer"] = customer_name
            room["check_in_date"] = check_in_date
            room["check_out_date"] = check_out_date
            room["status"] = "Occupied"
            print(f"Room {room_number} allocated to {customer_name} from {check_in_date} to {check_out_date}.")
            break
    else:
        print("Room not available or not found.")

def deallocate_room():
    room_number = input("Enter room number to release: ")
    for room in rooms:
        if room["room_number"] == room_number and room["status"] == "Occupied":
            room["status"] = "Available"
            room["customer"] = None
            room["check_in_date"] = None
            room["check_out_date"] = None
            print(f"Room {room_number} is now available.")
            return
    print("Room not found or not occupied.")

def display_allocation_details():
    room_number = input("Enter room number to view allocation details: ")
    for room in rooms:
        if room["room_number"] == room_number:
            if room["status"] == "Occupied":
                print(f"Room {room_number} is occupied by {room['customer']}. Check-in: {room['check_in_date']}, Check-out: {room['check_out_date']}")
            else:
                print(f"Room {room_number} is available.")
            return
    print("Room not found.")

def bill_and_deallocate():
    room_number = input("Enter room number to release and bill: ")
    for room in rooms:
        if room["room_number"] == room_number and room["status"] == "Occupied":
            bill = room["price"]
            print(f"Billing {room['customer']} for ${bill}.")
            room["status"] = "Available"
            room["customer"] = None
            room["check_in_date"] = None
            room["check_out_date"] = None
            print(f"Room {room_number} is now available.")
            return
    print("Room not occupied or not found.")

def save_to_file():
    filename = create_file_if_not_exists()
    with open(filename, 'w') as file:
        for room in rooms:
            if room["status"] == "Occupied":
                file.write(f"Room Number: {room['room_number']}, Customer: {room['customer']}, Check-in: {room['check_in_date']}, Check-out: {room['check_out_date']}\n")
    print(f"Room allocations saved to {filename}.")


def show_from_file():
    filename = create_file_if_not_exists()
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nRoom Allocations from File:")
            print(content)
    except FileNotFoundError:
        print(f"{filename} not found.")

def backup_file():
    filename = create_file_if_not_exists()
    backup_filename = f"LHMS_Backup_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    
    with open(filename, 'r') as source_file:
        with open(backup_filename, 'a') as backup_file:
            backup_file.write(source_file.read())
    
 
    with open(filename, 'w') as file:
        file.truncate(0)
    
    print(f"Backup created: {backup_filename}")
    print(f"Original file {filename} cleared.")

def main():
    while True:
        print("\nLANGHAM HOTEL MANAGEMENT SYSTEM")
        print("********************************")
        print("1. Add Rooms")
        print("2. Display Rooms")
        print("3. Allocate Rooms")
        print("4. De-Allocate Rooms")
        print("5. Display Room Allocation Details")
        print("6. Billing")
        print("7. Save Room Allocations to a File")
        print("8. Show Room Allocations from a File")
        print("9. Backup Room Allocations to a Backup File")
        print("0. Exit")
        print("********************************")
        
        choice = input("Enter Your Choice Here (0-9): ")

        if choice == "1":
            add_room()
        elif choice == "2":
            display_rooms()
        elif choice == "3":
            allocate_room()
        elif choice == "4":
            deallocate_room()
        elif choice == "5":
            display_allocation_details()
        elif choice == "6":
            bill_and_deallocate()
        elif choice == "7":
            save_to_file()
        elif choice == "8":
            show_from_file()
        elif choice == "9":
            backup_file()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
