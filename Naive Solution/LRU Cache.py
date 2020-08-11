'''
    Runtime:
        time: O(1), get() utilizing dict for retrieving and updating keys takes O(1). put uses linked list that
        takes O(1)
        space: O(capacity)
    Analysis: 
        Given: info regarding the LRU cache, such as capacity, put(elements), get(elements)
        Ask: implement a LRU
        To accomplish this: when taking about O(1) for retrieving info, a dict would be a good choice. but dict only 
        solves half the problem, since we also need to find a way to implement put(). Dict itself would not suffice 
        because its unordered structure. Follow this train of thought, we need a way to quickly add a node to an 
        arbitrary location during put(), in this case a doubly linked list is a good choice, of which each node keeps
        info of its previous and next node, to relocate a node, one simply needs to assign its pre and next to desired
        nodes. 
    
'''
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = node()
        self.tail = node()
        self.head.nex = self.tail
        self.tail.pre = self.head
        self.cache = {}
        self.storage = 0
        
    def move_to_tail(self, node):
        self.tail.pre.nex = node
        node.pre = self.tail.pre
        self.tail.pre = node
        node.nex = self.tail
        
    def delete_node(self, node):
        node.pre.nex = node.nex
        node.nex.pre = node.pre
        node.pre = None
        node.nex = None
        return node

    def get(self, key: int) -> int:
       
        if self.cache.get(key, None) is not None:
            # reorder position of called node
            temp = self.delete_node(self.cache.get(key))
            self.move_to_tail(temp)
            # return value
            return temp.val
        else:
            # not found
            return -1

    def replace(self, node, val):
        node.val = val
        return node
        
    def put(self, key: int, value: int) -> None:
        # check if key already exists, if so, update its value
        if self.cache.get(key, None):
            # update value
            temp = self.replace(self.cache.get(key), value)
            # reorder the linked list
            temp = self.delete_node(temp)
            self.move_to_tail(temp)
        # if key not in linked list
        else:
            # construct the node to be added
            nd = node(key, value)
            # if within capacity
            if self.storage < self.capacity:
                # increment storage
                self.storage += 1

            else:
                # remove the first node
                temp = self.delete_node(self.head.nex)
                # remove in cache
                self.cache.update({temp.key: None})
            # add new node to tail
            self.move_to_tail(nd)
            # add to cache
            self.cache.update({key: nd})
            
# a node class for constructing doubly linked list
class node:
    def __init__(self, key=None, val=None, pre=None, nex=None):
        self.key = key
        self.val = val 
        self.pre = pre
        self.nex = nex
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
