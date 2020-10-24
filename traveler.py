from interfaces.problem import Problem
from interfaces.renderer import Renderer
from cityRouteRenderer import CityRouteRenderer
from city import City
from interfaces.ordinalIndividual import OrdinalIndividual
import mutators
import ordinalReproductors as reproductors

class Traveler(Problem):

    def __init__(self, populationSize=100, *args, renderer=None, **kwargs):
        # super(CLASS_NAME, self).__init__(*args, **kwargs)

        # validate Inputs
        if populationSize <= 0:
            raise ValueError("population size must be greather than one")

        if renderer is not None and not isinstance(renderer, Renderer):
            raise ValueError("renderer must be a subclass of interfaces.Renderer")
        if renderer is None:
            renderer = CityRouteRenderer()

        # initialize values
        self._populationSize = populationSize
        self._renderer = renderer
        self._historicalTopIndividuals = []
        self.genomeSize = len(self.getData())

        # init population
        self.generatePopulation()
        TravelerIndividual.cityList = self.getData()
        

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
        return "Traveler Problem"

    def getData(self):
        return [
                City(x=1,  y=1),
                City(x=1,  y=7),
                City(x=2,  y=3),
                City(x=2,  y=5),
                City(x=3,  y=2),
                City(x=4,  y=4),
                City(x=5,  y=1),
                City(x=6,  y=6),
                City(x=7,  y=3),
                City(x=9,  y=8),
                City(x=10, y=5),
                City(x=12, y=3),
                City(x=13, y=1),
                City(x=13, y=6)
            ]

    def generatePopulation(self):
        self._population = [TravelerIndividual.generateIndividual(0, self.genomeSize) 
                            for i in range(self._populationSize)]
        return self._population

    def crossover(self):
        # generate a new population selecting the best of 5% of the population
        # selected randomly
        newPop = []
        for _ in range(self.populationSize):
            # get 5% of the population at random
            selected = self.selectPercentageFromPopulation(5)
            # get the top individual by fitness of the selection
            top = min(selected, key=lambda i: i.fitness)
            # insert the top individual to the new population
            newPop.append(top.reproduce(None))

        # replace the old population with the new one
        self._population = newPop

class TravelerIndividual(OrdinalIndividual):

    cityList = None

    @property
    def mutators(self):
        return [mutators.noopMutator]

    @property
    def reproductors(self):
        return [reproductors.geneInverseReprodcutor,
                #reproductors.noopReprodcutor,
                reproductors.geneSwapReprodcutor]

    def getFitness(self):
        fitness = 0
        for index in range(1, len(self.genome)):
            cityOrig = self.geneToCity(self.genome[index-1])
            cityDest = self.geneToCity(self.genome[index])
            fitness += cityOrig.distanceTo(cityDest)
        return fitness
    
    def geneToCity(self, cityIndex):
        return TravelerIndividual.cityList[cityIndex]

    def genomeToCityList(self):
        if TravelerIndividual.cityList is None:
            raise ValueError("City list has not been initialized")

        return [ self.geneToCity(gene) for gene in self.genome]

def test():
    import random
    # random.seed(42)
    t = Traveler()
    # print(t.population[0].genomeToCityList())
    # print(t.population[0].genomeToCityList()[0])
    # print(TravelerIndividual.cityList)
    t.run(wait=None)
    

if __name__ == '__main__':
    test()