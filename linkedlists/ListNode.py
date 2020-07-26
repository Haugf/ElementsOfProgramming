class ListNode:
    
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
    
    # Iterate through list until we find key, if we found key return null
    def search_list(self, L, key):
        while L and L.data != key:
            L = L.next
        return L 
    
    #Insert a a node after any specificed node
    def insert_after(self, node, new_node):
        new_node.next = node.next
        node.next = new_node
    
    def delete_after(self, node):
        node.next = node.next.next
            



List = ListNode(5, None)
