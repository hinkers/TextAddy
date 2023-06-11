import json
from game import Game
from room import Room


def main():
    with open("rooms.json") as file:
        rooms_data = json.load(file)

    rooms = [Room(**data) for data in rooms_data]

    game = Game(rooms)

    game.start()




if __name__ == '__main__':
    main()