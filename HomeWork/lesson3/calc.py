"""Напишите программу-калькулятор, которая поддерживает следующие операции:
сложение, вычитание, умножение, деление и возведение в степень.
Программа должна выдавать сообщения об ошибке и продолжать работу при вводе некорректных данных,
делении на ноль и возведении нуля в отрицательную степень.  """
import decimal
import sys


def addition(f_number, s_number):
    return f_number + s_number


def subtraction(f_number, s_number):
    return f_number - s_number


def multiplication(f_number, s_number):
    return f_number * s_number


def division(f_number, s_number):
    return f_number / s_number


def exponentiation(f_number, s_number):
    result = decimal.Decimal(0)
    result = pow(decimal.Decimal(f_number), decimal.Decimal(s_number))
    if result == decimal.Decimal('Infinity'):
        raise ZeroDivisionError
    return result


def operations(f_number, s_number, operation):
    match operation:
        case 0:
            print('quit')
            sys.exit()
        case 1:
            print('addition')
            print('{} + {} = {}'.format(f_number, s_number, addition(f_number, s_number)))
        case 2:
            print('subtraction')
            print('{} - {} = {}'.format(f_number, s_number, subtraction(f_number, s_number)))
        case 3:
            print('multiplication')
            print('{} * {} = {}'.format(f_number, s_number, multiplication(f_number, s_number)))
        case 4:
            print('division')
            try:
                print('{} * {} = {}'.format(f_number, s_number, division(f_number, s_number)))
            except ZeroDivisionError:
                print('----------------------------------------')
                print('error Zero Division')
                print('----------------------------------------')
                raise
        case 5:
            try:
                print('exponentiation')
                print('{} ^ {} = {}'.format(f_number, s_number, exponentiation(f_number, s_number)))
            except ZeroDivisionError:
                print('----------------------------------------')
                print('0 cannot be raised to a negative power')
                print('----------------------------------------')
                raise
            except decimal.Overflow:
                raise
        case _:
            raise ValueError


def main():
    while True:
        print('Calculator')
        try:
            first_number = float(input('First number: '))
            second_number = float(input('Second number: '))
            print('menu')
            print('1: (+) addition\n'
                  '2: (-) subtraction\n'
                  '3: (*) multiplication\n'
                  '4: (/) division\n'
                  '5: (^) exponentiation\n'
                  '0: quit\n')
            operations(first_number, second_number, int(input('choose operation: ')))
            break
        except (ValueError, ZeroDivisionError):
            print('----------------------------------------')
            print('incorrect value')
            print('----------------------------------------')
        except OverflowError:
            print('----------------------------------------')
            print('Result too large')
            print('----------------------------------------')
        except decimal.Overflow:
            print('----------------------------------------')
            print('Result too large')
            print('----------------------------------------')


if __name__ == '__main__':
    main()
