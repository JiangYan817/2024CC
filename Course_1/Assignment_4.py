##网络延迟时间
#有 n 个网络节点，标记为 1 到 n。
#给你一个列表 times，表示信号经过有向边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。
#现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        weight = collections.defaultdict(dict)
        for u, v, w in times:
            weight[u][v] = w
        heap = [(0, k)]
        dist = {}
        while heap:
            time, u = heapq.heappop(heap)
            if u not in dist:
                dist[u] = time
                for v in weight[u]:
                    heapq.heappush(heap, (dist[u] + weight[u][v], v))
        return max(dist.values()) if len(dist) == n else -1



