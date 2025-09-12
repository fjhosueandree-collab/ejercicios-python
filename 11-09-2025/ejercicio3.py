def sum(*args):
    valor = 0
    for n in args:
        valor += n
    return valor

print(sum(10, 3))        # Output: 13
print(sum(1, 2, 3))      # Output: 6
print(sum(3, 2, 4, 1))   # Output: 10
print(sum())             # Output: 0
