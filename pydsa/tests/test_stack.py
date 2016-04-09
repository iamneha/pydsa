from pydsa.stack import stack


def test_stack():
    q = stack()
    q.push(5)
    q.push(9)
    q.push(12)
    q.push(20)
    assert q.pop() == 20
    assert q.pop() == 12
    assert q.size() == 2
