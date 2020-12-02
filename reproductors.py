from interfaces.reproductor import AbstractReproductor
import random
import math

class MaskReproductor(AbstractReproductor):

    @classmethod
    def reproduce(cls, individualX, individualY, *args, bitsPerGene=8):
        """

        :param AbstractReproductor: [description]
        :type AbstractReproductor: (individual.abstractIndividual, individual.abstractIndividual)
        """
        # ensure both individuals are of the same class and their genomes have the same length

        # TODO: move this validation to de individual class on a method called canBreed
        if  individualX.__class__ is not individualY.__class__:
            raise ValueError("both individuals are not of the same class")

        genomeX = individualX.genome
        genomeY = individualY.genome

        if not len(genomeX) == len(genomeY):
            raise ValueError("both individual dont have the same len")

        individualCls = individualX.__class__

        totalBits = len(genomeX) * bitsPerGene
        cutPoint = random.randint(1,totalBits)
        wholeGeneSplit = cutPoint % bitsPerGene == 0

        splitpoint = cutPoint/bitsPerGene
        splitpoint1 = int(math.floor(splitpoint))
        splitpoint2 = int(math.ceil(splitpoint))

        #print(splitpoint1, splitpoint2)

        # array splicing is not inclusive
        childGenomeX = genomeX[:splitpoint1] 
        childGenomeY = genomeY[:splitpoint1] 

        if not wholeGeneSplit:
            displacement = cutPoint - splitpoint1 * bitsPerGene
            maskX = (2 ** (cutPoint - splitpoint1 * bitsPerGene)) - 1
            maskY = (2 ** (splitpoint2 * bitsPerGene - cutPoint)) - 1

            # TODO: displace either x or y 
            maskY = maskY << displacement

            parentGeneX = genomeX[splitpoint1]
            parentGeneY = genomeY[splitpoint1]

            childGeneX = (parentGeneX & maskX) + (parentGeneY & maskY)
            childGeneY = (parentGeneY & maskX) + (parentGeneY & maskX)

            childGenomeX.append(childGeneX)
            childGenomeY.append(childGeneY)

        childGenomeX += genomeY[splitpoint2:]
        childGenomeY += genomeX[splitpoint2:]

        return  individualCls(childGenomeX), individualCls(childGenomeY)


def test():
    from interfaces.individual import Individual
    class tstIndiv(Individual):
        def getFitness(self):
            return 1
        def mutators(self):
            return []
        def reproductors(self):
            return[]


    x,y = MaskReproductor.reproduce(tstIndiv(list(range(10,20))),tstIndiv(list(range(20,30))))
    print(x.genome)
    print(y.genome)

if __name__ == '__main__':
    test()