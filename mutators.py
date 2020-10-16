from interfaces.mutator import AbstractMutator
from collections import deque
import random

class noMutationMutator (AbstractMutator):

    @staticmethod
    def mutate(genome):
        return genome

class geneSwapMutator (AbstractMutator):
    
    @staticmethod
    def mutate(genome):
        genomeLen = len(genome)
        # select the longitude of the genes to swap, this may be up to 50% of
        # the genome ignoring the first and last elements
        swapLen = random.randint(1,int(genomeLen/2) - 1)
        # select the start point, this must be before the middle point
        # of the genome.
        # substracting the swap length ensures there is no overlaps
        swapOrigin = random.randint(1, int(genomeLen/2) - swapLen ) 
        # the destiny must be after the halfway point to ensure no overlaps
        # and we need to substract swaplen to avoid going over the end of the
        # genome
        swapDestiny  = random.randint(int(genomeLen/2), genomeLen-swapLen)

        begining = genome[:swapOrigin]
        originPartition = genome[swapOrigin:swapOrigin+swapLen]
        middle = genome[swapOrigin+swapLen:swapDestiny]
        destinyPartition = genome[swapDestiny:swapDestiny+swapLen]
        ending = genome[swapDestiny+swapLen:]

        return begining + destinyPartition + middle + originPartition + ending


class geneRotateMutator (AbstractMutator):

    @staticmethod
    def mutate(genome):
        genomeLen = len(genome)
        displacementLen = random.randint(2, int(genomeLen/2) - 1)
        displacementOrigin = random.randint(1, genomeLen-displacementLen-1)
        displacementEnd = displacementOrigin + displacementLen
        displacementMagnitude = random.randint(1, displacementLen)
        

        # use a deque to rotate
        partition = deque(genome[displacementOrigin : displacementEnd])
        partition.rotate(displacementMagnitude)

        # regenerate the list
        newGenome = list(genome[:displacementOrigin])
        newGenome += list(partition)
        newGenome += list(genome[displacementEnd:])

        return newGenome

class geneInverseMutator (AbstractMutator):

    @staticmethod
    def mutate(genome):
        genomeLen = len(genome)
        displacementLen = random.randint(2, int(genomeLen/2) - 1)
        displacementOrigin = random.randint(1, genomeLen-displacementLen-1)
        displacementEnd = displacementOrigin + displacementLen

        partition = genome[displacementOrigin : displacementEnd]
        # reverse the partition
        partition.reverse()

        # regenerate the list
        newGenome = list(genome[:displacementOrigin])
        newGenome += list(partition)
        newGenome += list(genome[displacementEnd:])

        return newGenome

def main():
    print(geneSwapMutator.mutate(list(range(10))))

if __name__ == '__main__':
    main()