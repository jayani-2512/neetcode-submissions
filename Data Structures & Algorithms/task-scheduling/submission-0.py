class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=Counter(tasks)
        mheap=[-x for x in c.values()]
        heapq.heapify(mheap)
        time=0
        q=deque()
        while q or mheap:
            time+=1
            if not mheap:
                time=q[0][1]
            else:
                c=1+heapq.heappop(mheap)
                if c:
                    q.append([c,time+n])
            if q and q[0][1]==time:
                heapq.heappush(mheap,q.popleft()[0])
        return time
