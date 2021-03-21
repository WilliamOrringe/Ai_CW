import numpy as np
import matplotlib.pyplot as plt

from Question2.ClusterMaker import ClusterMaker


class GraphDrawer:
    def __init__(self, datum, all_values):
        self.x_values, self.y_values = self.manipulate_data(datum)
        self.x_all, self.y_all = self.manipulate_data2(all_values)

    def manipulate_data(self, datum):
        x_coords = []
        y_coords = []
        for i in datum:
            x_coord, y_coord = (i.give_coords())
            x_coords.append(x_coord)
            y_coords.append(y_coord)
        return x_coords, y_coords

    def manipulate_data2(self, datum):
        x_coords = []
        y_coords = []
        for i in datum:
            if i != []:
                for j in i:
                    x_coord, y_coord = (j.give_coords())
                    x_coords.append(x_coord)
                    y_coords.append(y_coord)
        return x_coords, y_coords

    def draw_graph(self):
        plt.plot(self.x_all, self.y_all, linestyle='None',
                 marker="s")
        plt.show()


if __name__ == "__main__":
    cluster2 = ClusterMaker()
    data1, data2 = cluster2.k_means()
    graph = GraphDrawer(data1, data2)
    graph.draw_graph()
