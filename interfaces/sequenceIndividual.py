from .individual import Individual
import random

class SequenceIndividual(Individual):
    
    @classmethod
    def generateIndividual(cls, geneMin, geneMax):
        geneList = list(range(geneMin,geneMax))
        random.shuffle(geneList)
        return cls(geneList)