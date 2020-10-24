from interfaces.mutator import AbstractMutator

class noopMutator(AbstractMutator):

    @staticmethod
    def mutate(genome):
        return genome