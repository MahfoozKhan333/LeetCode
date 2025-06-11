class Solution(object):
    from collections import deque

class Solution:
    def countStudents(self, students, sandwiches):
        result = len(students)
        count = Counter(students)

        for s in sandwiches:
            if count[s] > 0:
                result -= 1
                count[s] -= 1
            else:
                return result

        return result
        