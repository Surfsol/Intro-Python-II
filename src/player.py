# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
       # super().__init__(name, description)
    def goto(self, direction):
        if self.current_room.connections[direction] is not None:
            #change current room
            self.current_room = self.current_room.connections[direction]
        else:
            print("Wrong Move!")