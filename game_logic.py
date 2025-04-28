from game_object import GameObject
from pubsub import pub

from player_object import PlayerObject
from Object import Object

class GameLogic:
    def __init__(self):
        self.properties = {}
        self.game_objects = {}
        self.next_id = 0

    def tick(self):
        for id in self.game_objects:
            self.game_objects[id].tick()

    def create_object(self, position, kind, size):
        if kind == "player":
            obj = PlayerObject(position, kind, self.next_id, size)
        else:
            obj = Object(position, kind, self.next_id, size)

        self.next_id += 1
        self.game_objects[obj.id] = obj
        pub.sendMessage('create', game_object=obj)
        return obj

    def load_world(self):
        self.create_object([0, 10, 0], "player", (0.3, 0.3, 0.3))
        self.create_object([0, -9, 0], "object", (0.3, 0.3, 0.3))

    def get_property(self, key):
        if key in self.properties:
            return self.properties[key]

        return None

    def set_property(self, key, value):
        self.properties[key] = value

    def remove(self, game_object):
        pass