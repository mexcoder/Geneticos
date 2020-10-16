import random
from abc import ABC, abstractmethod, abstractproperty
try:
    from functools import cached_property # introduced on python 3.8
except ImportError:
    from backports.cached_property import cached_property

class Individual(ABC):

    @abstractproperty
    def mutators(self):
        raise NotImplementedError

    @classmethod
    def generateIndividual(cls, genomeSize, geneMin, geneMax):
        return cls([random.randrange(geneMin, geneMax) for x in range(genomeSize)])
    
    def __init__(self, genome=[]):
        self.genome = genome    

    def __getitem__(self, item):
        return self.getGene(item)

    def getGene(self, geneIndex):
        return self.genome[geneIndex]

    def __getRandomMutator(self):
        return random.choice(self.mutators)

    def __repr__(self):
        return "<{} fitnes:{:.2f}>".format(self.__class__.__name__, self.fitness)

    @cached_property
    def fitness(self):
        return self.getFitness()
        # if not "__cached_fitness_property" in self:
        #     self.__cached_fitness_property = self.getFitness()
        # return self.__cached_fitness_property

    @abstractmethod
    def getFitness(self):
        raise NotImplementedError

    def mutate(self):
        mutator = self.__getRandomMutator()
        self.genome = mutator.mutate(self.genome)

    def clone(self):
        return self.__class__(self.genome)
