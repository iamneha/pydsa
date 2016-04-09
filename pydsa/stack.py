class stack(object):
    """
    >>> from pydsa import stack
    >>> q = stack()
    >>> q.push(9)
    >>> q.push(90)
    >>> q.push(19)
    >>> q.push(1)
    >>> q.size()
    4
    >>> q.pop()
    1
    >>> q.pop()
    19
    """
    def __init__(self):
        self.List = []

    def isEmpty(self):
        return self.List == []

    def push(self, item):
        """
        Insert element in stack.
        """
        self.List.append(item)

    def pop(self):
        """
        Remove element which inserted last in stack.
        """
        return self.List.pop()

    def size(self):
        """
        Return size of stack.
        """
        return len(self.List)
