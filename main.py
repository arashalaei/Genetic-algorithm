from Chromosome import Chromosome

if __name__ == '__main__':
    _map = ['_', '_', '_', '_', 'G', '_', 'M', 'L', '_', '_', 'G', '_']
    population = []
    Number_of_population = 200

    for i in range(Number_of_population):
        c = Chromosome(_map)
        population.append(c)
    
    sample = population[51]      # To test
    print(sample.get_string())   # Chromosome genes string
    print(sample.get_fitness())  # fitness valus
