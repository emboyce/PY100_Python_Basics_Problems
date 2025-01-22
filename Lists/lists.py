def first(lst):
    if not lst:
        return None
    else:
        return lst[0]

def alt_first(lst):
    return (None if not lst else lst[0])

print(alt_first(['Aspen']))
print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))  # None

def last(lst):
#    return (lst[len(lst)-1] if lst else None)
    return (lst[-1] if lst else None)

print(last(['Earth', 'Moon', 'Mars']))  # Mars

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
energy.pop(0)
energy.append('geothermal')
print(energy)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
al_list = []
al_list += alphabet
print(al_list)

scores = [96, 47, 113, 89, 100, 102]
count = 0
for score in scores:
    if score >= 100: count += 1
print(count)

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

for item in vocabulary:
    for sub_item in item:
        print(sub_item)

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'
print(isinstance(some_value2, list))

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(place, lst):
    for item in lst:
        if place == item: return True
    return False

print("Travel")
print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False

def contains1(place, lst):
    return place in lst

print(contains1('Barcelona', destinations))  # True
print(contains1('Nashville', destinations))  # False

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

code = "-".join(passcode)
print(code)

# Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

while grocery_list:
    print(grocery_list.pop(0))

print(grocery_list)