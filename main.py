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
        return node
    elif x < node.data:
        node.left = insert(node.left, x)
        return node
    else:
        raise RuntimeError("can't tolerate duplicate key")

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

if __name__ == "__main__":
    pass
