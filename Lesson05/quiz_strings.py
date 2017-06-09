def bigger(a, b):
    if a > b:
        return a
    else:
        return b


def biggest(a, b, c):
    return bigger(a, bigger(b, c))


def smaller(a, b):
    if a < b:
        return a
    else:
        return b


def smallest(a, b, c):
    return smaller(a, smaller(b, c))

print(smallest(1, 2, 3))