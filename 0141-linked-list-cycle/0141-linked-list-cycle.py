class Solution(object):
    def hasCycle(self, head):
        single_step = head
        double_step= head

        while double_step is not None and double_step.next is not None:
            single_step = single_step.next
            double_step = double_step.next.next
            if single_step == double_step:
                return True  

        return False  
        