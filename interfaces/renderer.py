from abc import ABC, abstractmethod


class Renderer(ABC):
    
    @abstractmethod
    def renderIndividual(self, indv):
        raise NotImplementedError
    
    @abstractmethod
    def renderPopulation(self, pop):
        raise NotImplementedError

    @abstractmethod
    def renderScore(self, indv):
        raise NotImplementedError

