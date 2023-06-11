from dataclasses import dataclass
from typing import Optional

@dataclass
class Room:

    id: int
    description: str
    directions: dict[str, Optional[int]]

    def print(self):
        available_directions = [k for k, v in self.directions.items() if v is not None]

        print(self.description)
        print('Available directions: ' + ', '.join(available_directions))