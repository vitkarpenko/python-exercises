import string
import random


def main():
    symbols = ''.join([string.ascii_lowercase,
                      string.ascii_uppercase,
                      string.digits,
                      string.punctuation])
    length = random.randint(8, 24)
    print(''.join([random.choice(symbols) for _ in range(length)]))


if __name__ == '__main__':
    main()
