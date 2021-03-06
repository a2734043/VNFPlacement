import numpy as np

k8s_small = [[0, 9, 19, 20, 22, 23, 24],
             [1, 2, 4, 10, 18, 21],
             [6, 8, 11, 13, 15, 25],
             [7, 12, 16, 26, 28, 29],
             [3, 5, 14, 17, 27]]

k8s_ms = [[4, 10, 14, 15, 16, 24, 29],
          [0, 12, 26, 27],
          [6, 8, 13, 22, 25, 28],
          [2, 5, 7, 9, 11, 18, 19, 21, 23],
          [1, 3, 17, 20]]

k8s_medium = [[2, 7, 17, 20, 21, 25],
              [1, 19, 24, 26, 27, 28],
              [4, 10, 11, 14, 15, 29],
              [3, 5, 6, 16, 18, 22, 23],
              [0, 8, 9, 12, 13]]

k8s_ml = [[5, 11, 15, 20, 23, 25],
          [3, 4, 7, 13, 21, 27, 28],
          [0, 9, 10, 14, 18, 26],
          [8, 17, 19, 24, 29],
          [1, 2, 6, 12, 16, 22]]

k8s_large = [[1, 3, 4, 8, 17, 21],
             [2, 6, 10, 19, 22, 23],
             [0, 7, 9, 13, 25, 26],
             [5, 15, 18, 20, 27, 28, 29],
             [11, 12, 14, 16, 24]]

son_small = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 28],
             [25, 26, 27, 29],
             [],
             [],
             []]

son_ms = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
          [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
          [],
          [],
          []]

son_medium = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
              [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
              [],
              []]

son_ml = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          [10, 11, 12, 15, 16, 17, 18, 19],
          [20, 21, 22, 23, 24, 25, 26, 27],
          [13, 14, 28, 29],
          []]

son_large = [[0, 1, 2, 3, 4, 5, 6, 7],
             [8, 9, 10, 11, 12, 13, 14, 21],
             [15, 16, 17, 18, 19, 20, 22, 23],
             [24, 25, 26, 27, 28, 29],
             []]

vnf_resource_list_small = [[1, 2, 10], [2, 2, 10], [4, 1, 10], [5, 4, 10], [2, 5, 10],
                           [2, 3, 10], [1, 4, 10], [5, 5, 10], [5, 2, 10], [4, 3, 10],
                           [2, 1, 10], [4, 4, 10], [3, 3, 10], [3, 5, 10], [3, 4, 10],
                           [4, 1, 10], [4, 1, 10], [1, 3, 10], [5, 1, 10], [4, 3, 10],
                           [5, 5, 10], [3, 3, 10], [2, 3, 10], [2, 1, 10], [3, 1, 10],
                           [3, 5, 10], [2, 2, 10], [5, 4, 10], [1, 4, 10], [3, 4, 10]]

vnf_resource_list_ms = [[1, 2, 10], [2, 2, 10], [4, 1, 10], [5, 4, 10], [2, 5, 10],
                        [2, 3, 10], [1, 4, 10], [5, 5, 10], [5, 2, 10], [4, 3, 10],
                        [2, 1, 10], [4, 4, 10], [3, 3, 10], [3, 5, 10], [3, 4, 10],
                        [8, 9, 10], [9, 8, 10], [7, 7, 10], [8, 6, 10], [7, 6, 10],
                        [6, 8, 10], [9, 6, 10], [7, 8, 10], [9, 9, 10], [6, 7, 10],
                        [8, 6, 10], [8, 7, 10], [8, 6, 10], [6, 6, 10], [6, 7, 10]]

vnf_resource_list_medium = [[7, 9, 10], [9, 8, 10], [7, 7, 10], [9, 6, 10], [9, 6, 10],
                            [8, 6, 10], [6, 8, 10], [7, 8, 10], [6, 6, 10], [8, 6, 10],
                            [9, 6, 10], [6, 9, 10], [6, 7, 10], [6, 8, 10], [9, 8, 10],
                            [8, 9, 10], [9, 8, 10], [7, 7, 10], [8, 6, 10], [7, 6, 10],
                            [6, 8, 10], [9, 6, 10], [7, 8, 10], [9, 9, 10], [6, 7, 10],
                            [8, 6, 10], [8, 7, 10], [8, 6, 10], [6, 6, 10], [6, 7, 10]]

vnf_resource_list_ml = [[8, 9, 10], [9, 8, 10], [7, 7, 10], [8, 6, 10], [7, 6, 10],
                        [6, 8, 10], [9, 6, 10], [7, 8, 10], [9, 9, 10], [6, 7, 10],
                        [8, 6, 10], [8, 7, 10], [8, 6, 10], [6, 6, 10], [6, 7, 10],
                        [10, 20, 10], [10, 20, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10],
                        [10, 10, 10], [10, 20, 10], [10, 10, 10], [10, 20, 10], [10, 10, 10],
                        [10, 10, 10], [10, 10, 10], [10, 20, 10], [10, 10, 10], [10, 20, 10]]

vnf_resource_list_large = [[10, 20, 10], [10, 20, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10],
                           [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 20, 10],
                           [10, 20, 10], [10, 10, 10], [10, 10, 10], [10, 20, 10], [10, 20, 10],
                           [10, 20, 10], [10, 20, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10],
                           [10, 10, 10], [10, 20, 10], [10, 10, 10], [10, 20, 10], [10, 10, 10],
                           [10, 10, 10], [10, 10, 10], [10, 20, 10], [10, 10, 10], [10, 20, 10]]

node_resource = {
    'cpu': 80,
    'memory': 160,
    'BW': 1000
}

placement = {'son': [son_small,
                     son_ms,
                     son_medium,
                     son_ml,
                     son_large],
             'k8s': [k8s_small,
                     k8s_ms,
                     k8s_medium,
                     k8s_ml,
                     k8s_large]}

vnf_resource_list = [vnf_resource_list_small,
                     vnf_resource_list_ms,
                     vnf_resource_list_medium,
                     vnf_resource_list_ml,
                     vnf_resource_list_large]

vnf_combination = ['small',
                   '3small3medium',
                   'medium',
                   '3medium3large',
                   'large']


def calculate(vnf_resource_list, placement):
    score = 0
    for index, node_stat in enumerate(placement):
        cpu_usage = np.sum([vnf_resource_list[i][0] for i in node_stat]) / node_resource['cpu']
        memory_usage = np.sum([vnf_resource_list[i][1] for i in node_stat]) / node_resource['memory']
        bw_usage = np.sum([vnf_resource_list[i][2] for i in node_stat]) / node_resource['BW']
        if cpu_usage > 1 or memory_usage > 1 or bw_usage > 1:
            score = -99
        node_score = (int(cpu_usage * 10) + int(memory_usage * 10))/2
        # + int(bw_usage * 10)

        # cpu = node_resource['cpu'] - np.sum([vnf_resource_list[i][0] for i in node_stat])
        # memory = node_resource['memory'] - np.sum([vnf_resource_list[i][1] for i in node_stat])
        # node_score = cpu + memory

        score += node_score
        if len(node_stat) == 0:
            score += 10
    return score


a = list()
for index, value in enumerate(vnf_resource_list):
    print(vnf_combination[index] + 'score:')
    score = calculate(value, placement['k8s'][index])
    print(score)
    a.append(score)
print(a)
