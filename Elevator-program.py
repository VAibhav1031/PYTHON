class Elevator:
    def __init__(self, top, bottom, current_floor):
        self.top = top
        self.bottom = bottom
        self.current_floor = current_floor

    def up(self):
        if self.current_floor == self.top:
            print("You are already at the top floor!")
        elif self.current_floor == self.bottom and self.current_floor != self.top:
            try:
                floor = int(input("Enter the floor:"))
                if self.bottom <= floor <= self.top:
                    self.current_floor = floor
                    print(f"You've reached floor {floor}.")
                else:
                    print("Invalid floor selection.")
            except ValueError:
                print("Invalid input. Please enter a valid floor number.")
        else:
            print("Error")

    def down(self):
        if self.current_floor == self.bottom:
            print("You are already at the bottom floor!")
        elif self.current_floor == self.top and self.current_floor != self.bottom:
            try:
                floor = int(input("Enter the floor:"))
                if self.bottom <= floor <= self.top:
                    self.current_floor = floor
                    print(f"You've reached floor {floor}.")
                else:
                    print("Invalid floor selection.")
            except ValueError:
                print("Invalid input. Please enter a valid floor number.")
        else:
            print("Error")

    def emergency_Call(self, floor):
        if self.current_floor != floor:
            print("Emergency call sent to authorities!")

elevator = Elevator(10, 1, 1)

while True:
    up_down = input("Where do you want to go, UP or DOWN? ").strip().lower()
    
    if up_down == "up":
        elevator.up()
    elif up_down == "down":
        elevator.down()
    else:
        print("Invalid choice. Please select UP or DOWN.")

    emer = input("Is there any Emergency (y or n)? ").strip().lower()
    if emer == 'y':
        try:
            floor = int(input("Enter the floor for the emergency: "))
            elevator.emergency_Call(floor)
        except ValueError:
            print("Invalid input for the emergency floor.")

    # You can add an option to exit the loop or continue the elevator simulation here if needed.
