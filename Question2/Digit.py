class Image:
    def __init__(self, data=None, cluster=None):
        if data is None:
            self.data = self.set_data_to_zero()
        else:
            self.data = data
        self.cluster = cluster

    def set_data_to_zero(self):
        values = []
        for i in range(64):
            values.append(0)
        return values

    def __add__(self, other):
        data_values = []
        for index in range(len(self.data)):
            data_values.append(self.data[index] + other.data[index])
        return Image(data_values)

    def __truediv__(self, other: int):
        if other == 0:
            other += 1

        data_values = []
        for index in range(len(self.data)):
            data_values.append(self.data[index] / other)
        return Image(data_values)

    def give_coords(self):
        x = 0
        for i in range(32):
            x += self.data[i]
        x /= 32
        y = 0
        for j in range(32, 64):
            y += self.data[i]
        y /= 32
        return x, y
