class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        
                ###. RECURSIVE SOLUTION ###
        # def preorder(arr: List[int], root: TreeNode):
        #     if root is None:
        #         return

        #     arr.append(root.val)
        #     preorder(arr,root.left)
        #     preorder(arr,root.right)
        
        # arr=[]
        # preorder(arr,root)
        # return arr

                ###. ITERATIVE SOLUTION ###
        
        preorder = []
        if root is None:
            return preorder
        
        st = []
        st.append(root)

        while st:
            root = st.pop()
            preorder.append(root.val)
            if root.right:
                st.append(root.right)
            if root.left:
                st.append(root.left)
        
        return preorder