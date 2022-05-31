import math

right_answer = 7 * math.pi ** 4 / 720


def n_member(n):  # n-ый член ряда
    return (-1) ** n / (n + 1) ** 4


def s(n):   # вычисление суммы первых n членов ряда
    s = 0
    for i in range(0, n):
        s += n_member(i)
    print(f"Сумма S{n} = {s}, математическое значение суммы ряда S = {right_answer}")


if __name__ == '__main__':
    for n in [5, 10, 50, 100, 1000]:
        s(n)
