from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional

from actions import Action, all_actions

if TYPE_CHECKING:
    from game import Game

@dataclass
class Room:

    id: int
    description: str
    directions: dict[str, Optional[int]]
    actions: list[Optional[str]] = field(default_factory=list)
    commands: list[Action] = field(default_factory=list)

    def __post_init__ (self):
        self.assign_actions()
    
    def assign_actions(self):
        for action in self.actions:
            if action not in all_actions:
                raise NotImplementedError
            self.commands.append(all_actions[action]())

    def check_commands(self, command: str):
        for action in self.commands:
            if action.check_command(command):
                return True
        return False
    
    def do_command(self, game: 'Game', command: str):
        for action in self.commands:
            if action.check_command(command):
                action.do_action(game)
                break

    def print(self):
        available_directions = [k for k, v in self.directions.items() if v is not None]

        print(self.description)
        print('Available directions: ' + ', '.join(available_directions))