from direct.showbase.ShowBaseGlobal import globalClock

from game_object import GameObject
import random

class Object(GameObject):
    def __init__(self, position, kind, id, size):
        super().__init__(position, kind, id, size)
        self.old_position = position
        self.speed = 0.1

    def tick(self):
        dt = globalClock.getDt()
        current = self.position
        self.position = (current[0], current[1] - 10 * dt, current[2])
        if self.position[1] < 5:
            self.reset_obstacle()

    def reset_obstacle(self):
        x = random.uniform(-5, 5)
        z = random.uniform(-3, 3)
        self.position = (x, 25, z)