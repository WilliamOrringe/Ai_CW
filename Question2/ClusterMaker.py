import math
import random
from random import randint
from time import sleep

from sklearn.datasets import load_digits
from Digit import Image


class ClusterMaker:
    def __init__(self):
        self.digits = load_digits()
        self.cluster_number = 10
        self.clusters_positions = self.randomise_clusters2()
        self.clusters = []
        self.image_clusters = []
        self.images = []
        for digit in self.digits["data"]:
            self.images.append(Image(digit))

        for cluster in self.clusters_positions:
            self.clusters.append(Image(cluster))

    def randomise_clusters(self):
        cluster_positions = []
        for _ in range(self.cluster_number):
            cluster_positions.append([float((randint(0, 100)) / 100) for _ in range(64)])
        return cluster_positions

    def randomise_clusters2(self):
        cluster_positions = []
        for _ in range(self.cluster_number):
            cluster_positions.append(random.choice(self.digits.data))
        return cluster_positions

    def distance(self, image: Image, cluster_location: Image):
        total = 0
        for index in range(len(image.data)):
            total += (image.data[index] - cluster_location.data[index])**2
        return math.sqrt(total)

    def distance_all(self, image: Image, cluster_locations: [Image]):
        distances = []
        for cluster in cluster_locations:
            distances.append(self.distance(image, cluster))
        temp_distance = []
        for i in distances:
            temp_distance.append(i)
        temp_distance.sort()
        return distances.index(temp_distance[0])

    def distance_all_all(self, images: [Image], cluster_locations: [Image]):
        for image in images:
            image.cluster = self.distance_all(image, cluster_locations)

    def assign_cluster_list(self):
        self.image_clusters = [[], [], [], [], [], [], [], [], [], []]
        for image in self.images:
            self.image_clusters[image.cluster].append(image)

    def recalculate_clusters(self):
        self.clusters = []
        for cluster in self.image_clusters:
            adder = Image()
            for image in cluster:
                adder = adder + image
            self.clusters.append(adder / len(cluster))

    def k_means(self):
        for i in range(30):
            temp_clusters = self.clusters
            self.distance_all_all(self.images, self.clusters)
            self.assign_cluster_list()
            self.recalculate_clusters()
            if self.clusters == temp_clusters:
                print("finished", i)
                break
        return self.clusters, self.image_clusters


if __name__ == "__main__":
    cluster2 = ClusterMaker()
    goat = cluster2.k_means()

