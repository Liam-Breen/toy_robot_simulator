class ToyRobot():

    def __init__(self) -> None:
        self.current_coordinates = None
        self.current_direction = None

    def report(self) -> tuple:
        return f"{self.current_coordinates[0]},{self.current_coordinates[1]},{self.current_direction}"

    def place(self, command) -> None:
        """Sets the current_coordinates and current_direction

        Args:
            command (String): The place command the user has entered
        """

        try:
            command = command.split(' ')
            command = command[1].split(',')
            coordinates = (int(command[0]), int(command[1]))
            direction = command[2]
        except:
            print('This was not a valid place command')
            command = input('Enter your command: ')
            self.place(command)

        if direction not in ['NORTH', 'SOUTH', 'EAST', 'WEST']:
            print(f'{direction} is not a valid direction.')
        elif (coordinates[0] or coordinates[1]) > 4 or (coordinates[0] or coordinates[1]) < 0:
            print(f'The coordinates, {coordinates},  are not valid')
        else:
            self.current_coordinates = coordinates
            self.current_direction = direction

if __name__ == "__main__":
    debug = True
    toy_robot = None
    command = input("Enter your first command: ")

    while command:

        if 'PLACE' in command:
            if debug: command = 'PLACE 0,0,NORTH'
            if toy_robot:
                toy_robot.place(command)
            else:
                toy_robot = ToyRobot()
                toy_robot.place(command)
                if debug: assert toy_robot.current_coordinates == (0, 0)
                if debug: assert toy_robot.current_direction == 'NORTH'

        elif toy_robot:
            if command == 'REPORT':
                print(toy_robot.report())

        command = input("Enter your command: ")