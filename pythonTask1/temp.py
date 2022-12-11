from collections import deque

c = int(input())
n = int(input())
w = list(map(int, input().split()))
pre = [-1] * sum(w)
path = [0] * n
resp = 0
idx = 0


def bfs():
    global resp, idx
    queue = deque()
    queue.append(0)
    queue.append(-1)
    while queue:
        eq = queue.popleft()

        if idx == n:
            resp = max(resp, eq)
            continue

        if eq != -1:
            queue.append(eq)
            if w[idx] + eq <= c:
                pre[eq + w[idx]] = eq
                queue.append(eq + w[idx])

        if eq == -1 and idx != n:
            idx += 1
            queue.append(-1)


def main():
    global resp
    bfs()
    print(f"最大装载量为: {resp}")
    while pre[resp] != -1:
        path[w.index(resp - pre[resp])] = 1
        resp = pre[resp]
    print(f"路径为：{path}", end="")


if __name__ == "__main__":
    main()
