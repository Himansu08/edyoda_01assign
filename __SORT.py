n = int(input().strip())
strings = [input().strip() for _ in range(n)]
strings.sort(key=lambda x: x[-2])
print(*strings)   