import random
from abc import ABC, abstractmethod

class individual(ABC):

    @staticmethod
    def generateIndividual(genomeSize, geneMin, geneMax):
        return [random.randrange(geneMin, geneMax) for x in range(genomeSize)]
    
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
        raise NotImplementedError