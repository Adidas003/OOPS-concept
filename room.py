class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.is_booked = False

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Room {self.room_number} ({self.room_type}): {status}"

class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room_number, room_type):
        room = Room(room_number, room_type)
        self.rooms.append(room)
        print(f"Added {room}")

    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_booked:
                    room.is_booked = True
                    print(f"Room {room_number} has been booked.")
                else:
                    print(f"Room {room_number} is already booked.")
                return
        print(f"Room {room_number} does not exist.")

    def unbook_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_booked:
                    room.is_booked = False
                    print(f"Room {room_number} has been unbooked.")
                else:
                    print(f"Room {room_number} is not booked.")
                return
        print(f"Room {room_number} does not exist.")

    def check_availability(self):
        available_rooms = [room for room in self.rooms if not room.is_booked]
        if available_rooms:
            print("Available rooms:")
            for room in available_rooms:
                print(room)
        else:
            print("No rooms available.")

def main():
    hotel = Hotel()
    
    while True:
        print("\nHotel Room Booking System")
        print("1. Add Room")
        print("2. Book Room")
        print("3. Unbook Room")
        print("4. Check Availability")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            room_number = input("Enter room number: ")
            room_type = input("Enter room type (e.g., Single, Double): ")
            hotel.add_room(room_number, room_type)
        elif choice == '2':
            room_number = input("Enter room number to book: ")
            hotel.book_room(room_number)
        elif choice == '3':
            room_number = input("Enter room number to unbook: ")
            hotel.unbook_room(room_number)
        elif choice == '4':
            hotel.check_availability()
        elif choice == '5':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
