for num in range(0, 11, 2):
    print(num)

for i in range(10, 0, -1):
    print(i)
print("Launch!")

greeting = 'Aloha!'
i = 0
while i < 3:
    print(greeting)
    i += 1

for i in range(1, 101):
    print(i * 2)

lst = [1, 3, 7, 15]
index = 0
while index < 4:
    print(lst[index])
    index += 1

friends = ['Sarah', 'John', 'Hannah', 'Dave']
for friend in friends:
    print(f"Hello, {friend}!")

cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city is None:
        continue
    else:
        print(len(city))

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']
for fish in fish_list:
    if fish == "Nemo":
        print(fish)
        break
    
    print(fish)

while True:
    print('Should I stop looping?')
    answer = input()
    if answer == "yes":
        break


