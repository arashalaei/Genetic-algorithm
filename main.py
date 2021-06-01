import random
from Chromosome import Chromosome
# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt
def sort_population(population:list):
    population.sort(key=lambda x:x.get_fitness(),reverse=True)

def averaging(population) -> float:
    sum = 0
    for chromosome in population:
        sum += chromosome.get_fitness()
    
    return sum / len(population)

### Crossover ###
def crossover(first_chromosome: Chromosome, second_chromosome: Chromosome, type: str = "one_point") -> tuple:
    _map = first_chromosome.get_map()
    fisrt_children = Chromosome(_map , False)
    second_children = Chromosome(_map, False)

    if type == 'one_point':
        offspring = random.randint(0, len(first_chromosome.get_string()))
        fisrt_children.set_string(False, first_chromosome.get_string()[:offspring] + second_chromosome.get_string()[offspring:])
        second_children.set_string(False ,second_chromosome.get_string()[:offspring] + first_chromosome.get_string()[offspring:] )
    elif type == 'two_point':
        a = random.randint(0, len(first_chromosome.get_string()))
        b = random.randint(0, len(first_chromosome.get_string()))
        while b == a:
            b = random.randint(0, len(first_chromosome.get_string()))
        offspring_1 = min(a, b)
        offspring_2 = max(a, b)
        fisrt_children.set_string(False,first_chromosome.get_string()[:offspring_1] + second_chromosome.get_string()[offspring_1:offspring_2] + first_chromosome.get_string()[offspring_2:])
        second_children.set_string(False,second_chromosome.get_string()[:offspring_1] + first_chromosome.get_string()[offspring_1:offspring_2] + second_chromosome.get_string()[offspring_2:])
    
    return fisrt_children, second_children 
    
### Selection ###
def select(population: list ,type = 1):
    sort_population(population)
    selection_length = len(population)
    if selection_length % 2 != 0:
        selection_length -= 1
    selection_length /= 2
    if selection_length % 2 != 0:
        selection_length += 1
    if type == 1:
        return population[:int(selection_length)]
    elif type == 2:
        copy_population = population[:] # Copy of population
        output_list = []
        for i in range(int(selection_length)):
            random.shuffle(copy_population)
            output_list.append(copy_population.pop(0))
        return output_list

if __name__ == '__main__':
    _map = ['_', '_', 'G', '_', 'G', '_', 'M', 'L', '_', '_', 'G', '_','G', '_', 'G', '_', 'G', '_', 'M', 'L', '_', '_', 'G', '_']
    # first method
    population = []
    number_of_population = 400
    mean_list = []
    # 1) initial population
    for i in range(number_of_population):
        c = Chromosome(_map , False)
        population.append(c)
    
    sort_population(population)
    max_fitness = population[0].get_fitness()
    counter = 0
    iterate_number = 10
    print(max_fitness)
    best_fitness = []
    worst_fitness = []
    while True:
        if counter == iterate_number:
            break
        # 2)Selection
        selected_list = select(population , 2)
        # 3)Crossover
        epoch = []
        for i in range(len(selected_list)):
            a = random.randint(0,  len(selected_list) - 1)
            b = random.randint(0,  len(selected_list) - 1)
            while b == a:
                b = random.randint(0,  len(selected_list) - 1)

            children = crossover(selected_list[a], selected_list[b],"two_point")
            epoch.append(children[0])
            epoch.append(children[1])
        # 4)Mutation
        for chromosome in epoch:
            chromosome.mutate(False, 0.5)
        
        mean_list.append(averaging(epoch))

        population[10:] = epoch[:]

        counter += 1
        sort_population(population)
        best_fitness.append(population[0].get_fitness())
        worst_fitness.append(population[-1].get_fitness())
        if population[0].get_fitness() > max_fitness:
            max_fitness = population[0].get_fitness()
            counter = 0

    print(population[0].get_string(), max_fitness)
    print(mean_list)
    print(best_fitness)
    print(worst_fitness)

    # draw chart
    generation = []
    for i in range(len(mean_list)):
        generation.append(i+1)
    # mid
    plt.plot(generation, mean_list, label='mid')
    plt.xlabel('generation')
    plt.ylabel('fitness')
    plt.legend()
    plt.show()
    # best mid worst
    plt.plot(generation, mean_list, label='mid')
    plt.plot(generation, best_fitness, label='best')
    plt.plot(generation, worst_fitness, label='worst')
    plt.xlabel('generation')
    plt.ylabel('fitness')
    plt.legend()
    plt.show()


