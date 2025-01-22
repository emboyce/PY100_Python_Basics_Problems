import random

def predict_weather():
    sunshine = random.choice(['True', 'False'])
    if sunshine == "True":
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()


pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'].append('bowser')
pets['dog'] += 'bowser'  # Testing - does not work

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}


info = {'name': 'Srdjan', 'age': 38, 'city': 'Rossland'}

print(info.get('cities', 'Default'))

if 'city' in info.keys():
    print(info['city'])
else:
    print('Unknown')


#import copy     Apparently this is not necessary
sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    # matrix.append(["-", "-", "-"])
    # matrix.append(copy.deepcopy(sub_list))
    matrix.append(sub_list.copy())

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

def find_maximum(numbers):
    if not numbers:
        return None
    max_number = float('-inf')
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2


def digit_product(str_num):
    digits = [int(n) for n in str_num]
    print(digits)
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0