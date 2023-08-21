def remainder_division(a, b):
    if b==0:
        raise ZeroDivisionError
    if b==1:
        raise Exception('Division identity, divide by 1. Answer is:', a)
    result = a//b
    remainder = a%b
    print(a, '/', b, 'is', result, 'remainder', remainder)

try:
    remainder_division(10, 1)
except ZeroDivisionError:
    print("Error: Attempted to divide by zero.")
except:
    print("Generic error")