from abc import ABC, abstractclassmethod

class AbstractReproductor(ABC):
    
    @abstractclassmethod
    def reproduce(cls, *args, **kwargs):
        raise NotImplementedError
