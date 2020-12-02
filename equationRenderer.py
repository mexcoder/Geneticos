from pointRenderer import PointRenderer
from interfaces.individual import Individual

class EquationRender (PointRenderer):
    
    
    def __init__(self, *args, steps=1000, compressFactor=10, target=None, **kwargs):
        self.steps = steps
        self.compressFactor = compressFactor
        
        if target is not None and not isinstance(target, Individual):
            raise ValueError("renderer must be a subclass of interfaces.Renderer")

        self.target = target
        super().__init__(*args, **kwargs)

    def configurePopulationPlot(self, plt, *args, **kwargs):
        super().configurePopulationPlot(plt, *args, **kwargs)
        if(self.target is not None):
            self.doRenderIndividual(plt, self.target, "--", c="red")        
    
    def renderIndividual(self, individual):
        """[summary]

        :param individual: an individual to render
        :type individual: point.PointIndividual
        """ 
        plt = self.getPopulationPlot()
        plt.clear()
        self.configurePopulationPlot(plt)
        self.doRenderIndividual(plt, individual, "-")

    def doRenderIndividual(self, plt, individual, style, **kwargs):
        xArray = [x/self.compressFactor for x in range(self.steps)]
        points = [individual.calcPoint(x) for x in xArray]
        plt.plot(
                 xArray,
                 points,                 
                 style,
                 **kwargs
                )

    # """[summary]

    #     :param individual: an individual to render
    #     :type individual: traveler.TravelerIndividual
    #     """ 
    #     plt = self.getPopulationPlot()
    #     plt.clear()
    #     self.configurePopulationPlot(plt)
    #     plt.set_xlabel("Generation {}".format(self.frame))
    #     route = individual.genomeToCityList()
    #     plt.plot([city.x for city in route[1:-1]],
    #              [city.y for city in route[1:-1]],
    #              "bo",
    #              mec="black"
    #             )
    #     # signal the start with an other shape and color
    #     ax = plt.plot(route[0].x, route[0].y, "y*", markerSize=10, mec="black")
    #     vectors = [(route[cityIndex-1].x, route[cityIndex-1].y,
    #              route[cityIndex].x-route[cityIndex-1].x, route[cityIndex].y-route[cityIndex-1].y)
    #             for cityIndex in range(1,len(route))]

    #     X, Y, U, V = zip(*vectors)
    #     ax = plt
    #     ax.quiver(X, Y, U, V, 
    #               facecolor="forestgreen",
    #               angles='xy',
    #               scale_units='xy',
    #               scale=1,
    #               edgecolor="black",
    #               linewidth=0.5)

    #     # signal the end with an other shape and color
    #     ax = plt.plot(route[-1].x, route[-1].y, "rp", markerSize=7, mec="black")
    #     vectors = [(route[cityIndex-1].x, route[cityIndex-1].y,
    #              route[cityIndex].x-route[cityIndex-1].x, route[cityIndex].y-route[cityIndex-1].y)
    #             for cityIndex in range(1,len(route))]