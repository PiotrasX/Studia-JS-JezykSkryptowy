def newton(n, k):
    if k == 0 or k == n:
        return 1
    if 0 < k < n:
        return newton(n - 1, k - 1) + newton(n - 1, k)
    else:
        return "Liczba 'k' musi zawierać się w przedziale <0,n>"


print(newton(7, 2))
print(newton(7, 5))
print(newton(7, 7))
print(newton(7, 9))
