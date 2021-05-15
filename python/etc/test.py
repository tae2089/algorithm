import random


def reduce_node(adjancy,node):
    a = list()
    for i in adjancy:
        if node != i:
            a.append(i)
    return a

def make_weight(values):
    a = list()
    if values != 0:
        for _ in values:
            a.append(random.randint(-5,9))
        return a
    else:
        return []
    

def make_adjancylist(nodes):
    # 사용될 노드 설정
    use_node = nodes[:random.randint(0, len(nodes))]

    # 노드 연결 만들기
    graph = {node: reduce_node(use_node[:random.randint(0, len(nodes))],node) for node in use_node}

    print(graph)
    #가중치 설정하기
    weights = {
        node:  make_weight(values)for node,values in graph.items()
    }
    print(weights)
    return graph, weights


make_adjancylist(['A','B','C','D','E','F'])
