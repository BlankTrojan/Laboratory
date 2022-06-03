def minmax(n, min=None, max=None):

    x, *y = n

    if min is None:
        min = [x]
    elif x < min[-1]:
        min.append(x)

    if max is None:
        max = [x]
    elif x > max[-1]:
        max.append(x)

    if y:
        return minmax(y, min, max)

    return min.pop(), max.pop()

if __name__ == "__main__":

    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 16, 16]
    min, max = minmax(n)
    print(min, max)
