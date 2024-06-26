from population_trend.population_growth_model import Plotter_Population_Trend_Model

import matplotlib.pyplot as plt


class Plotter_Population_Trend_Model_From_CPUE(Plotter_Population_Trend_Model):
    def set_labels(self):
        plt.ylabel("CPUE", size=20)
        plt.xlabel("Seasons", size=20)

    def plot_data(self):
        plt.plot(
            self.plot_seasons,
            self.data[self.interest_variable],
            "-Dk",
            label="Maximum CPUE",
        )
