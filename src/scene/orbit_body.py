import pyrr


class OrbitBody:
    def __init__(self, distance: float, size: float, speed: float):
        self.distance = distance
        self.size = size
        self.speed = speed

        self.angle = 0

    def update(self, dt):
        self.angle += self.speed * dt

    def matrix(self):
        rotation = pyrr.matrix44.create_from_z_rotation(self.angle)

        translation = pyrr.matrix44.create_from_translation(
            [self.distance, 0, 0]
        )

        scale = pyrr.matrix44.create_from_scale([self.size, self.size, 1])

        m = pyrr.matrix44.multiply(scale, translation)
        m = pyrr.matrix44.multiply(m, rotation)

        projection = pyrr.matrix44.create_orthogonal_projection(
            -1, 1,
            -1, 1,
            -1, 1
        )

        return m, projection
