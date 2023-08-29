n, m = map(int, input().split())

answer = []
tmp = []
def combination(current):
    if len(tmp) == m:
        print(tmp)
        tmp.sort()
        if tmp not in answer:
            answer.append(tmp[:])
        return
     
    for a in range(current, n+1):
        tmp.append(a)
        combination(current)
        tmp.pop()

combination(1)

print(answer)