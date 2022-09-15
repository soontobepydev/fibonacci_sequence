# this file is supposed to show the fibonacci sequence only with recursion.
# for a more user friendly presentation of the fibonacci sequence there is 'src/fibonacci_sequence.py'
# only functionality and error handling is to be expected from this file

def fibonacci_recursion(n):
    if n < 2:
        return n
    if n == 2:
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
 

def main():
    n = 0
    while n != -1:
        try:
            n = int(input('enter N of the fibonacci sequence '))
            if n == -1:
                continue
        except:
            print('you must put a number between 0 and above')
        else:
            print(f'F[{n}]= {fibonacci_recursion(n)}')

if __name__ == '__main__':
    main()