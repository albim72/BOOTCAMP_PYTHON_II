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

#proces ewolucji

def main():
    random.seed(64)
    pop = toolbox.population(n=300)
    CXPB, MUTPB = 0.5,0.2
    print("start procesu ewolucji...")
    #ewaluacja wejściowe populacji
    fitnesses = list(map(toolbox.evalute,pop))
    for ind,fit in zip(pop,fitnesses):
        ind.fitness.values = fit
    
    print(f"przeprowadzono ewaluację {len(pop)} osobników")
    
    fits = [ind.fitness.values[0] for ind in pop]
    
    #numer generacji g
    g=0
    
    #Ewolucja
    while max(fits) < 100 and g < 1000:
        g = g+1
        print(f"---- Generacja {g} ------")
        offspring = toolbox.select(pop,len(pop))
        offspring = list(map(toolbox.clone,offspring))
        
        #zastosowanie krzyżowania i mutacji do modyfikacji nowej populacji
        for child1, child2 in zip(offspring[::2],offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1,child2)
                del child1.fitness.values
                del child2.fitness.values
                
        for mutant in offspring:
            if random.random < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values
                
                
        
