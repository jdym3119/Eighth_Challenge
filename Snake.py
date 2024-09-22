class snake:
    def __init__(self, initial_position: tuple):
        self.initial_position = initial_position
        self.length = 1
        self.score = self.length - 1
        self.body = [initial_position]
        self.direction = "right"
        self.directions = ["left", "up", "down", "right"]
        self.opposed_directions = {"left": "right", "up": "down", "down": "up", "right": "left"}
    def move(self):
        head_x, head_y = self.body[-1]
        if self.direction == "left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "down":
            new_head = (head_x, head_y + 1)
        elif self.direction == "right":
            new_head = (head_x + 1, head_y)
        self.body.append(new_head)
        if len(self.body) > self.length:
            self.body.pop(0)
    def grow(self):
        self.length += 1
        self.score += 1
    def change_direction(self, new_direction):
        if new_direction in self.directions and new_direction != self.opposed_directions[self.direction]:
            self.direction = new_direction
    def is_dead(self, board):
        head = self.body[-1]
        return head in self.body[:-1] or not board.is_within_limits(head)
