from point import PointIndividual
from point import Point
from equationRenderer import EquationRender
from math import sin, cos, radians, fabs, fsum, inf
import mutators
import click 

class Equation (Point):
    
    
    def __init__(self,
                 populationSize=100,
                 *args,
                 renderer=None,
                 order=6,
                 steps=1000,
                 mutationPercentage=0,
                 enableElitism=False,
                 **kwargs):

        self._enableElitism = enableElitism
        self._mutationPercentage = mutationPercentage
        EquationIndividual.setTarget(self.getData(), steps=steps)

        if renderer is None:
            renderer = EquationRender(steps=steps, target=EquationIndividual(EquationIndividual.targetGenome))


        super().__init__(populationSize, *args, renderer=renderer, order=order, **kwargs)

    @property
    def mutationPercentage(self):
        return self._mutationPercentage

    @property
    def enableElitism(self):
        return self._enableElitism

    def getData(self):
        return [8, 25, 4, 45, 10, 17, 35]

    def generatePopulation(self):
        self._population = [EquationIndividual.generateIndividual(self.genomeSize, 0, 255) 
                            for i in range(self._populationSize)]
        return self._population
    

class EquationIndividual(PointIndividual):

    @classmethod
    def setTarget(cls, target, geneWeight=5, steps = 1000):
        cls.targetGenome = [gene * geneWeight for gene in target]
        cls.steps = steps

        tmpIndividual = cls(cls.targetGenome)
        cls.target = [tmpIndividual.calcPoint(x) for x in range(steps)]

    
    targetGenome = []
    target = []
    steps = 1000
    geneWeight = 5
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        steps = EquationIndividual.steps
        self.xValue = range(steps)
        self.geneWeight = EquationIndividual.geneWeight


    def getFitness(self):
        values = [self.calcPoint(x) for x in self.xValue]
        target = EquationIndividual.target
        errors = [fabs(target[g] - values[g]) for g in self.xValue]
        return fsum(errors)

    # def getFitness(self):
    #     values = self.genome
    #     target = EquationIndividual.targetGenome
    #     genomeLen = len(values)
    #     errors = [fabs(target[g] - values[g]) for g in range(genomeLen)]
    #     return fsum(errors)

    @property
    def mutators(self):
        return [
            #mutators.noopMutator
            mutators.percentageMutator
            ]

    def calcPoint(self, x):
        a, b, c, d, e, f, g = [gene / self.geneWeight for gene in self.genome]
        if c == 0 or e == 0:
            return inf
        return  a * (b * sin(x/c) + (d * cos(x/e))) + f * x - g

@click.command()
@click.option('--mutation', default=0, help='percentage of the population to mutate')
@click.option('--elitism/--no-elitism', is_flag=True, flag_value=True, help='enable the elitism')
@click.option('--seedFile', default=None, help='the seed satateFile to use for the prng')
def test(mutation, elitism, seedfile):
    import random
    import sys
    import pickle

    if seedfile is None:
        seed = random.randrange(sys.maxsize)
        # save to file
        with open("seed/{}.seed".format(seed), 'wb') as sf:
            pickle.dump(random.getstate(), sf)
        
    else:
        # load from file
        if ".seed" not in seedfile:
            seed = seedfile
            seedfile += ".seed"

        else:
            seed = seedfile.split(".")[0]

        with open("seed/{}".format(seedfile), 'rb') as sf:
            state = pickle.load(sf)
            random.setstate(state)



    print("{} will be used as seed for the rng".format(seed))

    t = Equation(mutationPercentage=mutation, enableElitism=elitism)
    # print(t.population[0].genomeToCityList())
    # print(t.population[0].genomeToCityList()[0])
    # print(PointIndividual.cityList)
    t.run(wait=None, iterations=150)
    

if __name__ == '__main__':
    test()