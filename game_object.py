class GameObject:
    def __init__(self, position, kind, id):
        self.position = position
        self.kind = kind
        self.id = id

    def tick(self):
        pass