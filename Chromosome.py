import random

class Chromosome:
    __map: list
    __actions = ['0', '0', '0', '0', '1', '2']
    __string: str 
    __fitness: int

    def __init__(self, _map) -> None:
        self.__map = _map
        self.__string = list()
        self.__fitness = 0
        self.__create()
        self.__calc_fitness()

    def get_map(self) -> list:
        return self.__map

    def get_string(self) -> list:
        return self.__string

    def get_fitness(self) -> list:
        return self.__fitness

    def set_string(self, new_string: list) -> None:
        self.__string = new_string
        self.__calc_fitness()

    def __create(self) -> None:
        for i in range(len(self.__map)):
            random.shuffle(self.__actions)
            self.__string.append(self.__actions[random.randint(0, len(self.__actions) - 1)])

    def mutate(self, possibility = 0.1):
        l = []
        if possibility == 0.1:
            l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        elif possibility == 0.5:
            l = [0, 1]

        if l[random.randint(0, len(l) - 1)] == 1:
            gen_number = random.randint(0, len(self.__map) - 1)
            self.__string[gen_number] = self.__actions[random.randint(0, len(self.__actions) - 1)]
            self.__calc_fitness()

    def __calc_fitness(self) -> None:
        path = location = 1
        score = max_path = 0
        __win__ = True
        for i in range(len(self.__string)):
            if location == len(self.__string) - 1:
                if self.__string[i+1] == '1':     # jump in last level
                    score = score + 2
                break
            if self.__map[location] == 'G':
                if i-1 >= 0 and self.__string[i] == '0' and self.__string[i-1] == '1':
                    score = score + 2
                elif self.__string[i] == '1':
                    score = score + 2
                elif not (self.__string[i] == '1'):  # lost
                    max_path = max(max_path, path-1)
                    path = 0
                    __win__ = False
            elif self.__map[location] == 'M':
                if not (self.__string[i] == '1' and self.__string[i+1] == '0'):
                    score = score + 2
            elif self.__map[location] == 'L':
                if not (self.__string[i] == '2' and self.__string[i+1] == '0'):  # lost
                    max_path = max(max_path, path-1)
                    path = 0
                    __win__ = False
            location = location + 1
            path = path + 1
        max_path = max(max_path, path)
        score = score + max_path
        if __win__:
            score = score + 5

        self.__fitness = score