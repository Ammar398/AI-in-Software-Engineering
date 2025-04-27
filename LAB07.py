import operator
import math
import random
import numpy as np

from deap import algorithms, base, creator, gp, tools

# Step 1: Define the primitive set
pset = gp.PrimitiveSet("MAIN", 1)  # one input: X
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.sub, 2)
pset.addPrimitive(operator.mul, 2)

# To prevent division by zero, define safe division
def safeDiv(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1

pset.addPrimitive(safeDiv, 2)
pset.addEphemeralConstant("rand101", lambda: random.randint(-1, 1))
pset.renameArguments(ARG0='x')

# Step 2: Define the individual and fitness
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # minimize error
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

# Step 3: Register operators
toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=3)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("compile", gp.compile, pset=pset)

# Step 4: Define the evaluation function
def evalSymbReg(individual):
    func = toolbox.compile(expr=individual)
    # Define dataset
    x_vals = np.linspace(-1, 1, 20)
    y_true = 5*x_vals**3 - 6*x_vals**2 + 8*x_vals - 1
    y_pred = np.array([func(x) for x in x_vals])
    mse = ((y_true - y_pred)**2).mean()
    rmse = math.sqrt(mse)
    return (rmse,)

toolbox.register("evaluate", evalSymbReg)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

# Step 5: Evolve the population
def main():
    random.seed(42)
    population = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    
    print("Evolution process starts")
    algorithms.eaSimple(population, toolbox, 0.5, 0.2, 40, stats=stats, halloffame=hof, verbose=True)
    
    print("\nBest individual:")
    print(hof[0])
    func = toolbox.compile(expr=hof[0])
    
    # Evaluate on test data
    x_vals = np.linspace(-1, 1, 20)
    y_true = 5*x_vals**3 - 6*x_vals**2 + 8*x_vals - 1
    y_pred = np.array([func(x) for x in x_vals])
    
    print("\nTest RMSE:", math.sqrt(((y_true - y_pred)**2).mean()))

if __name__ == "__main__":
    main()
