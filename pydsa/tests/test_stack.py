from pydsa.stack import Stack


def test_stack():
    q = Stack()
    q.push(5)
    q.push(9)
    q.push(12)
    q.push(20)
    assert q.pop() == 20
    assert q.pop() == 12
    assert q.size() == 2
    assert q.pop() == 9
    assert q.pop() == 5
    assert q.is_empty() == True
