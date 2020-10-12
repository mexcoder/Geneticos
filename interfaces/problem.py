from abc import ABC, abstractmethod, abstractproperty
import random

class Problem(ABC):

    @abstractproperty
    def population(self):
        raise NotImplementedError

    @abstractproperty
    def populationSize(self):
        raise NotImplementedError
    
    @abstractmethod
    def getName(self):
        """ returns the name of the problem beeing solved """
        raise NotImplementedError

    @abstractmethod
    def generatePopulation(self):
        """ generates a random population """
        raise NotImplementedError

    @abstractmethod
    def crossover(self):
        """ returns a population to mutate """
        raise NotImplementedError  
    
    def tagPopulationFitness(self):
        return [(individual.getFitness(), individual) for individual in self.population]

    def selectPercentageFromPopulation(self, percent):
        number = percent * self.populationSize / 100
        return self.selectFromPopulation

    def selectFromPopulation(self, number):
        return random.choices(self.population, k=number)

    def iterate(self):
        """ runs an iteration consisting of a fitness tagging, a round of selections
            an the generation of a new population
        """
        raise NotImplementedError