import random


def main():
    with open('sowpods.txt') as sowpods:
        words = random.choice(sowpods.readlines())
    print(words)


if __name__ == '__main__':
    main()
