def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    print('How much Fibonacci numbers do you want?')
    n = int(input('>>> '))
    for fib_num in fibonacci_sequence(n):
        print(fib_num, end=' ')
    print()

if __name__ == '__main__':
    main()
