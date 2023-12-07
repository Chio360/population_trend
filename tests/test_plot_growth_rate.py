from population_trend import Plotter_Growth_Rate
import matplotlib as plt
import numpy as np


def test_plotter_growth_rate():
    lambdas_dict = {"intervals": [1, 2, 3.5]}
    lambdas_dict_2 = {"intervals": [1.9, 3, 7.5]}
    plotter = Plotter_Growth_Rate(lambdas_dict, lambdas_dict_2)
    obtained = plotter.plot_error_bars()

    x_positions = plotter.error_bar_container.lines[0].get_data()[0]
    y_positions = plotter.error_bar_container.lines[0].get_data()[1]
    np.testing.assert_array_equal(x_positions, [1, 2])
    np.testing.assert_array_equal(y_positions, [2, 3])
    obtained_segments = plotter.error_bar_container.lines[2][0].properties()["segments"]
    assert obtained_segments[0][0][1] == lambdas_dict["intervals"][0]
    assert obtained_segments[0][1][1] == lambdas_dict["intervals"][2]
    assert obtained_segments[1][0][1] == lambdas_dict_2["intervals"][0]
    assert obtained_segments[1][1][1] == lambdas_dict_2["intervals"][2]
    assert isinstance(obtained, plt.axes._axes.Axes)
    obtained_y_label = obtained.get_ylabel()
    expected_y_label = "Growth Rate"
    assert obtained_y_label == expected_y_label
    assert obtained.get_xticklabels()[0].get_text() == "California"
    assert obtained.get_xticklabels()[1].get_text() == "Pacific"
    assert obtained.get_xticklabels()[1].get_fontsize() == 20.0

    obtained_xlim = plt.pyplot.xlim()
    expected_xlim = (0.5, 2.5)
    assert obtained_xlim == expected_xlim
