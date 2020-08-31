# dz7-1

class Matrix:
    def __init__(self, data_1, data_2):
        self.data_1 = data_1
        self.data_2 = data_2

    def __add__(self):
        matrx = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.data_1)):

            for j in range(len(self.data_2[i])):
                matrx[i][j] = self.data_1[i][j] + self.data_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrx]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrx]))

my_matrix = Matrix([[9, 22, 15],
                    [10, 21, 27],
                    [45, 54, 13]],
                   [[49, 12, 6],
                    [10, 11, 97],
                    [28, 9, 101]])
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


print(my_matrix.__add__())