"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:            
        queue = [root]
        output = []
        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                output.append(node.val)
                if node.children:
                    queue = node.children + queue
        return output
