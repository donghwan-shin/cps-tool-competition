import deap.algorithms
import numpy as np
import math
import logging as log
from random import randint
import matplotlib.pyplot as plt

from code_pipeline.tests_generation import RoadTestFactory


class GATestGenerator():
    """
        Generates a set of tests using GA (based on the Deap library; https://github.com/deap/deap).

    """

    def __init__(self, executor=None, map_size=None):
        self.executor = executor
        self.map_size = map_size

    def create_the_test(self, road_points):
        # Create a vertical segment starting close to the left edge of the map
        x = 10.0
        y = 10.0
        length = 100.0
        interpolation_points = int(length / 10.0)
        for y in np.linspace(y, y + length, num=interpolation_points):
            road_points.append((x, y))

        # Create the 90-deg right turn
        radius = 20.0

        center_x = x + radius
        center_y = y

        interpolation_points = 5
        angles_in_deg = np.linspace(-60.0, 0.0, num=interpolation_points)

        for angle_in_rads in [math.radians(a) for a in angles_in_deg]:
            x = math.sin(angle_in_rads) * radius + center_x
            y = math.cos(angle_in_rads) * radius + center_y
            road_points.append((x, y))

        # Create an horizontal segment, make sure the points line up with previous segment
        x += radius / 2.0
        length = 30.0
        interpolation_points = int(length / 10.0)
        for x in np.linspace(x, x + length, num=interpolation_points):
            road_points.append((x, y))

        # Now we add a final road point "below" the last one just to illustrate how the interpolation works
        # But make sure the resulting turn is not too sharp...
        y -= 100.0
        x += 20.0
        road_points.append((x, y))

        # Creating the RoadTest from the points
        the_test = RoadTestFactory.create_road_test(road_points)

        return the_test

    def init_attribute(self):
        attribute = (randint(0, self.map_size), randint(0, self.map_size))
        return attribute

    def evaluate(self, individual):
        # Creating the RoadTest from the points
        road_points = list(individual)
        the_test = RoadTestFactory.create_road_test(road_points)

        # Send the test for execution
        test_outcome, description, execution_data = self.executor.execute_test(the_test)

        # Print test outcome
        # log.info("test_outcome %s", test_outcome)
        # log.info("description %s", description)

        # Collect the oob_percentage values
        oob_percentages = [state.oob_percentage for state in execution_data]
        # log.info("Collected %d states information. Max is %.3f", len(oob_percentages), max(oob_percentages))

        # Compute the fitness (= the average oob_percentage) TODO: change this to a better fitness function
        if len(oob_percentages) == 0:
            fitness = 0.0
        else:
            fitness = sum(oob_percentages) / len(oob_percentages) / 100.0
        log.info("Individual: %s, Fitness: %.3f", individual, fitness)

        return fitness,  # important to return a tuple since deap considers multiple objectives

    def start(self):
        log.info("Starting test generation")

        from deap import base
        from deap import creator
        from deap import tools

        # Define the problem type
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)

        num_road_points = 3  # number of points in the road; by default, we want to generate 3 points to make one curve
        toolbox = base.Toolbox()
        # an attribute is a point in the road
        toolbox.register("attribute", self.init_attribute)
        # an individual is road_points (list)
        toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute, n=num_road_points)
        # a population is a list of individuals
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        # Register the crossover and mutation operators' hyperparameters
        toolbox.register("mate", tools.cxTwoPoint)
        toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
        toolbox.register("select", tools.selTournament, tournsize=3)

        # Register the fitness evaluation function
        toolbox.register("evaluate", self.evaluate)

        # Run a simple ready-made GA
        pop_size = 10  # population size
        num_generations = 10  # number of generations
        pop, deap_log = deap.algorithms.eaSimple(toolbox.population(n=pop_size), toolbox,
                                                 cxpb=0.85, mutpb=0.1, ngen=num_generations, verbose=True)

        # Print the best individual
        best_individual = tools.selBest(pop, 1)[0]
        log.info("Best individual: %s", best_individual)