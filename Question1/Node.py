class Node:
    def __init__(self, position, lvl, f, parent):
        self.position = position
        self.level = lvl
        self.f = f
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

    def get_neighbours(self):
        index_of_blank = self.position.index(0)
        x = int(index_of_blank / 3)
        y = index_of_blank % 3
        move_list = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
        neighbours = []
        for move in move_list:
            neighbour = self.make_move(self.position, move)
            if neighbour is not None:
                neighbours.append(Node(neighbour, self.level + 1, 0, self))
        return neighbours

    def create_copy(self, positions):
        temp = []
        for i in positions:
            temp.append(i)
        return temp

    def make_move(self, position, move: list):
        index_of_blank = position.index(0)
        if 0 <= move[0] < 3 and 0 <= move[1] < 3:
            temp_store = self.create_copy(position)
            temp_store2 = temp_store[move[0] * 3 + move[1]]
            temp_store[move[0] * 3 + move[1]] = temp_store[index_of_blank]
            temp_store[index_of_blank] = temp_store2
            return temp_store
        return None

    def print_node(self):
        for i in range(9):
            print(str(self.position[i]) + str(" "), end="")
            if i == 2 or i == 5:
                print(" ")
