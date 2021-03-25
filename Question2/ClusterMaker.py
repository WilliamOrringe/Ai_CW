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

    def randomise_clusters2(self):
        cluster_positions = []
        print(len(self.digits.target))
        for i in range(self.cluster_number):
            store = random.randint(0, self.cluster_number)
            rand_number = self.digits.target[store]
            print(rand_number)
            while rand_number != i:
                store = random.randint(0, self.cluster_number)
                rand_number = self.digits.target[store]
            cluster_positions.append(rand_number.data[store])
        return cluster_positions

    def distance(self, image: Image, cluster_location: Image):
        total = 0
        for index in range(len(image.data)):
            total += abs(image.data[index] - cluster_location.data[index])
        return total

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
        image_clusters = [[], [], [], [], [], [], [], [], [], []]
        for image in self.images:
            image_clusters[image.cluster].append(image)
        return image_clusters

    def recalculate_clusters(self):
        clusters = []
        for cluster in self.image_clusters:
            adder = Image()
            for image in cluster:
                adder = adder + image
            clusters.append(adder / len(cluster))
        return clusters

    def k_means(self):
        for i in range(30):
            temp_clusters = []
            for j in range(len(self.clusters)):
                temp_clusters.append(self.clusters[j])
            self.distance_all_all(self.images, self.clusters)
            self.image_clusters = self.assign_cluster_list()
            self.clusters = self.recalculate_clusters()
            print(i)
        return self.clusters, self.image_clusters


if __name__ == "__main__":
    cluster2 = ClusterMaker()
    goat = cluster2.k_means()
