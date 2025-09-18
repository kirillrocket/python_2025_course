arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def sq(a: int, b: int) -> int:
    return min(arr[b], arr[a]) * (b-a)


a = 0
b = len(arr) - 1
mx = sq(a, b)

while a != b:
    if sq(a + 1, b) > sq(a, b):
        if sq(a + 1, b) > mx:
            mx = sq(a + 1, b)
        a += 1
    elif sq(a, b - 1) > sq(a, b):
        if sq(a, b - 1) > mx:
            mx = sq(a, b - 1)
        b -= 1
    else:
        if arr[a] > arr[b]:
            a += 1
        else:
            b -= 1
print(mx)
