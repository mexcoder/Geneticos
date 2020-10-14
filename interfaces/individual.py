import random
from abc import ABC, abstractmethod

class Individual(ABC):

    @classmethod
    def generateIndividual(cls, genomeSize, geneMin, geneMax):
        return cls([random.randrange(geneMin, geneMax) for x in range(genomeSize)])
    
    def __init__(self, genome=[]):
        self.genome = genome    

    def __getitem__(self, item):
        return self.getGene(item)

    def getGene(self, geneIndex):
        return self.genome[geneIndex]

    @abstractmethod
    def getFitness(self):
        raise NotImplementedError

    def mutate(self):
        random.shuffle(self.genome) # just an example
