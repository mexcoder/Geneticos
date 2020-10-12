import random
import data
import pprint
import mutationOperations
from math import sqrt

random.seed(42) # to get consistent results on developmend


cityList = data.getData()


def distance(origin, dest):
    return sqrt( ( ( dest["x"] - origin["x"] ) ** 2 ) + ( ( dest["y"] - origin["y"]) ** 2 ))

def chromosome2cityList(chromosome, cities):
    cityList = []

    for gene in chromosome:
        # doing a touple rn, may change to another data type depending on math plot lib
        cityList.append((cities[gene]["x"], cities[gene]["y"]))

    return cityList

def generatePopulation(nGenes, populationSize, maxGeneValue): # max is not inclusive
    return [[random.randrange(0, maxGeneValue) for x in range(nGenes) ] for i in range(populationSize)]

def getCitiesFitness(individual, cities):
    fitnes = 0
    for index in range(1, len(individual)):
        cityOrigIndex = individual[index-1]
        cityDestIndex = individual[index]
        fitnes += distance(cities[cityOrigIndex], cities[cityDestIndex])

    return fitnes

def getFitness(individual):
    return getCitiesFitness(individual, cityList)

def selectFromPopulation(population, n):
    return random.choices(population, k=n)


def tagPopulation(pop, fn=getFitness):
    return [(fn(indv), indv) for indv in pop]

def orderTaggedPopulation(tPop):
    tPop.sort(key= lambda i : i[0])
    return tPop

def mutate(individual):
    operators = [mutationOperators.swap, mutationOperators.rotate]

    operator = random.choice(operators)
    
    return operator(individual)

population = generatePopulation(14, 100, 13)

pp = pprint.PrettyPrinter(indent=4)

# pp.pprint(population)

# print(len(cityList))
# print(len(population))
# print(len(population[1]))
# pp.pprint([chromosome2cityList(i, cityList) for i in population])
# pp.pprint([getFitness(i, cityList) for i in population])
pp.pprint(selectFromPopulation(tagPopulation(population),5))

# tag population
# select 5% of population and take the best
# mutate the best
# repeat until the childs are the same number as the parents
# do this 100 times