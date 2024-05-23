'''
Calculator
--------------------------
'''

import os

def addition():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Addition')
    
    continue_calc = 'y'
    
    num_1 = float(input('Enter a number:'))
    num_2 = float(input('Enter another number: '))
    ans = num_1 + num_2
    values_entered = 2
    print(f'Current result: {ans}')
    
    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n): '))
        while continue_calc.lower() not  in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n): '))
            
        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        ans += num
        print(f'Current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def subtraction():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Subtraction')
    
    continue_calc = 'y'
    
    num_1 = float(input('Enter a number:'))
    num_2 = float(input('Enter another number: '))
    ans = num_1 - num_2
    values_entered = 2
    print(f'Current result: {ans}')
    
    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n): '))
        while continue_calc.lower() not  in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n): '))
            
        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        ans += num
        print(f'Current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def multiplication():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Multiplication')
    
    continue_calc = 'y'
    
    num_1 = float(input('Enter a number:'))
    num_2 = float(input('Enter another number: '))
    ans = num_1 ** num_2
    values_entered = 2
    print(f'Current result: {ans}')
    
    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n): '))
        while continue_calc.lower() not  in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n): '))
            
        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        ans *= num
        print(f'Current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def division():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Divison')
    
    continue_calc = 'y'
    
    num_1 = float(input('Enter a number:'))
    num_2 = float(input('Enter another number: '))
    ans = num_1 / num_2
    values_entered = 2
    print(f'Current result: {ans}')
    
    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n): '))
        while continue_calc.lower() not  in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n): '))
            
        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        ans /= num
        print(f'Current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def exponents():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Exponents')
    
    continue_calc = 'y'
    
    num_1 = float(input('Enter a number:'))
    num_2 = float(input('Enter another number: '))
    ans = num_1 ** num_2
    values_entered = 2
    print(f'Current result: {ans}')
    
    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n): '))
        while continue_calc.lower() not  in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n): '))
            
        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        ans **= num
        print(f'Current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def floor_division():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Floor_Division')
    
    continue_calc = 'y'
    
    num_1 = float(input('Enter a number:'))
    num_2 = float(input('Enter another number: '))
    ans = num_1 // num_2
    values_entered = 2
    print(f'Current result: {ans}')
    
    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n): '))
        while continue_calc.lower() not  in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n): '))
            
        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        ans //= num
        print(f'Current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def calculator():
    quit = False
    while not quit:
        results = []
        print('Simple Calculator in Python!')
        print('Enter \'a\' for addition')
        print('Enter \'s\' for subtraction')
        print('Enter \'m\' for multiplication')                                    
        print('Enter \'d\' for division')                                    
        print('Enter \'e\' for exponenets')
        print('Enter \'f\' for floor division')
        print('Enter \'q\' for quit')
        
        choice = input('Selection: ')
        
        if choice == 'q':
            quit = True
            continue
        
        if choice == 'a':
            results = addition()
            print('Ans = ', results[0], 'total inputs: ', results[1])
        elif choice == 's':
            results = subtraction()
            print('Ans = ', results[0], 'total inputs: ', results[1])
        elif choice == 'm':
            results = multiplication()
            print('Ans = ', results[0], 'total inputs: ', results[1])
        elif choice == 'd':
            results = division()
            print('Ans = ', results[0], 'total inputs: ', results[1])
        elif choice == 'e':
            results = exponents()
            print('Ans = ', results[0], 'total inputs: ', results[1])
        elif choice == 'f':
            results = floor_division()
            print('Ans = ', results[0], 'total inputs: ', results[1])
        else:
            print('Sorry, invalid character')
            
if __name__ == '__main__':
   calculator()                                               