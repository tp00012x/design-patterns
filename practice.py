# Your list `x`
x = [1, 2, 3, 4, 5, 6, 7]

# Split `x` up in chunks of 3

print(*[iter(x)])

y = zip(*[x] * 2)

# Use `list()` to print the result of `zip()`
print(list(y))
