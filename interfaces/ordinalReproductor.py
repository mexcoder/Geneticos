from .reproductor import AbstractReproductor
from abc import abstractclassmethod

class abstractOrdinalReproductor(AbstractReproductor):

    @abstractclassmethod
    def reproduce(cls, parent):
        raise NotImplementedError