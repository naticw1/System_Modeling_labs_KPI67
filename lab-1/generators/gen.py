import statistics as stats
import pandas as pd

import generators.utils as utils

class GeneratorBase:
    def __init__(self, amount, intervals):
        self.amount = amount
        self.intervals = intervals
        
        self.created_dist = self._create_array()

        self.mean_value = stats.mean(self.created_dist)
        self.dispersion = stats.pvariance(self.created_dist)

        self.entries = utils.count_entries(self.created_dist, self.intervals)
        self.boundary_points = utils.get_boundary_points(self.entries, self.intervals)

        self.perfect_dist = self._gen_dist()

    def _get_analyze(self):
        entry_count = [i[1] for i in self.entries]
        observed_chi_2, expected_chi_2 = utils.observed_expected_chi2(
            self.perfect_dist, entry_count, self.intervals, self.amount)

        distribution_result = (
            "Distribution matches theoretical model"
            if observed_chi_2 < expected_chi_2
            else "Distribution does not match theoretical model"
        )

        print(
                       
            f"{pd.DataFrame(self.entries)}\n" +
            "=" * 50 + "\n" +
            f"Dispersion: {self.mean_value}\n" +
            f"Variance: {self.dispersion}\n" +
            f"Observed chi2: {observed_chi_2}\n" +
            f"Expected chi2: {expected_chi_2}\n" +
            "=" * 50 + "\n" +
            f"{distribution_result}\n"
        )

        
        utils.plot_histogram(self.intervals, self.created_dist)

    def validate(self):
        pass


    def _create_array(self):
        pass

    
    def _gen_dist(self):
        pass
