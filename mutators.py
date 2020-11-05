from interfaces.mutator import AbstractMutator
import random

class noopMutator(AbstractMutator):

    @staticmethod
    def mutate(genome):
        return genome

class percentageMutator(AbstractMutator):
    @staticmethod
    def mutate(genome, bitsPerGene=8):
        gene = random.randint(0, len(genome)-1)
        allele = random.randint(0,bitsPerGene)
        selected = genome[gene]
        mask = 1 << allele
        selected ^= mask # xor wil flip the selected bit an leave the other ones alone
        genome[gene]  = selected
        return genome