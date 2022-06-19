from cell import Cell


class Grille:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.matrix = self.set_matrix()

    def set_matrix(self):
        matrix = []
        for i in range(self.height):
            line_i = []
            for j in range(self.width):
                line_i.append(Cell())
            matrix.append(line_i)
        return matrix
