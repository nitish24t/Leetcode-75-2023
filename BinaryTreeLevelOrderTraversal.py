class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        output_arr = [[root.val]]
        queue = [root]
        height = 0

        while queue:
            length = len(queue)
            index_arr = []
            while length > 0:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    index_arr.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    index_arr.append(node.right.val)
                length -= 1
                # print("ht:{0} \t node:{1}".format(height,node.val))
            height += 1
            if len(index_arr):
                output_arr.insert(height, index_arr)
        return output_arr
      
      
"""
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]


Example 2:

Input: root = [1]
Output: [[1]]


Example 3:

Input: root = []
Output: []
"""
