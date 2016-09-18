def composition(f, g):
    return lambda x: f(g(x))


def __or__(self, other):
    return composition(other, self)


a = lambda x: 2 * x
b = lambda x: x + 1

print((composition(a, b))(2))
print((__or__(a, b))(2))
print((a | b)(2))
