class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def postorder(arr: List[int], root: TreeNode):
            if root is None:
                return

            postorder(arr,root.left)
            postorder(arr,root.right)
            arr.append(root.val)
        
        arr=[]
        postorder(arr,root)
        return arr