from interfaces.problem import Problem
from interfaces.renderer import Renderer
from pointRenderer import PointRenderer
from interfaces.individual import Individual
import mutators
import reproductors

class Point(Problem):

    def __init__(self, populationSize=100, *args, renderer=None, order=6, **kwargs):
        # super(CLASS_NAME, self).__init__(*args, **kwargs)

        # validate Inputs
        if populationSize <= 0:
            raise ValueError("population size must be greather than one")

        if renderer is not None and not isinstance(renderer, Renderer):
            raise ValueError("renderer must be a subclass of interfaces.Renderer")
        if renderer is None:
            renderer = PointRenderer()

        # initialize values
        self._populationSize = populationSize
        self._renderer = renderer
        self._historicalTopIndividuals = []
        self.genomeSize = order + 1 

        # init population
        self.generatePopulation()
        

    @property
    def population(self):
        return self._population

    @property
    def populationSize(self):
        return self._populationSize

    @property
    def renderer(self):
        return self._renderer

    @property
    def historicalTopScore(self):
        return [individual.fitness for individual in self._historicalTopIndividuals]

    @property
    def historicalTopIndividuals(self):
        return self._historicalTopIndividuals

    def addTopIndividual(self, individual):
        self._historicalTopIndividuals.append(individual)

    def getName(self):
        return "single point Problem"

    def generatePopulation(self):
        self._population = [PointIndividual.generateIndividual(self.genomeSize, 0, 255) 
                            for i in range(self._populationSize)]
        return self._population

    def crossover(self):
        # generate a new population selecting the best of 5% of the population
        # selected randomly
        newPop = []
        for _ in range(int(self.populationSize/2)):
            # get 5% of the population at random
            selected = self.selectPercentageFromPopulation(5)
            # get the top individual by fitness of the selection
            top = min(selected, key=lambda i: i.fitness)
            runnerUp = min(selected[1:], key=lambda i: i.fitness)
            # insert the top individual to the new population
            newPop += list(top.reproduce(runnerUp))

        if self.enableElitism:
            # append the old population
            newPop += self.population
            # sort
            newPop.sort(key = lambda i: i.fitness)
            # get the top individuals
            newPop = newPop[:self.populationSize]

        # replace the old population with the new one
        self._population = newPop

class PointIndividual(Individual):

    target = None
    xValue = None
    geneWeight = None

    def __init__(self, *args, target=77.378125, xValue=1.5, geneWeight=25.5, **kwargs):
        super().__init__(*args, **kwargs)
        self.target = target
        self.xValue = xValue
        self.geneWeight = geneWeight
    

    def calcPoint(self, x=None):
        if x is None:
            x = self.xValue

        genes = self.genome
        res = [( ( genes[i]/self.geneWeight ) * (x ** i) ) 
                for i in range(0,len(self.genome))]
        return sum(res)

    @property
    def mutators(self):
        return [mutators.noopMutator]

    @property
    def reproductors(self):
        return [reproductors.MaskReproductor]

    def getFitness(self):
        value = self.calcPoint(self.xValue)
        return abs(self.target - value)

def test():
    import random
    # random.seed(42)
    t = Point()
    # print(t.population[0].genomeToCityList())
    # print(t.population[0].genomeToCityList()[0])
    # print(PointIndividual.cityList)
    t.run(wait=None)
    

if __name__ == '__main__':
    test()