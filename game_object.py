class GameObject:
    def __init__(self, position, kind, id):
        self.position = position
        self.kind = kind
        self.id = id
        self.x_rotation = 0
        self.y_rotation = 0
        self.z_rotation = 0

    def tick(self):
        pass