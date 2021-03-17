class Digit:
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
        return Digit(data_values)

    def __truediv__(self, other):
        if other != 0:
            data_values = []
            for index in range(len(self.data)):
                data_values.append(self.data[index] / other)
            return Digit(data_values)
        return -1
