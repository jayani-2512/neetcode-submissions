class Twitter:

    def __init__(self):
        self.count=0
        self.followmap=defaultdict(set)
        self.tweet=defaultdict(list)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        mheap=[]
        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:
            if followeeId in self.tweet:
                idx=len(self.tweet[followeeId])-1
                c,t=self.tweet[followeeId][idx]
                mheap.append([c,t,followeeId,idx-1])
        heapq.heapify(mheap)
        while mheap and len(res)<10:
            c,t,followeeId,idx=heapq.heappop(mheap)
            res.append(t)
            if idx>=0:
                c, t =self.tweet[followeeId][idx]
                heapq.heappush(mheap,[c,t,followeeId,idx-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
            
        
