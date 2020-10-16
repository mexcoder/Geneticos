from abc import ABC, abstractmethod, abstractproperty
import random
import time

class Problem(ABC):

    @abstractproperty
    def population(self):
        raise NotImplementedError

    @abstractproperty
    def populationSize(self):
        raise NotImplementedError
    
    @abstractproperty
    def renderer(self):
        raise NotImplementedError

    @abstractproperty
    def historicalTopScore(self):
        raise NotImplementedError

    @abstractproperty
    def historicalTopIndividuals(self):
        raise NotImplementedError

    @abstractmethod
    def addTopIndividual(self, individual):
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
        """ generates a new population to mutate """
        raise NotImplementedError
    
    def mutate(self):
        for individual in self.population:
            individual.mutate()

    def selectPercentageFromPopulation(self, percent):
        number = int(percent * self.populationSize / 100)
        return self.selectFromPopulation(number)

    def selectFromPopulation(self, number):
        return random.choices(self.population, k=number)

    def iterate(self):
        """ runs an iteration consisting of a fitness tagging, a round of selections
            an the generation of a new population
        """

        # get the top individual and its score
        topIndividual = min(self.population, key=lambda i: i.fitness)
        
        # register the top score
        self.addTopIndividual(topIndividual)

        # render if needed
        if self.renderer is not None:
            self.renderer.renderIndividual(topIndividual)
            self.renderer.renderScore(self.historicalTopScore)
            self.renderer.draw()
        
        # do crossover and generate a new population
        self.crossover()

        # mutate the population
        self.mutate()

    def run(self, iterations=100, wait=None):
        for _ in range(iterations):
            self.iterate()
            if wait:
                time.sleep(wait)
