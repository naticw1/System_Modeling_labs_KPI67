import random
import math
import numpy as np

from .gen import GeneratorBase

class GeneratorThird(GeneratorBase):
    def __init__(self, amount, intervals, a, c):
        self.A = a
        self.C = c
        super().__init__(amount, intervals)

    def validate(self):
        print(
            "\n** Task 3 **\n" +
            f"A: 5^{round(math.log(self.A, 5))} (or {self.A})\n" +
            f"C: 2^{round(math.log(self.C, 2))} (or {self.C})\n" +
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        )
        self._get_analyze()

    def _create_array(self):
        z = self.A * random.random() % self.C
        x_array = []
        for _ in range(self.amount):
            z = self.A * z % self.C
            val = z / self.C
            x_array.append(val)
        return np.array(x_array)
    
    def _gen_dist(self):
        return [(self.boundary_points[i][1] - self.boundary_points[i][0]) /
                (max(self.created_dist) - min(self.created_dist))
                for i in range(self.intervals)]