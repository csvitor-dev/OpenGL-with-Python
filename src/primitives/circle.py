import numpy as np
import numpy.typing as npt
import math


class Circle:
    def __init__(self, radius: float = 1.0, segments: int = 64) -> None:
        self.vertices = self.__make_circle_vertices(radius, segments)

    def __make_circle_vertices(self, radius: float, segments: int):
        vertices = [0.0, 0.0, 0.0]

        for i in range(segments + 1):
            angle = 2 * math.pi * i / segments
            x, y = radius * math.cos(angle), radius * math.sin(angle)

            vertices += [x, y, 0.0]
        return np.array(vertices, dtype=np.float32)
