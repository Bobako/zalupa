import sys


def print_head(length, path):   # вывод строк из файла или stdin
    text = ""
    if path:
        try:
            with open(path, "r") as file:
                for i in range(length):
                    text += file.readline()
        except FileNotFoundError:
            print("Файл не найден")
            return
    else:
        for i in range(length):
            text += input() + "\n"
    print(text)


def parse_args():  # получение аргументов командной строки
    length = 10
    path = ""
    for arg in sys.argv[1:]:
        if arg[0] == "-":
            try:
                length = int(arg[1:])
            except Exception:
                print("Некорректный аргумент")
                return None
        else:
            path = arg
    return length, path


if __name__ == '__main__':
    args = parse_args()
    if args:
        print_head(*args)
