def sum(n):
    if n:
        return n+sum(n-1)
    else:
        return 0
print(sum(10))