# 2024-8-17
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return

        dq = deque([node])
        clone = {}
        visited = {}
        visited[node] = Node(node.val)

        while dq:
            for i in range(len(dq)):
                cur = dq.popleft()
                for neighbor in cur.neighbors:
                    if neighbor not in visited:
                        visited[neighbor] = Node(neighbor.val)
                        dq.append(neighbor)
                    visited[cur].neighbors.append(visited[neighbor])

        return visited[node]