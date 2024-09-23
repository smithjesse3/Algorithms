#prolem 1, wrsetlers
def designate(V, E):
    #import deque for breadth first search
    from collections import deque
    # store wrestlers and adjacent list
    wrestlers = {name: None for name in V}
    adj_list = {name: [] for name in V}

    # Create the adjacency list
    for pair in E:
        adj_list[pair[0]].append(pair[1])
        adj_list[pair[1]].append(pair[0])

    # Execute BFS to assign wrestlers face or heel
    for wrestler in V:
        if wrestlers[wrestler] is None:
            q = deque([(wrestler, 'face')])  # Start with wrestler as face
            while q:
                current, designation = q.popleft()
                if wrestlers[current] is None:
                    wrestlers[current] = designation
                    for neighbor in adj_list[current]:
                        q.append((neighbor, 'heel' if designation == 'face' else 'face'))

    # Group wrsetlers as either faces or heels
    faces = [wrestler for wrestler, designation in wrestlers.items() if designation == 'face']
    heels = [wrestler for wrestler, designation in wrestlers.items() if designation == 'heel']

    # Make sure there is no rivalry
    for pair in E:
        if wrestlers[pair[0]] == wrestlers[pair[1]]:
            return None

    return faces, heels

#test cases

V = ['The Rock', 'Steve Austin']
E = [('The Rock', 'Steve Austin')]
print(designate(V, E))
# this should return (['The Rock'], ['Steve Austin']) or (['Steve Austin'], ['The Rock']).
V = ['The Rock', 'Steve Austin', 'Triple H']
E = [('The Rock', 'Steve Austin'), ('The Rock', 'Triple H'), ('Steve Austin', 'Triple H')]
print(designate(V, E))
# this should return None

#Problem 2, alien dictionary
# import deque for BFS
from collections import deque
#create alien dictionary function
def alienDictionary(words):
    in_degree = {c : 0 for word in words for c in word}
    adj_list = {c: [] for c in in_degree}

    # Populate adjacency list and in_degree
    for i in range(0, len(words) - 1):
        # the first character difference between two consecutive words determined
        for c, d in zip(words[i], words[i + 1]):
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].append(d)
                    in_degree[d] += 1
                break
        # make sure the second word isnt a prefix
        else:
            if len(words[i]) > len(words[i + 1]):
                return None

    # Pick nodes whose in_degree is 0
    output = []
    q = deque([c for c in in_degree if in_degree[c] == 0])
    while q:
        c = q.popleft()
        output.append(c)
        for d in adj_list[c]:
            in_degree[d] -= 1
            if in_degree[d] == 0:
                q.append(d)

    # If all not found in output return none
    if len(output) < len(in_degree):
        return None
    return output
#test cases
print(alienDictionary(['bbc','ba','cb','a'])) # returns ['b','c','a']
print(alienDictionary(['baa','abcd','abca','cab','cad'])) # returns ['b','d','a','c']
print(alienDictionary(['acab', 'baca', 'dac'])) # returns ['a', 'c', 'b', 'd']