import heapq
import random


def reduce_node(adjancy, node):
    a = list()
    for i in adjancy:
        if node != i:
            a.append(i)
    return a


def make_weight(values):
    a = list()
    if values != 0:
        for _ in values:
            a.append(random.randint(-5, 9))
        return a
    else:
        return []


def make_adjancylist(nodes):
    # 사용될 노드 설정
    use_node = nodes[:random.randint(0, len(nodes))]

    # 노드 연결 만들기
    graph = {node: reduce_node(use_node[:random.randint(
        0, len(nodes))], node) for node in use_node}
    #가중치 설정하기
    weights = {
        node:  make_weight(values)for node, values in graph.items()
    }
    return graph, weights,use_node


def isinnagativenode(graph,nodes):
    for node in nodes:
        for weight in graph[node]:
            if weight<0:
                return False
    return True

def dijkstra(graph, weights,start):
    print("dijkstra algorithm")
    # 각 노드에 inf넣기
    distances = {node: float('inf') for node in graph}
    #초기화
    distances[start] = 0
    queue = []
    q2 = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        #거리, 노드
        current_distance, current_node = heapq.heappop(queue)
        #같은 노드의 크기 비교 -> 현재 노드의 값이 currnet_distance보다 작으면 pass
        if distances[current_node] < current_distance:
            continue
        else:
            # 순서
            q2.append(current_node)
        # 노드와 연결된 다른 노드들 꺼내기 adjacent = 노드들, weight= 가중치(거리)
        # enumerate(graph[current_node].values())
        for i, adjacent in enumerate(graph[current_node]):
            #노드에서 더한 값 구하기
            #weigths[current_node][i]의 값 을 for문으로 돌려주기

            distance = current_distance + weights[current_node][i]
            #거리가 이전보다 작으면 바꿔주기
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    return distances, q2



def bellman_ford(graph, weights,start):
    print("bellman_ford")
    distance, predecessor = dict(), dict()  # 거리 값, 각 정점의 이전 정점을 저장할 딕셔너리
    # 거리 값을 모두 무한대로 초기화 / 이전 정점은 None으로 초기화
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[start] = 0  # 시작 정점 거리는 0

    # 간선 개수(V-1)만큼 반복
    for _ in range(len(graph) - 1):
        #a,b,c,d,e,f key값 나옴
        for node in graph:
            # value
            for i,neighbour in enumerate(graph[node]):  # 각 정점마다 모든 인접 정점들을 탐색
                # (기존 인접 정점까지의 거리 > 기존 현재 정점까지 거리 + 현재 정점부터 인접 정점까지 거리)인 경우 갱신
                if distance[neighbour] > distance[node] + weights[node][i]:
                    # 값 갱신하기
                    distance[neighbour] = distance[node] + weights[node][i]
                    #중심이 될 노드 변경
                    predecessor[neighbour] = node

    # 음수 사이클 존재 여부 검사 : V-1번 반복 이후에도 갱신할 거리 값이 존재한다면 음수 사이클 존재
    for node in graph:
        for i, neighbour in enumerate(graph[node]):
            if distance[neighbour] > distance[node] + weights[node][i]:
                return -1, "그래프에 음수 사이클이 존재합니다."
    return distance, predecessor




def solution(graph,weights,nodes):
    #
    if isinnagativenode(weights,nodes):
        distance,predecessor= dijkstra(graph,weights, nodes[0])
        print(distance)
    else:
        distance, predecessor = bellman_ford(graph,weights, nodes[0])
        print(distance)


def main():

    nodes = ['A','B','C','D','E','F']
    mygraph, weights,use_node = make_adjancylist(nodes)
    print("graph:",mygraph)
    print("weights:",weights)
    solution(mygraph,weights,use_node)

if __name__ == '__main__':
    main()
