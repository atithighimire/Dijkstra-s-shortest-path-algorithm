from heapq import heapify, heappush, heappushpop
import sys


def dijsktra(graph, source, destination):
    inf = sys.maxsize
    node_data = {

        'A': {'cost': inf, 'pred': []},
        'B': {'cost': inf, 'pred': []},
        'C': {'cost': inf, 'pred': []},
        'D': {'cost': inf, 'pred': []},
        'E': {'cost': inf, 'pred': []},
        'F': {'cost': inf, 'pred': []},
    }

    node_data[source]['cost'] = 0
    visited = []

    temp = source

    for i in range(5):

        if temp not in visited:
            visited.append(temp)
            min_heap = []

            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + \
                            list(temp)

                    heappush(min_heap, (node_data[j]['cost'], j))
        heapify(min_heap)
        temp = min_heap[0][1]

    print('Shortest Path: ' +
          str(node_data[destination]['pred'] + list(destination)))

    print('Shortest Distance: ' + str(node_data[destination]['cost']))


if __name__ == "__main__":
    graph = {
        'A': {'B': 2, 'C': 5, 'F': 11},
        'B': {'A': 2, 'C': 8, 'D': 5, 'E': 13},
        'C': {'A': 5, 'B': 8, 'E': 12},
        'D': {'B': 5, 'E': 1, 'F': 17},
        'E': {'B': 13, 'C': 12, 'D': 1},
        'F': {'A': 11, 'D': 17}
    }

    source = 'A'
    destination = 'F'
    dijsktra(graph, source, destination)
