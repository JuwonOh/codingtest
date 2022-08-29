def solution(n, computers):
    visited = []
    intranet = []
    network = []

    def dfs(node):
        visited.append(node)
        intranet.append(node)
        for nextnode in range(n):
            if nextnode not in visited and computers[node][nextnode] == 1:
                dfs(nextnode)
        return intranet

    for node in range(n):
        if node not in visited:
            network.append(dfs(node))
            intranet.clear()

    return len(network)
