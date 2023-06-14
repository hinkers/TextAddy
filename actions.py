from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game


class Action:
    command: str

    def check_command(self, command: str):
        if command == self.command:
            return True
        return False

    def do_action(self, game: 'Game'):
        raise NotImplementedError


class Interact(Action):
    
    def __init__(self, *args, **kwargs):
        self.command = f'interact {self.command}'


class InteractStatue(Interact):
    command: str = 'statue'

    def do_action(self, game: 'Game'):
        game.flags.toggle('statue_activated')
        print('Interacted with statue')


class InteractFountain(Interact):
    command: str = 'fountain'

    def do_action(self, game: 'Game'):
        if game.flags.get('statue_activated'):
            print('You did it!')
            game.complete = True
            return
        print('Nothing interesting happens')
        


all_actions: dict[str, Action] = {
    'interact_statue': InteractStatue,
    'interact_fountain': InteractFountain
}