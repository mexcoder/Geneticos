from abc import ABC, abstractstaticmethod

class AbstractMutator(ABC):

    @abstractstaticmethod
    def mutate(genome):
        raise NotImplementedError