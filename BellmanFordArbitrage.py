import numpy as np

def dijkstra(table, start):
    n = len(table)
    distances = [float('inf')] * n
    distances[start] = 0
    prev = [-1] * n  # stores previous node

    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if distances[u] + table[u][v] < distances[v]:
                    distances[v] = distances[u] + table[u][v]
                    prev[v] = u

    # see if negative cycle exists
    for u in range(n):
        for v in range(n):
            if distances[u] + table[u][v] < distances[v]:
                node = v
                cycle = [node]
                while prev[node] != v:
                    node = prev[node]
                    cycle.append(node)
                cycle.append(v)
                return cycle[::-1]  # return cycle in order

    return None  # if no neg cycle found return none

def BellmanFord(table):
    n = len(table)
    log_table = [[-np.log(rate) for rate in row] for row in table]

    cycle = dijkstra(log_table, 0)  # see if BellmanFord is detected on any node

    if cycle is not None:
        # calc the percentage of profit
        profit = 1
        for i in range(len(cycle) - 1):
            # take neg log to get shortest path
            profit *= np.exp(-log_table[cycle[i]][cycle[i + 1]])
        profit_percentage = (profit - 1) * 100

        # print the sequence of BellmanFord opportunity
        print(' -> '.join(map(str, cycle)))
        # return percentage of profit if none return none found
        return profit_percentage
    else:
        print("BellmanFord opportunity not found")
        return 0

# Test case
currency = [[1, 49, 1 / 0.0107],
            [1 / 49, 1, 2],
            [0.0107, 0.5, 1]]

print(BellmanFord(currency))

#take neg log for shortest path
