class TableTop():

    def __init__(self) -> None:
        self.rows = None
        self.columns = None


class ToyRobot():

    def __init__(self) -> None:
        self.current_coordinates = None
        self.current_direction = None
        self.current_table_top = None

    def report(self) -> tuple:
        return f"{self.current_coordinates[0]},{self.current_coordinates[1]},{self.current_direction}"

    def call_command(self, command) -> None:

        place = command.split(' ')
        if place[0] == 'PLACE':
            self.place(command)
        elif self.current_direction and self.current_coordinates:
            if command == 'REPORT':
                print(self.report())
            elif command == 'MOVE':
                self.move()
            elif command == 'LEFT':
                self.set_direction('LEFT')
            elif command == 'RIGHT':
                self.set_direction('RIGHT')

        more_commands = True
        while more_commands:
            command = input("Enter your command: ")
            self.call_command(command)

    #TODO Add handling of incorrect entries
    def place(self, command) -> None:
        """Sets the current_coordinates and current_direction

        Args:
            command (String): The place command the user has entered
        """

        command = command.split(' ')
        command = command[1].split(',')
        coordinates = (int(command[0]), int(command[1]))
        direction = command[2]

        if direction not in ['NORTH', 'SOUTH', 'EAST', 'WEST']:
            print(f'{direction} is not a valid direction.')
        elif coordinates[0] >= self.current_table_top.rows or coordinates[1] >= self.current_table_top.columns or (coordinates[0] or coordinates[1]) < 0:
            print(f'The coordinates, {coordinates},  are not valid')
        else:
            self.current_coordinates = coordinates
            self.current_direction = direction

    def move(self) -> None:
        """Moves the toy robot forward one spot depending on the direction it faces"""

        if self.current_direction == 'EAST':
            x_cord = self.current_coordinates[0]
            if x_cord + 1 < self.current_table_top.rows:
                self.current_coordinates = (x_cord + 1, self.current_coordinates[1])

        elif self.current_direction == 'WEST':
            x_cord = self.current_coordinates[0]
            if x_cord - 1 >= 0:
                self.current_coordinates = (x_cord - 1, self.current_coordinates[1])

        elif self.current_direction == 'NORTH':
            y_cord = self.current_coordinates[1]
            if y_cord + 1 < self.current_table_top.columns:
                self.current_coordinates = (self.current_coordinates[0], y_cord + 1)

        elif self.current_direction == 'SOUTH':
            y_cord = self.current_coordinates[1]
            if y_cord - 1 >= 0:
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
    debug = False

    # Instantiate the default 5x5 TableTop
    #? How would I handle multiple TableTops

    tabletop_one = TableTop()
    tabletop_one.rows = 5
    tabletop_one.columns = 5

    #? How would I handle multiple ToyRobots
    toy_robot = ToyRobot()
    toy_robot.current_table_top = tabletop_one

    command = input("Enter your command: ")
    place = command.split(' ')[0]
    while place != 'PLACE':
        command = input("Enter your command: ")
        place = command.split(' ')[0]
    else:
        toy_robot.call_command(command)
