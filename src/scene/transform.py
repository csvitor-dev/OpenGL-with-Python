import pyrr


class Transform:
    def __init__(self):
        self.translation = pyrr.Vector3([0, 0, 0])
        self.rotation = 0
        self.scale = pyrr.Vector3([1, 1, 1])

    def matrix(self):
        T = pyrr.matrix44.create_from_translation(self.translation)
        R = pyrr.matrix44.create_from_z_rotation(self.rotation)
        S = pyrr.matrix44.create_from_scale(self.scale)

        return pyrr.matrix44.multiply(S, pyrr.matrix44.multiply(T, R))
