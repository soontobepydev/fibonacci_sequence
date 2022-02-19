import random
import math

def get_greetings_from_file():
    file_path = 'src\greetings.txt'
    with open(file_path) as file:
        greetings = file.readlines()
    return greetings
    
def greet():
    greetings = get_greetings_from_file()
    print(random.choice(greetings))

def get_fibonacci(n):
    Phi = (1 + math.sqrt(5))/2
    phi = (1 - math.sqrt(5))/2
    try:
        return n if n <= 2 else round( ((Phi  ** n) - (phi ** n ) )/ math.sqrt(5) ) 
    except:
        raise Exception('number is too big')


def main():
    greet()
    n = 0

    while (n != -1):
        print("what's the n number in the fibonacci sequence you want to see")
        print('type a number between 0 and 1. Insert -1 to end')
        print()
        try:
            n =int(input('N = '))
            if(n == -1):
                continue
        except:
            print()
            print('you must provide an integer number from 0 and above')
            print()
        else:
            try:
                print(f'F[{n}]={get_fibonacci(n)}')
            except Exception as error:
                print(error)


        
if __name__ == '__main__':
    main()