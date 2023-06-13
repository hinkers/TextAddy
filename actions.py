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
        print('Interacted with statue')


all_actions: dict[str, Action] = {
    'interact_statue': InteractStatue
}