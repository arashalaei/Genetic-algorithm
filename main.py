import  random 
from Chromosome import Chromosome

def crossover(first_chromosome: Chromosome, second_chromosome: Chromosome, type: str = "one_point") -> tuple:
    _map = first_chromosome.get_map()
    fisrt_children = Chromosome(_map)
    second_children = Chromosome(_map)

    if type == 'one_point':
        offspring = random.randint(1, len(first_chromosome.get_string()) - 1)
        fisrt_children.set_string(first_chromosome.get_string()[:offspring] + second_chromosome.get_string()[offspring:])
        second_children.set_string(second_chromosome.get_string()[:offspring] + first_chromosome.get_string()[offspring:] )
        return fisrt_children, second_children
    elif type == 'two_point':
        a = random.randint(1, len(first_chromosome.get_string()) - 1)
        b = random.randint(1, len(first_chromosome.get_string()) - 1)
        offspring_1 = min(a, b)
        offspring_2 = max(a, b)
        fisrt_children.set_string(first_chromosome.get_string()[:offspring_1] + second_chromosome.get_string()[offspring_1:offspring_2] + first_chromosome.get_string()[offspring_2:])
        second_children.set_string(second_chromosome.get_string()[:offspring_1] + first_chromosome.get_string()[offspring_1:offspring_2] + second_chromosome.get_string()[offspring_2:])
        return fisrt_children, second_children 


if __name__ == '__main__':
    _map = ['_', '_', '_', '_', 'G', '_', 'M', 'L', '_', '_', 'G', '_']
    population = []
    Number_of_population = 200

    for i in range(Number_of_population):
        c = Chromosome(_map)
        population.append(c)
    
    sample = population[51]      # To test
    print(sample.get_string(), sample.get_fitness())   # Chromosome genes string & ftness

    print('######')
    c1 = Chromosome(_map)
    c2 = Chromosome(_map)
    
    print(c1.get_string(), c1.get_fitness())
    print(c2.get_string(), c2.get_fitness())
    print('crossover')
    children = crossover(c1, c2, type='two_point')
    fisrt_child = children[0]
    second_child = children[1]
    print(fisrt_child.get_string(), fisrt_child.get_fitness())
    print(second_child.get_string(), second_child.get_fitness())


