from typing import Dict


class Graph(object):
    def __init__(self):
        self.nodes = []  # 表示图的点集
        self.edge: Dict[str, list] = {}  # 表示图的边集

    def insert(self, a, b, conf=2):
        '''
        有向图参数说明
        conf=0, a->b
        conf=1, b->a
        conf!=0 or 1, a<->b
        '''
        # 如果 a 不在图的点集里，则添加 a
        if not (a in self.nodes):
            self.nodes.append(a)
            self.edge[a] = list()
        # 如果 b 不在图的点集里，则添加 b
        if not (b in self.nodes):
            self.nodes.append(b)
            self.edge[b] = list()
        if conf == 0:
            self.edge[a].append(b)
        elif conf == 1:
            self.edge[b].append(a)
        else:
            # a 连接 b
            self.edge[a].append(b)
            # b 连接 a
            self.edge[b].append(a)

    def succ(self, a):
        # 返回与 a 连接的点
        return self.edge[a]

    def show_nodes(self):
        # 返回图的点集
        return self.nodes

    def show_edge(self):
        print(self.edge)


graph = Graph()
graph.insert('0', '1')
graph.insert('0', '2')
graph.insert('0', '3')
graph.insert('1', '3')
graph.insert('2', '3')
graph.show_edge()