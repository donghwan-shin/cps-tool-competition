import deap.algorithms
import numpy as np
import math
import logging as log
from random import randint, gauss, random
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
from PIL import Image

from sample_test_generators.save_best_individual import BestIndividualSaver
from self_driving.beamng_car_cameras import BeamNGCarCameras
from code_pipeline.tests_generation import RoadTestFactory


class GATestGenerator():
    """
        Generates a set of tests using GA (based on the Deap library; https://github.com/deap/deap).

    """

    def __init__(self, cxpb: float, mutpb: float, pop_size: int, num_gens: int, executor=None, map_size=None):
        self.executor = executor
        self.map_size = map_size

        self.cxpb = cxpb  # crossover probability
        self.mutpb = mutpb  # mutation probability
        self.pop_size = pop_size  # population size
        self.num_gens = num_gens  # number of generations (including the initial population)

    def init_attribute(self):
        padding_size = self.map_size / 10
        attribute = (randint(padding_size, self.map_size - padding_size),
                     randint(padding_size, self.map_size - padding_size))
        return attribute

    def mutate_tuple(self, individual, mu, sigma, indpb):
        """(modified from deap.tools.mutGaussian)
        This function applies a gaussian mutation of mean *mu* and standard
        deviation *sigma* on the input individual. This mutation expects a
        :term:`sequence` individual composed of real valued 2-dimensional tuples.
        The *indpb* argument is the probability of each attribute to be mutated.

        :param individual: Individual to be mutated
        :param mu: Mean or :term:`python:sequence` of means for the
                   gaussian addition mutation
        :param sigma: Standard deviation or :term:`python:sequence` of
                      standard deviations for the gaussian addition mutation
        :param indpb: Independent probability for each attribute to be mutated
        :returns: A tuple of one individual.
        """

        for i in range(0, len(individual)):
            if random() < indpb:
                # convert tuple into list to update values
                point = list(individual[i])

                # update the first value (x-pos)
                point[0] += int(gauss(mu, sigma))
                if point[0] < 0:
                    point[0] = 0
                if point[0] > self.map_size:
                    point[0] = self.map_size

                # update the second value (y-pos)
                point[1] += int(gauss(mu, sigma))
                if point[1] < 0:
                    point[1] = 0
                if point[1] > self.map_size:
                    point[1] = self.map_size

                # update the attribute (tuple) in the individual
                individual[i] = tuple(point)

        return individual,

    def evaluate(self, individual):
        # Creating the RoadTest from the points
        road_points = list(individual)
        the_test = RoadTestFactory.create_road_test(road_points)

        # Send the test for execution
        # test_outcome, description, execution_data = self.executor.execute_test(the_test)
        test_outcome, description, execution_data = self.executor.execute_test(the_test, is_for_training=True)

        # Print test outcome
        # log.info("test_outcome %s", test_outcome)
        # log.info("description %s", description)

        # Collect the oob_percentage values
        oob_percentages = [state.oob_percentage for state in execution_data]
        # log.info("Collected %d states information. Max is %.3f", len(oob_percentages), max(oob_percentages))

        # Compute the fitness
        if len(oob_percentages) == 0:
            fitness = 0.0
        else:
            # fitness = sum(oob_percentages) / len(oob_percentages)
            fitness = max(oob_percentages)  # TODO: change this to a better fitness function
        log.info(f"Individual (road_points): {road_points}, "
                 f"test_outcome: {test_outcome}, "
                 f"Fitness: {fitness:.5f}")

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
        toolbox.register("mutate", self.mutate_tuple, mu=0, sigma=self.map_size/10, indpb=1)
        toolbox.register("select", tools.selTournament, tournsize=3)

        # Register the fitness evaluation function
        toolbox.register("evaluate", self.evaluate)

        # Run a simple ready-made GA
        # pop_size = 5  # population size(5,20)
        # num_generations = 20  # number of generations 5, 20
        hof = tools.HallOfFame(1)  # save the best one individual during the whole search
        pop, deap_log = deap.algorithms.eaSimple(population=toolbox.population(n=self.pop_size),
                                                 toolbox=toolbox,
                                                 halloffame=hof,
                                                 cxpb=self.cxpb,
                                                 mutpb=self.mutpb,
                                                 ngen=self.num_gens - 1,  # because it starts from an init population
                                                 verbose=False)

        # Print the best individual from the hall of fame
        best_individual = tools.selBest(hof, 1)[0]

        log.info(f"Best individual: {best_individual}, fitness: {best_individual.fitness}")

        # append the best individual to a file
        with open("GA_best_individuals.log", "a") as f:
            f.write(f'pop_size={self.pop_size}, num_gens={self.num_gens}, cxpb={self.cxpb}, mutpb={self.mutpb}, '
                    f'best_individual={best_individual}, fitness={best_individual.fitness}\n')

        # log.info(f"Best individual: {best_individual}, fitness: {best_individual.fitness}")
        #
        # # return best_individual
        # # folder_name = input("请输入文件夹名：")
        # # saver = BestIndividualSaver(folder_name)
        #
        # saver = BestIndividualSaver("best_individual", "n20_p5_c01_m01")
        # saver.save_best_individual(best_individual)
        #
        # log.info(f"拿到了结果")
        #
        #
        #
