from interfaces.problem import Problem
from interfaces.renderer import Renderer
from city import City
from individual import individual

class Traveler(Problem):


    def __init__(self, populationSize=100, *args, renderer=None, **kwargs):
        # super(CLASS_NAME, self).__init__(*args, **kwargs)

        # validate Inputs
        if populationSize <= 0:
            raise ValueError("population size must be greather than one")

        if renderer is not None and not isinstance(renderer, Renderer):
            raise ValueError("renderer must be a subclass of interfaces.Renderer")

        # initialize values
        self._populationSize = populationSize
        self.renderer = renderer
        self.genomeSize = len(self.getData())

        # init population
        self.generatePopulation()

    @property
    def population(self):
        return self._population

    @property
    def populationSize(self):
        return self._populationSize

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
        self._population = [individual.generateIndividual(self.genomeSize,
                                                         0,
                                                         self.genomeSize) 
                            for i in range(self._populationSize)]
        return self._population
