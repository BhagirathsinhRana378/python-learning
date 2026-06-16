try:
    age = int(input('Age:'))
    income=444
    risk = income/age
    print(age)
    print(risk)
except ValueError:
    print('invalid value')
except ZeroDivisionError:
    print('unable to divide with zero')

    #we can you multiple except block to catch the error