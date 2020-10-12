from abc import ABC, abstractclassmethod


class Renderer(ABC):
    
    @abstractclassmethod
    def renderIndividual(indv):
        raise NotImplementedError
    
    @abstractclassmethod
    def renderPopulation(pop):
        raise NotImplementedError

    @abstractclassmethod
    def renderResult(indv):
        raise NotImplementedError

