from typing import Optional
from re import split

class BSTNode:
    def __init__(self, data: int):
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None
        self.data = data

    @property
    def height(self) -> int:
        if self.left is None:
            lh = -1
        else:
            lh = self.left.height

        if self.right is None:
            rh = -1
        else:
            rh = self.right.height

        return max(lh, rh) + 1

    @property
    def balanced(self) -> int:
        if self.left is None:
            lh = -1
        else:
            lh = self.left.height

        if self.right is None:
            rh = -1
        else:
            rh = self.right.height

        return abs(lh - rh) <= 1

    def __repr__(self) -> str:
        r = []

        if self.left is not None:
            r += [self.left.__repr__()]

        r += [f"{self.data}"]

        if self.right is not None:
            r += [self.right.__repr__()]

        return " ".join(split("\\s+", " ".join(r)))

def insert(node: Optional[BSTNode], x: int) -> BSTNode:
    if node is None:
        return BSTNode(x)

    if x > node.data:
        node.right = insert(node.right, x)

        if not node.balanced and x > node.data and node.right is not None and x > node.right.data: # right-right case
            node = left_rotate(node)
            assert node is not None
        elif not node.balanced and x > node.data and node.right and x < node.right.data: # right-left case
            node.right = right_rotate(node.right)
            node = left_rotate(node)
            assert node is not None

        return node
    elif x < node.data:
        node.left = insert(node.left, x)

        if not node.balanced and x < node.data and node.left and x < node.left.data: # left-left case
            node = right_rotate(node)
            assert node is not None
        elif not node.balanced and x < node.data and node.left and x > node.left.data: # left-right case
            node.left = left_rotate(node.left)
            node = right_rotate(node)
            assert node is not None

        return node
    else:
        raise RuntimeError("can't tolerate duplicate key")

def delete(t: Optional[BSTNode], x: int) -> Optional[BSTNode]:
    if t is None:
        return t

    if t.data == x and t.left is None:
        t = t.right
    elif t.data == x:
        t = right_rotate(t)
        t = delete(t.right, x)
    elif x < t.data:
        t.left = delete(t.left, x)
    else:
        t.right = delete(t.right, x)

    if t is None:
        return t

    if t.left is None:
        lh = -1
    else:
        lh = t.left.height

    if t.right is None:
        rh = -1
    else:
        rh = t.right.height

    if lh - rh > 1: # left-heavy
        t = right_rotate(t)
    elif lh - rh < -1: # right-heavy
        t = left_rotate(t)

    return t

def right_rotate(y: Optional[BSTNode]):
    if y is None:
        return None

    if y.left is None:
        raise RuntimeError("right rotation is not defined is y.left is None")

    x = y.left
    y.left = x.right
    x.right = y

    return x

def left_rotate(x: Optional[BSTNode]):
    if x is None:
        return None

    if x.right is None:
        raise RuntimeError("left rotation is not defined is x.right is None")

    y = x.right
    x.right = y.left
    y.left = x

    return y

def search(t: Optional[BSTNode], x: int) -> bool:
    if t is None:
        return False

    if t.data == x:
        return True

    if x < t.data:
        return search(t.left, x)
    else:
        return search(t.right, x)

if __name__ == "__main__":
    pass
