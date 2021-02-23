class ToyRobot():

    def __init__(self) -> None:
        self.current_coordinates = None
        self.current_direction = None

    def report(self) -> tuple:
        return f"{self.current_coordinates[0]},{self.current_coordinates[1]},{self.current_direction}"

if __name__ == "__main__":
    ...