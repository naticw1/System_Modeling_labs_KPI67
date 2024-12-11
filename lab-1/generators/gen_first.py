import random
import numpy as np

from .gen import GeneratorBase

class GeneratorFirst(GeneratorBase):
    def __init__(self, amount, intervals, a):
        self.A = a
        super().__init__(amount, intervals)

    def validate(self):
        print(
            "\n** Task 1 **\n" +
            f"Lambda: {self.A}\n" +
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        )
        self._get_analyze()

    def _create_array(self):
        x_array = []
        for _ in range(self.amount):
            val = -np.log(random.random()) / self.A
            x_array.append(val)
        return np.array(x_array)
    
    def _gen_dist(self):
        return [np.exp(-self.A * self.boundary_points[i][0]) -
                np.exp(-self.A * self.boundary_points[i][1])
                for i in range(self.intervals)]