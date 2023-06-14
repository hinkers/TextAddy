import json
from typing import Any


class Flags:

    _flags: dict[str, Any]

    def __init__(self):
        with open('flags.json', 'r') as file:
            self._flags = json.load(file)
    
    def exists(self, name: str) -> bool:
        return name in self._flags

    def get(self, name: str) -> Any:
        return self._flags[name]
    
    def set(self, name: str, value: Any):
        self._flags[name] = value
    
    def toggle(self, name: str):
        self._flags[name] = not self._flags[name]