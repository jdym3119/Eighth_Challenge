from Snake import snake
from Food import food
import tkinter as tk
from tkinter import messagebox

class board:
    def __init__(self, num_cells_x, num_cells_y, cell_size):
        self.num_cells_x = num_cells_x
        self.num_cells_y = num_cells_y
        self.cell_size = cell_size
        self.dimensions = (num_cells_x * cell_size, num_cells_y * cell_size)
        self.limits = (num_cells_x, num_cells_y)
        self.score_label = None
    def is_within_limits(self, snake_position):
        x, y = snake_position
        return 0 <= x < self.limits[0] and 0 <= y < self.limits[1]
    def draw(self, snake, food, draw_snake=True, draw_food=True):
        self.canvas.delete("all")
        if draw_snake:
            for x, y in snake.body:
                self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size, (x + 1) * self.cell_size, (y + 1) * self.cell_size, fill="green", outline="black")
        if draw_food:
            food_x, food_y = food.get_position()
            self.canvas.create_rectangle(food_x * self.cell_size, food_y * self.cell_size, (food_x + 1) * self.cell_size, (food_y + 1) * self.cell_size, fill="red", outline="black")
        self.score_label.config(text=f"Score: {sk.score}")
    def start_game(self):
        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.root.config(bg="black")
        self.root.geometry(f"{self.dimensions[0]}x{self.dimensions[1]+100}")
        self.score_frame = tk.Frame(self.root)
        self.score_frame.pack(fill=tk.X, side=tk.TOP)
        self.score_label = tk.Label(self.root, text=f"Score: {sk.score}", font=("Arial", 20,), bg="black", fg="white")
        self.score_label.pack()
        self.button_frame = tk.Frame(self.root, bg="black")
        self.button_frame.pack(fill=tk.X, side=tk.BOTTOM)
        self.reset_button = tk.Button(self.button_frame, text="Reset", font=("Arial", 14), command=self.reset_game, bg="gray", fg="white")
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.exit_button = tk.Button(self.button_frame, text="Exit", font=("Arial", 14), command=self.exit, bg="red", fg="white")
        self.exit_button.pack(side=tk.RIGHT, padx=10, pady=10)
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()
        self.canvas = tk.Canvas(self.game_frame, width=self.dimensions[0], height=self.dimensions[1], bg="#13df1c")
        self.canvas.pack()
        self.update()
        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.mainloop()
    def update(self):
        sk.move()
        if sk.is_dead(self):
            self.show_game_over()
            return
        if fd.was_eaten(sk.body[-1]):
            sk.grow()
            fd.move(sk.body)
        self.draw(sk, fd)
        self.root.after(100, self.update)
    def on_key_press(self, event):
        direction = event.keysym
        if direction in ["Left", "Right", "Up", "Down"]:
            sk.change_direction(direction.lower())
    def reset_game(self):
        self.canvas.delete("all")
        self.score_label.config(text="Score: 0")
        sk.body = [sk.initial_position]
        sk.length = 1
        sk.score = 0
        sk.direction = "right"
        fd.position = (10, 10)
        self.update()
    def exit(self):
        self.root.quit()
    def show_game_over(self):
        self.root.after_cancel(self.update)
        game_over_popup = tk.Toplevel(self.root)
        game_over_popup.title("Game Over")
        game_over_popup.geometry("200x100")
        game_over_popup.config(bg="black")
        label = tk.Label(game_over_popup, text="Game Over!", font=("Arial", 14), bg="black", fg="white")
        label.pack(pady=10)
        reset_button = tk.Button(game_over_popup, text="Reset", font=("Arial", 12), command=lambda: [game_over_popup.destroy(), self.reset_game()], bg="gray", fg="white")
        reset_button.pack(side=tk.LEFT, padx=10, pady=10)
        exit_button = tk.Button(game_over_popup, text="Exit", font=("Arial", 12), command=self.exit, bg="red", fg="white")
        exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

if __name__ == '__main__':
    bd = board(num_cells_x=20, num_cells_y=15, cell_size=25)
    sk = snake(initial_position=(5, 5))
    fd = food(position=(10, 10), board_limits=(20, 15))
    bd.start_game()
