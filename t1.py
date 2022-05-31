def func(x):  # анализируемая функция
    return 3 * x ** 4 + 2 * x ** 3 - 3 * x ** 2 - 3


def tab(x, h, xn):  # табулирование
    fs = []
    while x <= xn:
        fs.append(func(x))
        x += h
    return fs


def main(x0, h, xn):  # подсчет отрицательных и положительный значений
    fs = tab(x0, h, xn)
    print(f"Значения: {fs}")
    neg = 0
    pos = 0
    for f in fs:
        if f > 0:
            pos += 1
        elif f < 0:
            neg += 1
    if neg > pos:
        print("Отрицательных больше")
    elif neg < pos:
        print("Положительных больше")
    else:
        print("Равное количество отрицательных и положительных")


if __name__ == '__main__':
    x0, h, xn = -1, 0.5, 5
    print(f"x0: {x0}, h: {h}, xn: {xn}")
    main(x0, h, xn)
