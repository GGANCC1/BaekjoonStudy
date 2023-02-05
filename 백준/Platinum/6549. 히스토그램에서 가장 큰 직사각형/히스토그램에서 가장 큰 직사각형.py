import sys
sys.setrecursionlimit(10**5)


def merge(left, right):
    if arr[left] < arr[right]:
        return left
    return right


def initTree(node, nodeLeft, nodeRight):
    if nodeLeft == nodeRight:
        tree[node] = nodeLeft
        return tree[node]
    mid = nodeLeft + (nodeRight - nodeLeft) // 2
    leftVal = initTree(node * 2, nodeLeft, mid)
    rightVal = initTree(node * 2 + 1, mid + 1, nodeRight)
    tree[node] = merge(leftVal, rightVal)
    return tree[node]


def query(left, right, node, nodeLeft, nodeRight):
    if right < nodeLeft or nodeRight < left:
        return inf
    if nodeLeft >= left and right >= nodeRight:
        return tree[node]
    mid = nodeLeft + (nodeRight - nodeLeft) // 2
    leftidx = query(left, right, node * 2, nodeLeft, mid)
    rightidx = query(left, right, node * 2 + 1, mid + 1, nodeRight)
    if leftidx == inf:
        return rightidx
    elif rightidx == inf:
        return leftidx
    else:
        return merge(leftidx, rightidx)


def sol(i, j):
    idx = query(i, j, 1, 1, n)
    maximum = (j - i + 1) * arr[idx]
    if idx < j:
        maximum = max(maximum, sol(idx + 1, j))
    if i < idx:
        maximum = max(maximum, sol(i, idx - 1))
    return maximum


inf = sys.maxsize
while True:
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    if arr[0] == 0:
        break
    n = len(arr) - 1
    tree = [0] * (4 * n + 1)
    initTree(1, 1, n)
    print(sol(1, n))
