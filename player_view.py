from pubsub import pub

from view_object import ViewObject


class PlayerView:
    def __init__(self, game_logic):
        self.game_logic = game_logic
        self.view_objects = {}

        pub.subscribe(self.new_game_object, 'create')
        pub.subscribe(self.new_remove_object, 'remove')


    def new_remove_object(self, game_object):
        print("hello")
        for remove_object in self.view_objects:
            if self.view_objects[remove_object].game_object == game_object:
                self.view_objects[remove_object].delete()
                del self.view_objects[remove_object]
                break

    def new_game_object(self, game_object):
        view_object = ViewObject(game_object)
        self.view_objects[game_object.id] = view_object

    def tick(self):
        for key in self.view_objects:
            self.view_objects[key].tick()

