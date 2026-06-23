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

# shorter and easier and better syntax
with open('youtube. txt', 'w') as file:
    file.write('chai aur python')
#we can you multiple except block to catch the error