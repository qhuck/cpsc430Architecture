from game_object import GameObject
from pubsub import pub

from player_object import PlayerObject


class GameLogic:
    def __init__(self):
        self.properties = {}
        self.game_objects = {}
        self.next_id = 0

    def tick(self):
        for id in self.game_objects:
            self.game_objects[id].tick()

    def create_object(self, position, kind):
        if kind == "player":
            obj = PlayerObject(position, kind, self.next_id)
        else:
            obj = GameObject(position, kind, self.next_id)

        self.next_id += 1
        self.game_objects[obj.id] = obj

        pub.sendMessage('create', game_object=obj)
        return obj

    def load_world(self):
        self.create_object([0, 0, 0], "crate")
        self.create_object([-3, 0, 0], "crate")
        self.create_object([3, 0, 0], "crate")
        self.create_object([0, -10, 0], "player")

    def get_property(self, key):
        if key in self.properties:
            return self.properties[key]

        return None

    def set_property(self, key, value):
        self.properties[key] = value
