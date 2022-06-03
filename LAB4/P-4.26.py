def Hanoi(n, of, to, carried):
    if n == 0:
        return
    Hanoi(n - 1, of, carried, to)
    print("Move disk", n, "from pole", of, "to pole", to)
    Hanoi(n - 1, carried, to, of)


n = 4
Hanoi(n, 'A', 'C', 'B')

