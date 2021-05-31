import random

class Chromosome:
    _map: list
    __actions = ['0', '0', '0', '1', '2']
    __string: str 
    __fitness: int

    def __init__(self, _map) -> None:
        self._map = _map
        self.__string = list()
        self.__fitness = 0
        self.__create()
        self.__calc_fitness()

    def get_string(self) -> list:
        return self.__string

    def get_fitness(self) -> list:
        return self.__fitness

    def __create(self) -> None:
        for i in range(len(self._map)):
            random.shuffle(self.__actions)
            self.__string.append(self.__actions[random.randint(0, len(self.__actions) - 1)])

    def __calc_fitness(self) -> None:
        path = location = 1
        score = max_path = 0
        __win__ = True
        for i in range(len(self.__string)):
            if location == len(self.__string) - 1:
                if self.__string[i+1] == '1':     # jump in last level
                    score = score + 2
                break
            if self._map[location] == 'G':
                if i-1 >= 0 and self.__string[i] == '0' and self.__string[i-1] == '1':
                    score = score + 2
                elif self.__string[i] == '1':
                    score = score + 2
                elif not (self.__string[i] == '1'):  # lost
                    max_path = max(max_path, path-1)
                    path = 0
                    __win__ = False
            elif self._map[location] == 'M':
                if not (self.__string[i] == '1' and self.__string[i+1] == '0'):
                    score = score + 2
            elif self._map[location] == 'L':
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