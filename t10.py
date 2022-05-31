def func(x):  # анализируемая функция
    return 3 * x ** 4 + 2 * x ** 3 - 3 * x ** 2 - 2


def tab(x, h, xn):  # табулирование
    fs = []
    while x <= xn:
        fs.append(func(x))
        x += h
    return fs


def main(x0, h, xn):  # подсчет отрицательных и положительный значений
    fs = tab(x0, h, xn)
    neg = 0
    pos = 0
    for f in fs:
        if f > 0:
            pos += 1
        elif f < 0:
            neg += 1
    if neg > pos:
        print("Отрицатальных больше")
    elif neg < pos:
        print("Положительных больше")
    else:
        print("Равное количество отрицательных и положительных")


if __name__ == '__main__':
    main(0, 0.5, 5)
