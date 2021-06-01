import math

_map = ['_', '_', '_', '_', 'G', '_', 'M', 'L', '_', '_', 'G', '_']


def fitness_value(chromosome, _win_mode_):
    path = location = 1
    score = max_path = 0
    __win__ = True
    for i in range(len(chromosome)):
        if location == len(chromosome) - 1:
            if chromosome[i+1] == '1':     # jump in last level
                score = score + 2
            break
        if _map[location] == 'G':
            if i-1 >= 0 and chromosome[i] == '0' and chromosome[i-1] == '1':
                score = score + 2
            elif chromosome[i] == '1':
                score = score + 2
            elif not (chromosome[i] == '1'):  # lost
                max_path = max(max_path, path-1)
                path = 0
                __win__ = False
        elif _map[location] == 'M':
            if not (chromosome[i] == '1' and chromosome[i+1] == '0'):
                score = score + 2
        elif _map[location] == 'L':
            if not (chromosome[i] == '2' and chromosome[i+1] == '0'):  # lost
                max_path = max(max_path, path-1)
                path = 0
                __win__ = False
        if chromosome[i] == '1':
            score = score - 0.5
        location = location + 1
        path = path + 1
    max_path = max(max_path, path)
    score = score + max_path
    if __win__ and _win_mode_:
        score = score + 5

    return score

test = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
test1 = ['0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0']
test2 = ['0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1']

f = [test1, test2, test]
# print(fitness_value(test))


def choice(chromosomes, mode):
    __my__dict__ = {}
    for c in chromosomes:
        __my__dict__[str(c)] = fitness_value(c, True)
    mark_list = sorted(__my__dict__.items(), key=lambda x: x[1], reverse=True)
    sort_dict = dict(mark_list)
    len_of_best_chromosomes = math.ceil(len(sort_dict) / 2)
    temp = sort_dict.keys()
    return temp


print(choice(f, 1))




