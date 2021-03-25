import math

from Node import Node


def in_list(node_object: Node, nodes_list: list):
    for node in nodes_list:
        if node.position == node_object.position:
            return node
    return False


def find_route(finish_node):
    current_node = finish_node
    path_list = []
    while current_node.parent is not None:
        path_list.append(current_node)
        current_node = current_node.parent
    return path_list + [current_node]


class Graph:
    def __init__(self, start_state, goal_state, euclidean_state=False):
        self.open_nodes = []
        self.closed_nodes = []
        self.size = 3
        self.start = Node(start_state, 0, 0, None)
        self.goal = goal_state
        self.euclidean = euclidean_state

    def manhattan_distance(self, start_index, final_index):
        return abs((start_index / self.size) - (final_index / self.size)) + abs(
            (start_index % self.size) - (final_index % self.size)
        )

    def euclidean_distance(self, start_index, final_index):
        return math.sqrt(
            ((final_index / self.size) - (start_index / self.size)) ** 2
            + ((final_index % self.size) - (start_index % self.size)) ** 2
        )

    def distance_to_goal(self, current, goal_state, euclidean_state):
        total = 0
        for i in range(9):
            if euclidean_state:
                total += self.euclidean_distance(i, goal_state.index(current[i]))
            else:
                total += self.manhattan_distance(i, goal_state.index(current[i]))
        return total

    def find_f(self, current, goal_state):
        return (
            self.distance_to_goal(current.position, goal_state, self.euclidean)
            + current.level
        )

    def add_to_open(self, neighbor):
        for node in self.open_nodes:
            if neighbor == node and neighbor.f >= node.f:
                return False
        return True

    def a_star(self):

        self.open_nodes.append(self.start)
        counter = 0
        while len(self.open_nodes) > 0:
            counter += 1
            self.open_nodes.sort()
            current_node = self.open_nodes.pop(0)
            self.closed_nodes.append(current_node)
            if current_node.position == self.goal:
                print("Moves = " + str(current_node.level))
                print("Iterations: ", counter - 1)
                print("Number of nodes in open list: ", len(self.open_nodes))
                print("Number of nodes visited: ", len(self.closed_nodes))
                print(
                    "Total nodes generated: ",
                    (len(self.closed_nodes) + len(self.open_nodes)),
                )
                print("======")
                path_list = find_route(current_node)
                path_list.reverse()
                return path_list, counter - 1
            neighbours = current_node.get_neighbours()
            for neighbour in neighbours:
                if in_list(neighbour, self.closed_nodes):
                    continue
                neighbour.f = self.find_f(neighbour, self.goal)
                if self.add_to_open(neighbour):
                    self.open_nodes.append(neighbour)


if __name__ == "__main__":
    start = "724506831"
    goal = "012345678"
    euclidean = False
    start_list = [int(val) for val in start]
    goal_list = [int(val) for val in goal]
    graph = Graph(start_list, goal_list, euclidean)
    path_l, _ = graph.a_star()
    [path.print_node() for path in path_l]
