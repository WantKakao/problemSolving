n = int(input())

m = int(n ** 0.5)
if m ** 2 == n:
    print(1)
else:
    is_found = False
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            if i ** 2 + j ** 2 == n:
                print(2)
                is_found = True
                break
        if is_found:
            break

    if not is_found:
        for i in range(1, m + 1):
            for j in range(1, m + 1):
                for k in range(1, m + 1):
                    if i ** 2 + j ** 2 + k ** 2 == n:
                        print(3)
                        is_found = True
                        break
                if is_found:
                    break
            if is_found:
                break

    if not is_found:
        print(4)