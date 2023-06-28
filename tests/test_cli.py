from population_trend import (
    write_burrows_by_species_and_island,
)
import pandas as pd


data_path = "tests/data/dcco_laal_gumu_burrows_data.csv"
data = pd.read_csv(data_path)
species = "Laysan Albatross"
island = "Guadalupe"


def test_write_burrows_by_species_and_island():
    output_path = "tests/data/laal_guadalupe.csv"
    write_burrows_by_species_and_island(data_path, species, island, output_path)
    obtained_csv = pd.read_csv(output_path)
    obtained_columns = len(obtained_csv.columns)
    expected_columns = 12
    assert obtained_columns == expected_columns
