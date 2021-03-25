def create_copy(positions: list):
    """
    Create copy of board position so that the values don't point to each other.
    :param positions: board position array.
    :return: new list copy.
    """
    temp = []
    for i in positions:
        temp.append(i)
    return temp


def make_move(position, move: list):
    """
    Make a move and return a new Node object for a specific move
    :param position: board position.
    :param move: which tile is being swapped with blank space.
    :return: a new Node object for a specific move.
    """
    index_of_blank = position.index(0)  # Find index of blank space.
    if 0 <= move[0] < 3 and 0 <= move[1] < 3:  # Check if move is valid.
        temp_store = create_copy(position)  # Copy position.
        temp_store2 = temp_store[move[0] * 3 + move[1]]  # Temporarily store old position.
        temp_store[move[0] * 3 + move[1]] = temp_store[index_of_blank]  # Update non-blank.
        temp_store[index_of_blank] = temp_store2  # Update blank.
        return temp_store
    return None


class Node:
    def __init__(self, position: list, lvl: int, f: float, parent: Node):
        """
        Initialise Node object.
        :param position: the board state of the node.
        :param lvl: how many moves from start node.
        :param f: the cost assigned to the node by g + h.
        :param parent: the node this node was made from for creating path at the end.
        """
        self.position = position
        self.level = lvl
        self.f = f
        self.parent = parent

    def __lt__(self, other):
        """
        Comparator method for sorting the list in terms of f values.
        :param other: the other Node that it is being compared against.
        :return: if self node is less than or not less than the other node.
        """
        return self.f < other.f

    def get_neighbours(self):
        """
        Finds all the neighbours of the current node and returns them as [Node]
        :return: all the neighbours of the board state as [Node]
        """
        index_of_blank = self.position.index(0)
        x = int(index_of_blank / 3)
        y = index_of_blank % 3
        move_list = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]  # The four moves that the tile can go to.
        neighbours = []
        for move in move_list:  # For all the moves.
            neighbour = make_move(self.position, move)  # Make the new board state, also validates the move.
            if neighbour is not None:  # Make sure the neighbour exists.
                neighbours.append(Node(neighbour, self.level + 1, 0, self))  # Add the new node to a list of neighbours.
        return neighbours

    def print_node(self):
        """
        Display the node in the console
        """
        print("  " + u"\u2193")  # Down arrow
        print("=====")
        for i in range(9):
            print(str(self.position[i]) + str(" "), end="")
            if i == 2 or i == 5:
                print(" ")
        print()
        print("=====")
