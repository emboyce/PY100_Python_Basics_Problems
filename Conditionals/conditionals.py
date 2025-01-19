import random
random_number = random.randint(0,1)

print("Yes!") if random_number == 1 else print("No")

weather = 'foggy'
if weather == 'sunny':
    print('It\'s a beautiful day!')
elif weather == 'rainy':
    print('Grab your umbrella')
else:
    print("Let's stay inside")

weather = 'j'
match weather:
    case 'sunny':
        print('It\'s a beautiful day!')
    case 'rainy':
        print('Grab your umbrella')
    case _:
        print("Let's stay inside")



