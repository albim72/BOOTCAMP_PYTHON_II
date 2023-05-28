import random

from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax",base.Fitness,weights=(1.0,))
creator.create("Individual",list,fitness=creator.FitnessMax)

toolbox = base.Toolbox()

#generator atrybutów
toolbox.register("attr_bool",random.randint,0,1)
#struktura osobnika
toolbox.register("individual",tools.initRepeat,creator.Individual,toolbox.attr_bool,100)
#definicja populacji
toolbox.register("population",tools.initRepeat,list,toolbox.individual)

#funkcja celu
def evalOneMax(individual):
    return sum(individual)

#funckja ewaluacji
toolbox.register("evaluate",evalOneMax)

#operator krzyżowania
toolbox.register("mate",tools.cxTwoPoint)

#operator mutacji
toolbox.register("mutate",tools.mutFlipBit,indpb = 0.05)

#operator selekcji
toolbox.register("select",tools.selTournament,tournsize=3)
