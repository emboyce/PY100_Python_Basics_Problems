name = "Victor"
profession = "programmer"

print("Hello {}. You are a {}.".format("Eliza", profession))
print(f"Hello {name}. You are a {profession}.")

ice_cream_density = 10

while ice_cream_density > 0:
    print('Drip...')
    ice_cream_density -= 1

print('The ice cream melted.')

from datetime import datetime
print(datetime.now())

from datetime import date
today = date.today()
print(today)
print(today.year)
print(today.isocalendar())

alist = ["s","h","i","t"]
joinee = "p"
# I have no idea why the following doesn't throw an error
print(str.join("Aa", "Bb"))
# Apparently it's because it's calling join on the str class itself
# and in this case it uses the first argument as the iterator
# a weird behaviour to avoid using.

test_string = "Eliza is fantastic at coding"
is_string = "Aspen"
if is_string in test_string:
    print("Yes")
else:
    print("Nope")

speed_limit = 60
current_speed = 80

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')
    
tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + "5")