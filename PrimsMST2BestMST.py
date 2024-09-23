#Problem 1 MST Prims
import math
def prim2(G, r):
    n = len(G)
    p = [(None, math.inf)]*n # (pred, proximity) for each vertex
    p[r] = (None, 0)
    ## Complete this part##
    # keep vertex already found in mst
    present_in_mst = n * [False]
    #build the mst
    for i in range(n):
        #find the closest min adj vertex not in mst
        minimum_adj = math.inf
        u = -1
        for i in range(n):
            if p[i][1] < minimum_adj and not present_in_mst[i]:
                minimum_adj = p[i][1]
                u = i
        #if found include in the mst
        present_in_mst[u] = True
        #update value for min adj vertex
        for z in range(n):
            if not present_in_mst[z] and G[u][z] < p[z][1] and G[u][z] != 0:
                p[z] = (u, G[u][z])

    # Construct a MST from p
    A = []
    for i in range(n):
        if p[i][0] != None:
            A.append((i, p[i][0]))
    return A
# Test cases
g1 = [ [ 0, 4, 0, 0, 0, 0, 0, 8, 0],
[ 4, 0, 8, 0, 0, 0, 0, 11, 0],
[ 0, 8, 0, 7, 0, 4, 0, 0, 2],
[ 0, 0, 7, 0, 9, 14, 0, 0, 0],
[ 0, 0, 0, 9, 0, 10, 0, 0, 0],
[ 0, 0, 4, 14, 10, 0, 2, 0, 0],
[ 0, 0, 0, 0, 0, 2, 0, 1, 6],
[ 8, 11, 0, 0, 0, 0, 1, 0, 7],
[ 0, 0, 2, 0, 0, 0, 6, 7, 0] ]
print(prim2(g1, 0))
# The above should return
# [(1, 0), (2, 1), (3, 2), (4, 3), (5, 2), (6, 5), (7, 6), (8, 2)]
g2 = [ [ 0, 8, 5, 9, 6, 3],
[ 8, 0, 2, 2, 5, 2],
[ 5, 2, 0, 3, 1, 7],
[ 9, 2, 3, 0, 1, 9],
[ 6, 5, 1, 1, 0, 9],
[ 3, 2, 7, 9, 9, 0] ]
print(prim2(g2, 0))
# The above should return [(1, 5), (2, 1), (3, 4), (4, 2), (5, 0)]





#Problem 2 second best mst
import math

def secondMST(G, r):
    #find initial mst
    mst = prim2(G, r)
    mst_weight = sum(G[u][v] for u, v in mst)
    n = len(G)
    second_best_weight = math.inf
    second_best_mst = None

    for u, v in mst:
        # remove edge u, v from graph temporarily
        temp = G[u][v]
        G[u][v] = G[v][u] = 0

        # Calc mst of resulting graph
        new_mst = prim2(G, r)
        new_weight = sum(G[a][b] for a, b in new_mst)

        # iff the weight of new mst > weight of the original mst
        # and less than current second-best then update the second best
        if mst_weight < new_weight < second_best_weight:
            second_best_weight = new_weight
            second_best_mst = new_mst

        #add edge u, v back into graph
        G[u][v] = G[v][u] = temp

    return second_best_mst

# Test cases
g1 = [ [ 0, 4, 0, 0, 0, 0, 0, 8, 0],
[ 4, 0, 8, 0, 0, 0, 0, 11, 0],
[ 0, 8, 0, 7, 0, 4, 0, 0, 2],
[ 0, 0, 7, 0, 9, 14, 0, 0, 0],
[ 0, 0, 0, 9, 0, 10, 0, 0, 0],
[ 0, 0, 4, 14, 10, 0, 2, 0, 0],
[ 0, 0, 0, 0, 0, 2, 0, 1, 6],
[ 8, 11, 0, 0, 0, 0, 1, 0, 7],
[ 0, 0, 2, 0, 0, 0, 6, 7, 0] ]
print(secondMST(g1, 0))
# The above should return
# [(1, 0), (2, 1), (3, 2), (5, 4), (5, 2), (6, 5), (7, 6), (8, 2)]
g2 = [ [ 0, 8, 5, 9, 6, 3],
[ 8, 0, 2, 2, 5, 2],
[ 5, 2, 0, 3, 1, 7],
[ 9, 2, 3, 0, 1, 9],
[ 6, 5, 1, 1, 0, 9],
[ 3, 2, 7, 9, 9, 0] ]
print(secondMST(g2, 0))
# The above should return[(1, 5), (2, 1), (3, 4), (1, 3), (5, 0)]
# (or any spanning tree whose total weight is 10.)