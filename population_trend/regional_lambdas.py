import numpy as np
import json

from bootstrapping_tools import calculate_intervals_from_p_values_and_alpha

from population_trend import Bootstrap_from_time_series


class Island_Bootstrap_Distribution_Concatenator:
    def __init__(self, paths):
        self.paths_string = paths
        self.distributions = self.read_json_files()

    def split_paths(self):
        splited_paths = self.paths_string.split(",")
        clean_paths = [path.strip() for path in splited_paths]
        return clean_paths

    def read_json_files(self):
        splited_paths = self.split_paths()
        json_list = []
        for path in splited_paths:
            with open(path) as json_file:
                json_content = json.load(json_file)
            json_list.append(json_content)
        return json_list


def read_distribution(json_dict):
    completed_distribution = json_dict["bootstrap_intermediate_distribution"]
    lambdas_distribution = [sample[0] for sample in completed_distribution]
    return lambdas_distribution


def concatenate_distribution(*argv):
    rng = np.random.default_rng()
    list_of_distributions = []
    for arg in argv:
        resampled = rng.choice(arg, size=2000, replace=True)
        list_of_distributions.append(resampled)
    return np.array(list_of_distributions).T


def mean_by_row(concatenated_distributions):
    return np.mean(concatenated_distributions, axis=1)


class Calculator_Regional_Lambdas_Intervals(Bootstrap_from_time_series):
    def __init__(self, regional_lambdas):
        self.lambdas = regional_lambdas
        self.p_values = self.get_p_values()
        self.intervals = self.intervals_from_p_values_and_alpha()
        self.interval_lambdas = [interval for interval in self.intervals]
        self.lambda_latex_interval = self.get_lambda_interval_latex_string()

    def intervals_from_p_values_and_alpha(self):
        intervals = calculate_intervals_from_p_values_and_alpha(self.lambdas, self.p_values, 0.05)
        return intervals

    def get_intermediate_lambdas(self):
        return [
            lambdas
            for lambdas in self.lambdas
            if (lambdas > self.intervals[0]) and (lambdas < self.intervals[2])
        ]
