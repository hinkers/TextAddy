from flags import Flags
from player import Player
from room import Room


class Game:

    rooms: list[Room]
    current_room: Room
    complete: bool = False

    def __init__(self, rooms):
        self.rooms = rooms
        self.current_room = rooms[0]
        self.player = Player()
        self.flags = Flags()

    def get_room_by_id(self, id):
        room = [r for r in self.rooms if r.id == id]
        if len(room) == 1:
            return room[0]
        return None

    def start(self):
        self.current_room.print()
        while not self.complete:
            self.process_command(input('What do> '))

    def process_command(self, command):
        command = command.lower().strip()
        if command in ['north', 'south', 'east', 'west']:
            direction = self.current_room.directions[command]
            if direction is not None:
                self.current_room = self.get_room_by_id(direction)
                self.current_room.print()
            else:
                print('You cannot go this way.')
            return
        elif command == 'quit':
            print('Goodbye.')
            self.complete = True
            return
        elif command == 'room':
            self.current_room.print()
            return
        elif self.current_room.check_commands(command):
            self.current_room.do_command(self, command)
            return
        print(f'I do not know how to "{command}".')

