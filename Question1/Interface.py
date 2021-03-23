import tkinter as tk

from Question1 import Node
from Question1.Graph import Graph


class View(tk.Frame):
    def __init__(self, data: [Node], iterations: int, move, master=None):
        super().__init__(master)
        self.labels = []
        self.data = data
        self.move = move
        self.iterations = iterations
        self.master = master
        self.pack()
        self.create_grid(move)
        self.buttons()
        self.state_creator()

    def create_grid(self, move):
        current_data = self.data[move].position
        new_list = root.grid_slaves()
        for item in new_list:
            item.destroy()
        for i in range(9):
            display_data = str(current_data[i]) if current_data[i] != 0 else ""
            self.labels.append(tk.Label(self, text=display_data, borderwidth=2, relief="solid", width=9,
                                        height=3, font=("courier", 24)).grid(row=i // 3, column=i % 3))

        self.move_number = tk.Label(self, borderwidth=2, relief="raised")
        self.move_number.configure(text="Move number : " + str(self.move) + "/" + str(len(self.data)-1))
        self.move_number.grid(row=4, column=1)

    def buttons(self):
        self.previous = tk.Button(self, text="Previous", command=self.previous_command).grid(row=4, column=0)
        self.next = tk.Button(self, text="Next", command=self.next_command).grid(row=4, column=2)
        self.specify = tk.Label(self)
        self.specify.configure(text="Iterations : " + str(self.iterations))
        self.specify.grid(row=5, column=1)

    def previous_command(self):
        if self.move > 0:
            self.move -= 1
        self.create_grid(self.move)

    def next_command(self):
        if self.move < len(self.data) - 1:
            self.move += 1
        self.create_grid(self.move)

    def state_creator(self):
        self.start_label = tk.Label(self, text="Start", borderwidth=2, relief="raised")
        self.start_label.grid(row=6, column=0)

        self.goal_label = tk.Label(self, text="Goal", borderwidth=2, relief="raised")
        self.goal_label.grid(row=6, column=1)

        self.start = tk.Text(self, width=3, height=3, font=("courier", 20))
        self.start.grid(row=7, column=0)

        self.goal = tk.Text(self, width=3, height=3, font=("courier", 20))
        self.goal.grid(row=7, column=1)

        self.euclidean = tk.StringVar(self)
        self.euclidean.set("Manhattan-Distance")
        self.heuristic = tk.OptionMenu(self, self.euclidean, "Manhattan-Distance", "Euclidean-Distance")
        self.heuristic.grid(row=6, column=2)

        self.submit = tk.Button(self, text="Submit", width=7, height=2, command=self.submit_state)
        self.submit.grid(row=7, column=2)

    def submit_state(self):
        start_input = self.start.get("1.0", "end")
        start_input = start_input.rstrip("\n")
        start_valid = self.validate_inputs(start_input)
        if not start_valid:
            self.start_label.config(text="Start-Invalid")
        else:
            self.start_label.config(text="Start-Valid")

        goal_input = self.goal.get("1.0", "end")
        goal_input = goal_input.rstrip("\n")
        goal_valid = self.validate_inputs(goal_input)
        if not goal_valid:
            self.goal_label.config(text="Goal-Invalid")
        else:
            self.goal_label.config(text="Goal-Valid")
        if start_valid and goal_valid:
            euclidean = self.euclidean.get() == "Euclidean-Distance"
            self.data, self.iterations = setup(start_input, goal_input, euclidean)
            self.create_grid(0)
            self.buttons()
        else:
            euclidean = self.euclidean.get() == "Euclidean-Distance"
            self.data, self.iterations = setup("724506831", "012345678", euclidean)
            self.create_grid(0)
            self.buttons()

    def validate_inputs(self, text: str):
        if len(text) == 9:
            numbers = set([int(i) for i in text])
            goal = {0, 1, 2, 3, 4, 5, 6, 7, 8}
            return numbers == goal
        return False


def setup(start, goal, euclidean=False):
    start_list = [int(val) for val in start]
    goal_list = [int(val) for val in goal]
    graph = Graph(start_list, goal_list, euclidean)
    return graph.a_star()


if __name__ == '__main__':
    root = tk.Tk(className="Path Visualiser")
    root.geometry('580x540')
    data, iterations = setup("724506831", "012345678")
    app = View(data, iterations, 0, root)
    app.mainloop()
