class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t:t[0])
        res=[]
        mheap=[]
        i,time=0,tasks[0][0]

        while mheap or i<len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(mheap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not mheap:
                time=tasks[i][0]
            else:
                p,idx=heapq.heappop(mheap)
                time+=p
                res.append(idx)
        return res