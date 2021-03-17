import tkinter as tk

from Question1 import Node
from Question1.Graph import Graph


class View(tk.Frame):
    def __init__(self, data: [Node], move, master=None):
        super().__init__(master)
        self.labels = []
        self.data = data
        self.move = move
        self.master = master
        self.pack()
        self.create_grid(move)
        self.buttons()

    def create_grid(self, move):
        current_data = self.data[move].position
        for i in range(9):
            display_data = str(current_data[i]) if current_data[i] != 0 else ""
            self.labels.append(tk.Label(self, text=display_data, borderwidth=2, relief="solid", width=7,
                                        height=3, font=("courier", 24)).grid(row=i // 3, column=i % 3))
        self.move_number = tk.Label(self, text="Move number : " + str(self.move), borderwidth=2, relief="raised",
                                    ).grid(row=4, column=1)

    def buttons(self):
        self.previous = tk.Button(self, text="Previous", command=self.previous_command).grid(row=4, column=0)
        self.next = tk.Button(self, text="Next", command=self.next_command).grid(row=4, column=2)
        self.specify = tk.Button(self, text="Input you own board", command=self.next_command).grid(row=5, column=1)

    def previous_command(self):
        if self.move > 0:
            self.move -= 1
        self.create_grid(self.move)

    def next_command(self):
        if self.move < len(self.data)-1:
            self.move += 1
        self.create_grid(self.move)


if __name__ == '__main__':
    graph = Graph()
    data_list = graph.a_star()
    root = tk.Tk(className="Path Visualiser")
    root.geometry('580x500')
    app = View(data_list, 0, root)
    app.mainloop()
