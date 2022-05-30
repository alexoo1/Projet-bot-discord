from abc import ABC, abstractmethod
from typing import Dict


class Handler(ABC):

    state: Dict = None

    @staticmethod
    @abstractmethod
    def setup():
        pass
