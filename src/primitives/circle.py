import numpy as np
import math


def create_circle(radius=1.0, segments=64):
    vertices = [0.0, 0.0, 0.0]

    for i in range(segments + 1):

        angle = 2 * math.pi * i / segments

        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        vertices += [x, y, 0.0]

    return np.array(vertices, dtype=np.float32)
