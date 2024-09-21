class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def preorder(arr: List[int], root: TreeNode):
            if root is None:
                return

            arr.append(root.val)
            preorder(arr,root.left)
            preorder(arr,root.right)
        
        arr=[]
        preorder(arr,root)
        return arr