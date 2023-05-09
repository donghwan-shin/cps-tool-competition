import re



pop_size = 15
num_gens = 5
cxpb = 0.9
mutpb = 0.9
fitness_list = []

with open('average_o.txt', 'r') as f:
    for line in f:
        if 'pop_size={}, num_gens={}, cxpb={}, mutpb={}'.format(pop_size, num_gens, cxpb, mutpb) in line:
            match = re.search('fitness=\((.*?)\)', line)
            fitness = float(match.group(1))
            fitness_list.append(fitness)

average_fitness = sum(fitness_list) / len(fitness_list)
with open('average.txt', 'w') as f:
    f.write('pop_size={}, num_gens={}, cxpb={}, mutpb={}\n'.format(pop_size, num_gens, cxpb, mutpb))
    f.write('Average Fitness: {}\n'.format(average_fitness))
    f.write('All Fitness: {}\n'.format(fitness_list))

