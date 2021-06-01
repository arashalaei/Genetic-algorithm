import  random 
from Chromosome import Chromosome

### Crossover ###
def crossover(first_chromosome: Chromosome, second_chromosome: Chromosome, type: str = "one_point") -> tuple:
    _map = first_chromosome.get_map()
    fisrt_children = Chromosome(_map)
    second_children = Chromosome(_map)

    if type == 'one_point':
        offspring = random.randint(0, len(first_chromosome.get_string()))
        fisrt_children.set_string(first_chromosome.get_string()[:offspring] + second_chromosome.get_string()[offspring:])
        second_children.set_string(second_chromosome.get_string()[:offspring] + first_chromosome.get_string()[offspring:] )
    elif type == 'two_point':
        a = random.randint(0, len(first_chromosome.get_string()))
        b = random.randint(0, len(first_chromosome.get_string()))
        while b == a:
            b = random.randint(0, len(first_chromosome.get_string()))
        offspring_1 = min(a, b)
        offspring_2 = max(a, b)
        fisrt_children.set_string(first_chromosome.get_string()[:offspring_1] + second_chromosome.get_string()[offspring_1:offspring_2] + first_chromosome.get_string()[offspring_2:])
        second_children.set_string(second_chromosome.get_string()[:offspring_1] + first_chromosome.get_string()[offspring_1:offspring_2] + second_chromosome.get_string()[offspring_2:])
    
    return fisrt_children, second_children 

def sort_population(population:list):
    population.sort(key=lambda x:x.get_fitness(),reverse=True)
    
### Selection ###
def selection(population: list ,type = 1):
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
    _map = ['_', '_', '_', '_', 'G', '_', 'M', 'L', '_', '_', 'G', '_']
    population = []
    Number_of_population = 200

    for i in range(Number_of_population):
        c = Chromosome(_map)
        population.append(c)
    
    print('Selection')
    print(selection(population,type=1)[0].get_fitness())

    print('######')
    c1 = Chromosome(_map)
    c2 = Chromosome(_map)
    
    print(c1.get_string(), c1.get_fitness())
    print(c2.get_string(), c2.get_fitness())
    print('crossover')
    children = crossover(c1, c2, type='one_point')
    fisrt_child = children[0]
    second_child = children[1]
    print(fisrt_child.get_string(), fisrt_child.get_fitness())
    print(second_child.get_string(), second_child.get_fitness())
    
    print('######')
    c3 = Chromosome(_map)
    print(c3.get_string(), c3.get_fitness())
    print('Mutation')
    c3.mutate(possibility=0.5)
    print(c3.get_string(), c3.get_fitness())