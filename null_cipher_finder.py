import sys
import string


def load_text(file):
    """Загрузите текстовый файл в виде строки."""
    with open(file) as f:
        return f.read().strip()


def solve_null_cipher(message, lookahead):
    """Решить нулевой шифр, основываясь на числе букв
        после знака препинания,
        message = текст нулевого шифра как цепочка символов без пробелов
        lookahead = конечная точка диапазона букв после знака препинания
    """
    for i in range(1, lookahead + 1):
        plaintext = ''
        count = 0
        found_first = False
        for char in message:
            if char in string.punctuation:
                count = 0
                found_first = True
            elif found_first is True:
                count += 1
            if count == i:
                plaintext += char
        print("Используя сдвиг {} после знака препинания = {}".format(i, plaintext))
        print()


def main():
    """Загрузите текст, разгадайте нулевой шифр."""
    # загрузить и обработать сообщение:
    filename = input("\nВведите полное имя файла для перевода сообщения: ")
    try:
        loaded_message = load_text(filename)
    except IOError as e:
        print("{}. Завершение программы.".format(e), file=sys.stderr)
        sys.exit(1)
    print("\nПЕРВОНАЧАЛЬНОЕ СООБЩЕНИЕ =")
    print("{}".format(loaded_message), "\n")
    print("\nСписок проверяемых знаков препинания = {}".
          format(string.punctuation), "\n")

    # удалить пробелы:
    message = ''.join(loaded_message.split())

    # получить от пользователя диапазон возможных ключей шифра:
    while True:
        lookahead = input("\nЧисло букв, проверяемых после " \
                          "знака препинания: ")
        if lookahead.isdigit():
            lookahead = int(lookahead)
            break
        else:
            print("Пожалуйства, введите число.", file=sys.stderr)
    print()

    # выполнить функцию декодирования шифра
    solve_null_cipher(message, lookahead)


if __name__ == '__main__':
    main()