class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
       
        while root:
            if p.val > root.val and q.val > root.val:
                root= root.right
            elif p.val < root.val and q.val < root.val:
                root= root.left
            else:
                return root
        return None
    
        