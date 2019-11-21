#fibonacci.py

def fib():
    fibs=[1,2]
    for i in range(1,9):
        fibs.append(fibs[i-1]+fibs[i])
    return fibs
def main():
    print('OUTPUT', fib())

if __name__ == '__main__':
    main()
