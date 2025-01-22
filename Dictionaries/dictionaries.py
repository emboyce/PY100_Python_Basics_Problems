car = {
    "type": "sedan",
    "color": "blue",
    "mileage": 80000,
}

print(car)

#Dict keys must be immutable and hashable

car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
}

car['year'] = 2003
print(car)

car.pop('mileage')
print(car)
car.pop('mileage', None)

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

print(car['color'])
print(car.get('mileage'))

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

print(len(car.keys()))
print(len(car))

student = {
    'id': 123,
    'grade': 'B',
}

print(student.get('name'))
print(student.get('grade', None))
print('name' in student)

vehicle = {
    "Car": {
        'type': 'sedan',
        'color': 'blue',
        'year': 2003,
    },
    "Truck":
    {
       'type': 'pickup',
        'color': 'red',
        'year': 1998, 
    },
}

print(vehicle)
vehicle2 = {
    "car": car,
    "student": student,
}

print(vehicle2)

attributes = ['type', 'color', 'year']
car = ['sedan', 'blue', 2003]
truck = ['pickup', 'red', 1998]

car_dict = dict(zip(attributes, car))
truck_dict = dict(zip(attributes, truck))
full_dict = dict([('Car', car_dict), ('Truck', truck_dict)])

print(vehicle)
print(full_dict)
print(vehicle == full_dict)

print(list(zip(attributes, car)))
print(dict(zip(attributes, car)))

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

list_car = [
    ['type', 'sedan'],
    ['color', 'blue'],
    ['year', 2003],
    ]

print([list(item for item in car.items())])
ez_car = [list(item) for item in car.items()]
#I don't fully get this bit of code yet

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = []
# print(numbers.values())
for value in numbers.values():
    half_numbers.append(int(value/2))
print(half_numbers)

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for key, value in numbers.items():
    print(key, value)
    
