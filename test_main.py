from .main import BSTNode, insert, left_rotate, right_rotate

def test_insert():
    t = insert(None, 1)
    t = insert(t, 3)
    t = insert(t, 10)
    t = insert(t, 5)
    assert repr(t) == "1 3 5 10"

def test_left_rotate():
    t = BSTNode(1)
    t.right = BSTNode(2)
    t.right.right = BSTNode(2)
    t = left_rotate(t)
    assert t.data == 2
    assert t.left.data == 1
    assert t.right.data == 3
    assert t.height == 1

def test_right_rotate():
    t = BSTNode(2)
    t.left = BSTNode(1)
    t.right = BSTNode(3)
    t = right_rotate(t)
    assert t.data == 1
    assert t.height == 2
    assert t.left is None
    assert t.right.data == 2
    assert t.right.left is None
    assert t.right.right.data == 3
