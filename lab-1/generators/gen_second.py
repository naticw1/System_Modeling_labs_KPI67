import random
import numpy as np
from scipy import integrate

from .gen import GeneratorBase

class GeneratorSecond(GeneratorBase):
    def __init__(self, amount, intervals, a, sigma):
        self.A = a
        self.sigma = sigma
        super().__init__(amount, intervals)

    def validate(self):
        print(
            "\n** Task 2 **\n" +
            f"Lambda: {self.A}\n" +
            f"Sigma: {self.sigma}\n" +
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        )
        self._get_analyze()

    def _create_array(self):
        x_array = []
        for _ in range(self.amount):
            myu = -6
            for _ in range(12):
                myu += random.random()
            val = self.sigma * myu + self.A
            x_array.append(val)
        return np.array(x_array)
    
    def _gen_dist(self):
        return [integrate.quad(
                lambda x: 1 / (self.sigma * np.sqrt(2 * np.pi)) * np.exp(- pow((x - self.A),2) / (2 * pow(self.sigma,2))),
                self.boundary_points[i][0],
                self.boundary_points[i][1])[0]
                for i in range(self.intervals)]