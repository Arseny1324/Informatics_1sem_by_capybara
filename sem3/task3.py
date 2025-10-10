import sys

def extended_gcd(a, b):
    if b == 0:
        return 1, 0, a
    x1, y1, d = extended_gcd(b, a % b)
    return y1, x1 - (a // b) * y1, d

def best_xy(a, b):
    x0, y0, d = extended_gcd(a, b)
    if d == 0:  # на всякий случай
        return 0, 0, 0
    step_x = b // d
    step_y = a // d

    best_x, best_y = x0, y0
    best_val = abs(x0) + abs(y0)

    # Найдём оптимальное k аналитически (точно!)
    # Минимизируем |x0 + k*step_x| + |y0 - k*step_y|
    # Простой способ — проверить k около точек излома
    candidates = set()
    if step_x != 0:
        candidates.add(round(-x0 / step_x))
    if step_y != 0:
        candidates.add(round(y0 / step_y))
    candidates.update([0, -1, 1])

    for k in candidates:
        x = x0 + k * step_x
        y = y0 - k * step_y
        val = abs(x) + abs(y)
        if val < best_val or (val == best_val and x < best_x):
            best_x, best_y, best_val = x, y, val

    return best_x, best_y, d

# Чтение ввода
for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    a, b = map(int, line.split())
    x, y, d = best_xy(a, b)
    print(x, y, d)