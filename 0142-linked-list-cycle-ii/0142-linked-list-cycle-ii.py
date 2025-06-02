class Solution(object):
    def detectCycle(self, head):
        visited = set()
        current= head

        while current:
            if current in visited:
                return current
            visited.add(current)
            current= current.next
        return None
        