from .renderer import Renderer
import matplotlib.pyplot as plt
from abc import abstractmethod

class MatplotlibRenderer(Renderer):

    def __init__(self, *args, **kwargs):
        self.configurePopulationPlot(self.getPopulationPlot())
        self.configureScorePlot(self.getScorePlot())
        mng = plt.get_current_fig_manager()

        try:
            mng.window.state('zoomed') #works fine on Windows!
        except:
            mng.window.wm_attributes('-zoomed', 1) #works fine on Linux!
        plt.ion() # activate interactive mode
        plt.show() # open the window without blocking

        self.frame = 0
    
    def __del__(self):
        plt.ioff() # disable interactive mode
        plt.show() # block the program from exiting until the window is closed
       

    @abstractmethod
    def configurePopulationPlot(self, plt):
        raise NotImplementedError

    @abstractmethod
    def configureScorePlot(self, plt):
        raise NotImplementedError

    def getPopulationPlot(self):
        return plt.subplot(121, label="population")

    def getScorePlot(self):
        return plt.subplot(122, label="score")

    def draw(self):
        plt.draw()
        plt.pause(.001)
        plt.savefig("render/{}.png".format(self.frame), format="png")
        self.frame += 1