def solution(n):
    n = int(n)

    count = 0

    while (n != 1):
        if n == 3:
            count += 2
            break

        if not n & 1:
            n = n >> 1
            count += 1

        elif n & 2:
            n += 1
            count += 1

        else:
            n -= 1
            count += 1

    return count