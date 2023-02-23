import sys


def merge(left, right):
    if left == 0:
        return right
    elif right == 0:
        return left
    else:
        return [min(left[0], right[0]), max(left[1], right[1])]


def initTree(node, nodeLeft, nodeRight):
    if nodeLeft == nodeRight:
        tree[node] = [arr[nodeLeft], arr[nodeRight]]
        return tree[node]
    mid = nodeLeft + (nodeRight - nodeLeft) // 2
    leftVal = initTree(node * 2, nodeLeft, mid)
    rightVal = initTree(node * 2 + 1, mid + 1, nodeRight)
    tree[node] = merge(leftVal, rightVal)
    return tree[node]


def query(left, right, node, nodeLeft, nodeRight):
    if right < nodeLeft or nodeRight < left:
        return 0
    if nodeLeft >= left and right >= nodeRight:
        return tree[node]
    mid = nodeLeft + (nodeRight - nodeLeft) // 2
    return merge(query(left, right, node * 2, nodeLeft, mid),
                 query(left, right, node * 2 + 1, mid + 1, nodeRight))


def sol(i, j):
    result = query(i, j, 1, 1, N)
    return result


N, M = map(int, sys.stdin.readline().split())
arr = [0] + [int(sys.stdin.readline().rstrip()) for _ in range(N)]
tree = [0] * (4 * N + 1)
initTree(1, 1, N)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(" ".join(map(str, sol(a, b))))


