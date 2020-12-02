from interfaces.matplotlibRenderer import MatplotlibRenderer

class PointRenderer (MatplotlibRenderer):

    generation = 1

    def setGrid(self, plt):
        plt.grid(color='gray', linestyle='--', linewidth=1)

    
    def configurePopulationPlot(self, plt):
        self.setGrid(plt)
        plt.set_title("Best individual Value")
        
    def configureScorePlot(self, plt, best = None, current = None):
        self.setGrid(plt)
        plt.set_title("Best individual score across generations")
        if best is None:
            plt.set_ylabel("Score")
        else:
            plt.set_ylabel("Score - Current {1:.2f} - Best {0:.2f}".format(best, current))
        
        plt.set_xlabel("Generation")
        plt.can_pan()
        plt.can_zoom()

    def renderIndividual(self, individual):
        """[summary]

        :param individual: an individual to render
        :type individual: point.PointIndividual
        """ 
        plt = self.getPopulationPlot()
        # plt.clear()
        # self.configurePopulationPlot(plt)
        plt.set_xlabel("Generation {}".format(self.frame))
        plt.axline((-2, 77.37), (self.frame + 2, 77.37))
        point = individual.calcPoint(1.5)
        plt.plot([self.frame ],
                 [point],
                 "o",
                 mec="black"
                )
        
    def renderScore(self, problemScore):
        plt = self.getScorePlot()
        plt.clear()
        self.configureScorePlot(plt, min(problemScore), problemScore[-1])
        plt.plot(problemScore, marker='o')

    def renderPopulation(self, pop):
        pass