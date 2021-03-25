import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.manifold import Isomap
from Question2.ClusterMaker import ClusterMaker


class GraphDrawer:
    def __init__(self, datum, all_values):
        self.x_values, self.y_values = self.manipulate_data(datum)
        self.x_all, self.y_all = self.manipulate_data2(all_values)
        self.datum = datum

    def manipulate_data(self, datum):
        x_coords = []
        y_coords = []
        for i in datum:
            x_coord, y_coord = i.give_coords()
            x_coords.append(x_coord)
            y_coords.append(y_coord)
        return x_coords, y_coords

    def manipulate_data2(self, datum):
        x_coords = []
        y_coords = []
        for i in datum:
            if i:
                for j in i:
                    x_coord, y_coord = j.give_coords()
                    x_coords.append(x_coord)
                    y_coords.append(y_coord)
        return x_coords, y_coords

    def iso_thing(self):
        iso = Isomap(n_components=2)
        digits = load_digits(n_class=10)
        new_list = []
        for index in self.datum:
            new_list.append(index.data)
        projection = iso.fit_transform(digits.data)
        projection2 = iso.fit_transform(new_list)
        plt.scatter(
            projection2[:, 0], projection2[:, 1], c=["#FF0000" for _ in range(10)]
        )
        plt.scatter(
            projection[:, 0],
            projection[:, 1],
            lw=0.1,
            c=digits.target,
            cmap=plt.cm.get_cmap("cubehelix", 9),
        )
        plt.colorbar(ticks=range(10), label="digit value")
        plt.clim(-0.5, 9.5)
        plt.gca().set_facecolor("#F5F5DC")
        plt.show()

    def draw_graph(self):
        plt.plot(self.x_all, self.y_all, linestyle="None", marker="s")
        plt.show()

    def show_image(self, data):
        goat = np.reshape(data, (8, 8))
        plt.imshow(np.asmatrix(goat), interpolation="nearest", cmap="Greys")
        plt.show()


if __name__ == "__main__":
    cluster2 = ClusterMaker()
    data1, data2 = cluster2.k_means()
    graph = GraphDrawer(data1, data2)
    for i in range(len(data2)):
        print(len(data2[i]))
    for datum in data1:
        graph.show_image(datum.data)

    graph.iso_thing()
