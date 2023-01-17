import numpy as np
import pygame


class GridDrawer:
    color_mapping = {
        1.0: (255, 255, 255),
        0.0: (0, 0, 0),
        0.2: (24, 24, 24),
        0.4: (48, 48, 48),
        0.6: (72, 72, 72),
        0.8: (96, 96, 96),
    }

    def __init__(self, grid: np.ndarray, feature_range: int) -> None:
        self.grid = grid
        self.color_step = 1 / feature_range

    def get_similarity(self, culture: np.ndarray, neighbor: np.ndarray) -> float:
        """
        Gets the similarity of the culture at the given index to the culture at the given neighbor.
        """
        similarity = np.sum(culture == neighbor) / self.grid.shape[2]
        return similarity

    def draw_square(self, screen: pygame.Surface, x: int, y: int) -> None:
        """
        Draws a square on the PyGame window.
        The square is colored according to the similarity of the culture at the given index to its neighbors.
        """
        culture = self.grid[x, y]
        # Order: Top, right, bottom and left
        if y - 1 >= 0 and x - 1 >= 0:
            neighbor = self.grid[x, y - 1]
            similarity = self.get_similarity(culture, neighbor)
            color = (
                self.color_mapping[similarity]
                if similarity in self.color_mapping
                else (int(similarity * 255), int(similarity * 255), int(similarity * 255))
            )
            start_pos, end_pos = (x * 16, y * 16), (x * 16 + 16, y * 16)
            pygame.draw.line(screen, color, start_pos, end_pos, width=2)

        if x + 1 < self.grid.shape[0] and y - 1 >= 0:
            neighbor = self.grid[x + 1, y]
            similarity = self.get_similarity(culture, neighbor)
            color = (
                self.color_mapping[similarity]
                if similarity in self.color_mapping
                else (int(similarity * 255), int(similarity * 255), int(similarity * 255))
            )
            start_pos, end_pos = (x * 16 + 16, y * 16), (x * 16 + 16, y * 16 + 16)
            pygame.draw.line(screen, color, start_pos, end_pos, width=2)

        if y + 1 < self.grid.shape[1] and x + 1 < self.grid.shape[0]:
            neighbor = self.grid[x, y + 1]
            similarity = self.get_similarity(culture, neighbor)
            color = (
                self.color_mapping[similarity]
                if similarity in self.color_mapping
                else (int(similarity * 255), int(similarity * 255), int(similarity * 255))
            )
            start_pos, end_pos = (x * 16, y * 16 + 16), (x * 16 + 16, y * 16 + 16)
            pygame.draw.line(screen, color, start_pos, end_pos, width=2)

        if x - 1 >= 0 and y + 1 < self.grid.shape[1]:
            neighbor = self.grid[x - 1, y]
            similarity = self.get_similarity(culture, neighbor)
            color = (
                self.color_mapping[similarity]
                if similarity in self.color_mapping
                else (int(similarity * 255), int(similarity * 255), int(similarity * 255))
            )
            start_pos, end_pos = (x * 16, y * 16), (x * 16, y * 16 + 16)
            pygame.draw.line(screen, color, start_pos, end_pos, width=2)

    def draw(self) -> None:
        """
        Initializes a PyGame window and draws the grid with 16px squares.
        Each border wall is colored according to its similarity to the neighboring culture.
        """
        pygame.init()
        pygame.display.set_caption("Axelrod Model")
        screen = pygame.display.set_mode((self.grid.shape[0] * 16, self.grid.shape[1] * 16))
        screen.fill((255, 255, 255))

        for x in range(self.grid.shape[0]):
            for y in range(self.grid.shape[1]):
                self.draw_square(screen, x, y)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
