from abc import ABC, abstractmethod

class Data(ABC):

    @abstractmethod
    def getData(self):
        raise NotImplementedError