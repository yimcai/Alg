import numpy as np 
from functools import total_ordering
from queue import PriorityQueue

@total_ordering
class Participant(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def __repr__(self,):
        return " ".join([self.firstname, self.lastname])

    def __eq__(self, other):
        return ((self.firstname, self.lastname) == (other.firstname, other.lastname))

    def __lt__(self, other):
        return ((self.firstname, self.lastname) < (other.firstname, other.lastname))
if __name__ == "__main__":
    q = PriorityQueue()
    q.put(Participant("Alice", "Tanya"))
    q.put(Participant("John", "Snow"))
    q.put(Participant("Bob", "Sula"))
    while not q.empty():
        print(q.get())



