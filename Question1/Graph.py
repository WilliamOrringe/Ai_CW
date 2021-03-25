import math

from Node import Node


def in_list(node_object: Node, nodes_list: list):
    """
    Checks to see if an object is in the list.
    :param node_object: the object to search for.
    :param nodes_list:  the list of objects to search in.
    :return: object if found otherwise returns false.
    """
    for node in nodes_list:  # Loops through the nodes.
        if node.position == node_object.position:  # Checks if the node matches this particular one in the list.
            return node
    return False


def find_route(finish_node):
    """
    Generates a list of the parent node of the current_node and then repeats until
    the current node is the starting node.
    :param finish_node: the final node that is equal to the goal node
    :return: the path list
    """
    current_node = finish_node
    path_list = []
    while current_node.parent is not None:
        path_list.append(current_node)
        current_node = current_node.parent
    return path_list + [current_node]


class Graph:
    """
    Has the distance heuristic and the a_star function.
    """
    def __init__(self, start_state, goal_state, euclidean_state=False):
        """
        Sets up the start node and other parameters.
        :param start_state: start board state.
        :param goal_state:  goal board state.
        :param euclidean_state:  if euclidean distance or not.
        """
        self.open_nodes = []
        self.closed_nodes = []
        self.size = 3
        self.start = Node(start_state, 0, 0, None)
        self.goal = goal_state
        self.euclidean = euclidean_state

    def manhattan_distance(self, start_index, final_index):
        """
        Finds the manhattan distance between two indexes.
        :param start_index: the index of the current position
        :param final_index: the index of the same number in the goal board
        :return: the manhattan distance
        """
        return abs((start_index / self.size) - (final_index / self.size)) + abs(
            (start_index % self.size) - (final_index % self.size)
        )

    def euclidean_distance(self, start_index, final_index):
        """
        Finds the euclidean distance between two indexes.
        :param start_index: the index of the current position
        :param final_index: the index of the same number in the goal board
        :return: the euclidean distance
        """
        return math.sqrt(
            ((final_index / self.size) - (start_index / self.size)) ** 2
            + ((final_index % self.size) - (start_index % self.size)) ** 2
        )

    def distance_to_goal(self, current, goal_state, euclidean_state):
        """
        Finds the distance to goal from the current state to goal state using
        the specified distance function.
        :param current: the current board state
        :param goal_state: the goal state
        :param euclidean_state: which distance function to use
        :return: the distance
        """
        total = 0
        for i in range(9):
            if euclidean_state:
                total += self.euclidean_distance(i, goal_state.index(current[i]))
            else:
                total += self.manhattan_distance(i, goal_state.index(current[i]))
        return total

    def find_f(self, current, goal_state):
        """
        Finds the f cost of the position and returns it.
        :param current: the current board state
        :param goal_state: the goal state
        :return: g + h
        """
        return (
            self.distance_to_goal(current.position, goal_state, self.euclidean)
            + current.level
        )

    def add_to_open(self, neighbor):
        """
        Checks to see if the node is in the open list and if it is it checks if the
        f cost is lower for the one it has found than the one in the open list.
        :param neighbor: the node that is being checked.
        :return: If lower f cost and in the list then it will return true otherwise false.
        """
        for node in self.open_nodes:
            if neighbor == node and neighbor.f >= node.f:
                return False
        return True

    def a_star(self):
        """
        Performs the a_star search.
        :return: Tuple: (path_list, iteration_count).
        """
        self.open_nodes.append(self.start)  # Adds the start node to the open list.
        counter = 0
        while len(self.open_nodes) > 0:  # While open list is not empty.
            counter += 1
            self.open_nodes.sort()  # Sort the open list in terms of f cost (lowest -> highest).
            current_node = self.open_nodes.pop(0)  # Remove the current node from the open list.
            self.closed_nodes.append(current_node)  # Add the current node to the closed list.
            if current_node.position == self.goal:  # Check if the current node is the goal node.
                # Output data to the console about the performance.
                print("Moves = " + str(current_node.level))
                print("Iterations: ", counter - 1)
                print("Number of nodes in open list: ", len(self.open_nodes))
                print("Number of nodes visited: ", len(self.closed_nodes))
                print(
                    "Total nodes generated: ",
                    (len(self.closed_nodes) + len(self.open_nodes)),
                )
                print("======")
                path_list = find_route(current_node)  # Find the path.
                path_list.reverse()  # Reverse the order so it goes Start -> Goal.
                return path_list, counter - 1  # Return the result.
            neighbours = current_node.get_neighbours()  # Find the neighbours of the current node.
            for neighbour in neighbours:  # Loop through each neighbour.
                if in_list(neighbour, self.closed_nodes):  # Check to see if it is in the closed list.
                    continue
                neighbour.f = self.find_f(neighbour, self.goal)  # Find the f cost otherwise.
                if self.add_to_open(neighbour):  # Check to see if it should be added to the open list.
                    self.open_nodes.append(neighbour)  # Add to the open list.


if __name__ == "__main__":
    start = "724506831"
    goal = "012345678"
    euclidean = False
    start_list = [int(val) for val in start]
    goal_list = [int(val) for val in goal]
    graph = Graph(start_list, goal_list, euclidean)
    path_l, _ = graph.a_star()
    [path.print_node() for path in path_l]
