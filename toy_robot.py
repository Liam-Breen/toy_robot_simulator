class TableTop():

    def __init__(self) -> None:
        self.rows = None
        self.columns = None


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

    def move(self) -> None:
        """Moves the toy robot forward one spot depending on the direction it faces"""

        if self.current_direction == 'EAST':
            x_cord = self.current_coordinates[0]
            if x_cord + 1 < 5:
                self.current_coordinates = (x_cord + 1, self.current_coordinates[1])

        elif self.current_direction == 'WEST':
            x_cord = self.current_coordinates[0]
            if x_cord - 1 >= 0:
                self.current_coordinates = (x_cord - 1, self.current_coordinates[1])

        elif self.current_direction == 'NORTH':
            y_cord = self.current_coordinates[1]
            if y_cord + 1 < 5:
                self.current_coordinates = (self.current_coordinates[0], y_cord + 1)

        elif self.current_direction == 'SOUTH':
            y_cord = self.current_coordinates[1]
            if y_cord + 1 >= 0:
                self.current_coordinates = (self.current_coordinates[0], y_cord - 1)

    def set_direction(self, direction: str) -> None:
        """Changes the direction the toy robot is facing by 90 degrees depending on user entry.

        Args:
            direction (String): The way the direction will change. Either LEFT or RIGHT.
        """

        directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']

        old_direction_index = directions.index(self.current_direction)


        if 'RIGHT' in direction:
            new_direction = old_direction_index + 1
            if new_direction > 3:
                new_direction = 0
        elif 'LEFT' in direction:
            new_direction = old_direction_index - 1
        else:
            print(f'{direction} is not a valid direction.')
        self.current_direction = directions[new_direction]

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

            elif command == 'MOVE':
                toy_robot.move()
                if debug: assert toy_robot.current_coordinates == (0, 1)
                if debug: assert toy_robot.current_direction == 'NORTH'

            elif command == 'LEFT':
                toy_robot.set_direction('LEFT')
                if debug: assert toy_robot.current_direction == 'WEST'

            elif command == 'RIGHT':
                toy_robot.set_direction('RIGHT')
                if debug: assert toy_robot.current_direction == 'NORTH'

        command = input("Enter your command: ")