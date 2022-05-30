from abc import ABC, abstractmethod
from typing import Dict


class Command(ABC):
    state: Dict = {}

    @staticmethod
    @abstractmethod
    def setup():
        pass
