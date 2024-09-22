import random

class food:
    def __init__(self, position, board_limits):
        self.position = position
        self.board_limits = board_limits
    def get_position(self):
        return self.position
    def was_eaten(self, snake_position):
        return snake_position == self.position
    def move(self, snake_body):
        while True:
            new_position = (random.randint(0, self.board_limits[0] - 1), random.randint(0, self.board_limits[1] - 1))
            if new_position not in snake_body:
                self.position = new_position
                break

