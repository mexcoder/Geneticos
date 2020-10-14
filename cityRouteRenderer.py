from interfaces.matplotlibRenderer import MatplotlibRenderer

class CityRouteRenderer (MatplotlibRenderer):

    def setGrid(self, plt):
        plt.grid(color='gray', linestyle='--', linewidth=1)

    
    def configurePopulationPlot(self, plt):

        plt.set_title("Best individual route")
        
    def configureScorePlot(self, plt):
        plt.set_title("Best individual score across generations")
        plt.set_ylabel("Score")
        plt.set_xlabel("Generation")
        plt.can_pan()
        plt.can_zoom()

    def renderIndividual(self, individual):
        """[summary]

        :param individual: an individual to render
        :type individual: traveler.TravelerIndividual
        """ 
        plt = self.getPopulationPlot()
        plt.clear()
        self.setGrid(plt)
        route = individual.genomeToCityList()
        plt.plot([city.x for city in route[1:-1]],
                 [city.y for city in route[1:-1]],
                 "bo",
                 mec="black"
                )
        # signal the start with an other shape and color
        ax = plt.plot(route[0].x, route[0].y, "y*", markerSize=10, mec="black")
        vectors = [(route[cityIndex-1].x, route[cityIndex-1].y,
                 route[cityIndex].x-route[cityIndex-1].x, route[cityIndex].y-route[cityIndex-1].y)
                for cityIndex in range(1,len(route))]

        X, Y, U, V = zip(*vectors)
        ax = plt
        ax.quiver(X, Y, U, V, 
                  facecolor="forestgreen",
                  angles='xy',
                  scale_units='xy',
                  scale=1,
                  edgecolor="black",
                  linewidth=0.5)

        # signal the end with an other shape and color
        ax = plt.plot(route[-1].x, route[-1].y, "rp", markerSize=7, mec="black")
        vectors = [(route[cityIndex-1].x, route[cityIndex-1].y,
                 route[cityIndex].x-route[cityIndex-1].x, route[cityIndex].y-route[cityIndex-1].y)
                for cityIndex in range(1,len(route))]

        
    def renderScore(self, problemScore):
        print(len(problemScore), problemScore[-1])
        plt = self.getScorePlot()
        plt.clear()
        self.setGrid(plt)
        plt.plot(problemScore, marker='o')

    def renderPopulation(self, pop):
        pass