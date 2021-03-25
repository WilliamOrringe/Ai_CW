import tkinter as tk

from Question1 import Node
from Question1.Graph import Graph


def validate_inputs(text: str):
    """
    Check if the input board state contains one of each number between 0-8 and only once
    with correct length and return if it is valid.
    :param text: the board state to be validated.
    :return: if it is valid or not
    """
    if len(text) == 9:
        numbers = set([int(i) for i in text])
        goal = {0, 1, 2, 3, 4, 5, 6, 7, 8}
        return numbers == goal
    return False


class View(tk.Frame):
    """
    Shows the interface.
    """
    def __init__(self, data_list: [Node], iteration_count: int, move, master=None):
        """
        This initialises the frame for the interface.
        :param data_list: the route from the start state to goal state
        :param iteration_count: how many iterations it took
        :param move: the board state we are looking at
        :param master: parent of the frame
        """
        super().__init__(master)
        # Setting up labels and buttons for the interface
        self.move_number = tk.Label(self, borderwidth=2, relief="raised")
        self.previous = tk.Button(
            self, text="Previous", command=self.previous_command
        ).grid(row=4, column=0)
        self.next = tk.Button(self, text="Next", command=self.next_command).grid(
            row=4, column=2
        )
        self.specify = tk.Label(self)
        self.start = tk.Text(self, width=3, height=3, font=("courier", 20))
        self.start_label = tk.Label(self, text="Start", borderwidth=2, relief="raised")
        self.goal_label = tk.Label(self, text="Goal", borderwidth=2, relief="raised")
        self.submit = tk.Button(
            self, text="Submit", width=7, height=2, command=self.submit_state
        )
        self.goal = tk.Text(self, width=3, height=3, font=("courier", 20))
        self.euclidean = tk.StringVar(self)
        self.heuristic = tk.OptionMenu(
            self, self.euclidean, "Manhattan-Distance", "Euclidean-Distance"
        )
        # Assigning data from constructor
        self.labels = []
        self.data = data_list
        self.move = move
        self.iterations = iteration_count
        self.master = master
        self.pack()
        self.create_grid(move)
        self.buttons()
        self.state_creator()

    def create_grid(self, move):
        """
        Shows the grid for the numbers, to show each board state in the grid.
        :param move: which move we are looking at.
        :return: nothing
        """
        current_data = self.data[
            move
        ].position  # Get the data for the move we are looking at
        new_list = root.grid_slaves()
        for item in new_list:  # Delete the old buttons and labels in the grid.
            item.destroy()
        for i in range(9):
            display_data = (
                str(current_data[i]) if current_data[i] != 0 else ""
            )  # Show blank if data at point == 0
            self.labels.append(
                tk.Label(
                    self,
                    text=display_data,
                    borderwidth=2,
                    relief="solid",
                    width=9,
                    height=3,
                    font=("courier", 24),
                ).grid(row=i // 3, column=i % 3)
            )  # Append all the data to a list of labels so it will get displayed in the grid.

        self.move_number.configure(
            text="Move number : " + str(self.move) + "/" + str(len(self.data) - 1)
        )  # Update what move we are looking at.
        self.move_number.grid(row=4, column=1)  # Add to the grid view.

    def buttons(self):
        """
        display the buttons.
        """
        self.specify.configure(
            text="Iterations : " + str(self.iterations)
        )  # Update what is on the label for
        # iterations.
        self.specify.grid(row=5, column=1)  # Add to the grid.

    def previous_command(self):
        """
        Show the previous board state by subtracting one from what the move is at.
        """
        if self.move > 0:
            self.move -= 1
        self.create_grid(self.move)

    def next_command(self):
        """
        Show the next board state by adding one from what the move is at.
        """
        if self.move < len(self.data) - 1:
            self.move += 1
        self.create_grid(self.move)

    def state_creator(self):
        """
        Add all the labels to the grid and set up default values and buttons.
        """
        # Adding to grid
        self.start_label.grid(row=6, column=0)
        self.goal_label.grid(row=6, column=1)
        self.start.grid(row=7, column=0)
        self.goal.grid(row=7, column=1)
        self.heuristic.grid(row=6, column=2)
        self.submit.grid(row=7, column=2)
        # Setting default value
        self.euclidean.set("Manhattan-Distance")

    def submit_state(self):
        """
        Update the start and goal state if they are valid and use the
        distance function that is selected and call the a-star function
        with these new inputs and display this new data.
        """
        # Get start input and strip new line character.
        start_input = self.start.get("1.0", "end")
        start_input = start_input.rstrip("\n")
        start_valid = validate_inputs(start_input)  # Check if start input is valid.
        if not start_valid:  # Display text if invalid/valid.
            self.start_label.config(text="Start-Invalid")
        else:
            self.start_label.config(text="Start-Valid")
        # Get goal input and strip new line character.
        goal_input = self.goal.get("1.0", "end")
        goal_input = goal_input.rstrip("\n")
        goal_valid = validate_inputs(goal_input)  # Check if goal input is valid.
        if not goal_valid:  # Display text if invalid/valid.
            self.goal_label.config(text="Goal-Invalid")
        else:
            self.goal_label.config(text="Goal-Valid")
        if (
            start_valid and goal_valid
        ):  # If the goal and start inputs are valid call a star with the new inputs
            euclidean = (
                self.euclidean.get() == "Euclidean-Distance"
            )  # Check which distance function
            self.data, self.iterations = setup(
                start_input, goal_input, euclidean
            )  # Use new state
            self.create_grid(0)  # Reset grid and buttons
            self.buttons()
        else:
            euclidean = (
                self.euclidean.get() == "Euclidean-Distance"
            )  # Check which distance function
            self.data, self.iterations = setup(
                "724506831", "012345678", euclidean
            )  # Use default state
            self.create_grid(0)  # Reset grid and buttons
            self.buttons()


def setup(start: str, goal: str, euclidean=False):
    """
    Handling the start, goal and distance function parameters and parsing this to the
    a_star function and getting the path and how many iterations this took back and returning it
    :param start: start board state
    :param goal: goal board state
    :param euclidean: if the distance function to be used is euclidean or not.
    :return: tuple: (path_list, iteration_count)
    """
    # Converting the strings to int arrays
    start_list = [int(val) for val in start]
    goal_list = [int(val) for val in goal]
    # Setting up new instance of Graph class
    graph = Graph(start_list, goal_list, euclidean)
    # Calling a_star and returning it
    return graph.a_star()


if __name__ == "__main__":
    root = tk.Tk(className="Path Visualiser")
    root.geometry("580x540")
    data, iterations = setup("724506831", "012345678")
    # optional parameter of which distance function to perform before window opens
    app = View(data, iterations, 0, root)  # Create view for the interface.
    app.mainloop()
