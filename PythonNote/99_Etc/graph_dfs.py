class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices  # 정점의 개수
        self.adj_list = [[] for _ in range(num_vertices)]  # 인접 리스트를 사용한 그래프 표현

    def add_edge(self, u, v):
        self.adj_list[u].append(v)  # 간선 추가 메서드: 두 정점 u, v를 인자로 받아 간선을 추가

    def _dfs_util(self, vertex, visited):
        visited[vertex] = True  # 정점을 방문한 것으로 표시
        print(f"방문한 노드: {vertex}")

        # 인접한 정점들을 순회하며 방문하지 않은 정점에 대해 재귀 호출
        for adjacent in self.adj_list[vertex]:
            if not visited[adjacent]:
                self._dfs_util(adjacent, visited)

    def dfs(self, start_vertex):
        visited = [False] * self.num_vertices  # 방문한 정점을 기록하는 리스트
        self._dfs_util(start_vertex, visited)  # 깊이 우선 탐색 실행

if __name__ == "__main__":
    graph = Graph(6)  # 6개의 정점을 가진 그래프 객체 생성

    # 간선 추가
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)

    graph.dfs(0)  # 시작 정점을 0으로 설정하고 깊이 우선 탐색 실행
