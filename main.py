from typing import Callable

def counter(func: Callable):
    def inner(*args,**kwargs):
        inner.count += 1
        return func(*args, **kwargs)
    inner.count = 0
    return inner

@counter
def C(m: int, n: int) -> int:
    if m == n or m == 0:
        return 1
    return C(m, n - 1) + C(m - 1, n - 1)

def main() -> None:
    N = 8
    LIST_M = [7, 6, 5, 4, 3, 8]
    for m in LIST_M:
        assert N >= m, f"N({N}) должно быть >= M({m})"
        C.count = 0
        c = C(m=m, n=N)
        print(f"C({m}, {N}) = {c}; Количество рекурсивных вызовов функции C = {C.count - 1}")

if __name__ == "__main__":
    main()
