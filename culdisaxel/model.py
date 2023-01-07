from typing import Optional

import numpy as np

from culdisaxel.draw import GridDrawer
from culdisaxel.helpers import get_grid_neighbors


class AxelrodModel:
    # Grid of size n x n
    n: int

    # Number of culture features
    features: int

    # Range of the culture features
    feature_range: int

    # Number of cycles
    cycles: int

    # List of cycle numbers at which the model should be shown
    print_at_cycles: list

    # Grid of cultures
    _grid: Optional[np.ndarray]

    def __init__(
        self, n: int = 10, features: int = 5, feature_range: int = 10, cycles: int = 100000, print_at_cycles: list = []
    ) -> None:
        self._grid = None

        self.n = n
        self.features = features
        self.feature_range = feature_range
        self.cycles = cycles
        self.print_at_cycles = print_at_cycles

    def initialize_grid(self) -> np.ndarray:
        return np.random.randint(self.feature_range, size=(self.n, self.n, self.features))

    def get_random_culture(self) -> tuple[int, int]:
        return tuple(np.random.randint(self.n, size=2))

    def check_if_sites_interact(self, site1: tuple[int, int], site2: tuple[int, int]) -> bool:
        """
        Checks if the two sites interact with each other by checking the similarity of their features.
        """
        culture1 = self._grid[site1]
        culture2 = self._grid[site2]

        similarity = np.sum(culture1 == culture2) / self.features
        return np.random.random() <= similarity

    def change_feature(self, site1: tuple[int, int], site2: tuple[int, int]) -> None:
        """
        Changes a random feature of the culture at site1
        to the value of the corresponding feature of the culture at site2.
        """
        culture1 = self._grid[site1]
        culture2 = self._grid[site2]

        if np.array_equal(culture1, culture2):
            # All features are the same, no need to change anything
            return

        feature = np.random.randint(self.features)
        while culture1[feature] == culture2[feature]:
            feature = np.random.randint(self.features)

        # print(
        #     "Replacing feature",
        #     culture1[feature],
        #     "at culture",
        #     culture1,
        #     "with value",
        #     culture2[feature],
        #     "from culture",
        #     culture2,
        # )
        culture1[feature] = culture2[feature]

    def simulate(self) -> None:
        self._grid = self.initialize_grid()

        for i in range(self.cycles):
            if i in self.print_at_cycles:
                GridDrawer(self._grid, self.feature_range).draw()

            active_site = self.get_random_culture()
            neighbors = get_grid_neighbors(self.n, active_site)
            for neighbor in neighbors:
                if self.check_if_sites_interact(active_site, neighbor):
                    self.change_feature(active_site, neighbor)

        GridDrawer(self._grid, self.feature_range).draw()
