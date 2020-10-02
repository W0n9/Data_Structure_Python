def bfs(graph, start):
    # explored：已经遍历的节点列表，queue:寻找待遍历的节点队列
    '''
    图的深度遍历搜索BFS
    类似树的层序遍历
    '''
    explored, queue = [], [start]
    explored.append(start)
    while queue:
        # v:将要遍历的某节点
        v = queue.pop(0)
        # w:节点 v 的邻居
        for w in graph[v]:
            # w:如果 w 未被遍历，则遍历
            if w not in explored:
                # 添加 w 节点到已遍历的节点列表
                explored.append(w)
                # 添加 w 节点到寻找待遍历的节点队列
                queue.append(w)
    return explored


G = {
    '0': ['1', '2'],
    '1': ['2', '3'],
    '2': ['3', '5'],
    '3': ['4'],
    '4': [],
    '5': []
}

print(bfs(G, '0'))