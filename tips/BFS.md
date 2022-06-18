## BFS(너비 우선 탐색)

- 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
- 큐 자료구조를 이용해서 다음과 같이 활동한다.
    - 탐색 시작 노드를 큐에 삽입하고, 방문 처리를 한다.
    - 큐에서 노드를 꺼내고, 해당 노드의 인접 노드에서 방문하지 않은 노드를 전부 큐에 삽입하여 방문 처리 한다.
    - 위의 작업을 실행 할 수 없을때까지 반복.

step 0: 시작 노드인 1번을 queue에 넣고 방문 처리를 한다. 
step 1: queue에서 1을 꺼내고, 1에서 방문하지 않은 인접 노드 2,3,8을 큐에 넣고, 방문 처리 한다.
step 2: queue에서 2를 꺼내서 방문하지 않은 인접 노드 7을 queue에 삽입하고 방문처리 한다.
step 3: queue에서 3을 꺼내서 방문하지 않은 인접 노드 4,5를 queue에 삽입하고 방문처리 한다.
step 4: queue에서 8을 꺼내고, 방문하지 않은 인접 노드가 없기에 무시한다.
step 5: 이런 방식으로 queue에서 오드를 넣고 뺀다.

- 시작 노드부터 가까운 노드를 중심으로 탐색. 넓게 탐색한다. 가까운 노드부터 탐색
- 출발 노드에서 거리가 가까운 순으로 노드가 배치된다.
  
## 유의점
- 간선의 비용이 모두 동일한 상황에서 최단 거리 문제를 해결하기 위해서 사용 될 수 있음.

## 예제

graph = [[], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]
- 각 노드가 방문한 노드인지 여부를 표현. index 0은 사용하지 않음.
visited = [False] * 9

from collections import deque
- bfs 함수 정의
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = '')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
- bfs 함수 호출
bfs(graph, 1, visited)



