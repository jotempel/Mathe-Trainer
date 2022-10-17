import random


def get_random_numbers(x_lower, x_upper, y_lower, y_upper):
    x = random.randint(x_lower, x_upper)
    y = random.randint(y_lower, y_upper)
    return x, y


def is_a_number(n):
    try:
        int(n)
        return True
    except:
        return  False


max_multiplier = 10
max_denominator = 10
max_numerator = 100

number_of_exercises = 10
correct_counter = 0
false_counter = 0

try:
    r = input('Wie viele Aufgaben möchtest du rechnen? ')
    while not is_a_number(r) or is_a_number(r) and int(r) <= 0:
            print('Falsche Eingabe! Du musst eine Zahl größer 0 eingeben.')
            r = input('Wie viele Aufgaben möchtest du rechnen? ')
    number_of_exercises = int(r)
    
    for i in range(number_of_exercises):
        
        arithmetic_operation = random.randint(1, 2)
    
        if arithmetic_operation == 1:    
            x, y = get_random_numbers(1, max_multiplier, 1, max_multiplier)
            correct_result = x * y
            print(x, ' * ', y, '=' )
        else:
            x, y = get_random_numbers(1, max_denominator, 1, max_numerator)
            while x % y != 0:
                x, y = get_random_numbers(1, max_denominator, 1, max_numerator)
            correct_result = x / y
            print(x, ' : ', y, '=' )

        r = input('Deine Antwort:')
        while not is_a_number(r) or is_a_number(r) and int(r) <= 0:
            print('Falsche Eingabe! Du musst eine Zahl größer 0 eingeben.')
            r = input('Deine Antwort:')
        result = int(r)
        if result == correct_result:
            print('Richtig!')
            correct_counter += 1
        else:
            print('Falsch! Die richtige Antwort ist ', correct_result)
            false_counter += 1
        print('\n')
except:
    print('Abbruch.')
print('Du hast ' + str(correct_counter + false_counter) + ' von ' + str(number_of_exercises) + ' beantwortet,\n')
print('davon hast du ' + str(correct_counter) + ' Aufgaben richtig und ' + str(false_counter) + ' falsch gerechnet.')
