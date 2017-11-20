# 采用简单的深度遍历
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution(object):
    s = 0
    es = None

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        self.es = employees
        for e in employees:
            if e.id == id:
                self.dsf(e)
        return self.s

    def dsf(self, employee):
        self.s += employee.importance
        for e in employee.subordinates:
            for item in self.es:
                if e == item.id:
                    self.dsf(item)