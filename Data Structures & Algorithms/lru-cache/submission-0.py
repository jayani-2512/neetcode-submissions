class ListNode:
    def __init__(self,key,val,n,p):
        self.key,self.val,self.next,self.prev=key,val,n,p

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.hashmap={}
        self.left=ListNode(0,0,None,None)
        self.right=ListNode(0,0,None,self.left)
        self.left.next=self.right

    def remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev

    def insert(self,node):
        prev=self.right.prev
        nxt=self.right
        prev.next=node
        nxt.prev=node
        node.prev=prev
        node.next=nxt

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        self.hashmap[key]=ListNode(key,value,None,None)
        self.insert(self.hashmap[key])

        if len(self.hashmap)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]
