class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inorder(arr: List[int], root: TreeNode):
            if root is None:
                return

            inorder(arr,root.left)
            arr.append(root.val)
            inorder(arr,root.right)
        
        arr=[]
        inorder(arr,root)
        return arr