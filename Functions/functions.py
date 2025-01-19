def multiply(num1, num2):
    return num1 * num2

print(multiply(12, 4))      # 48

def bruce_eckel_quote():
    print("Python is executable pseudocode")

bruce_eckel_quote()

def cite(author, quote):
    print(f'{author} said: "{quote}"')
    print('{} said: "{}"'.format(author, quote))

cite('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."

def squared_number(num):
    return num**2

print(squared_number(3))   # 9

def compare_by_length(str1, str2):
    if len(str1) < len(str2):
        return -1
    elif len(str2) < len(str1):
        return 1
    else:
        return 0


print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0

captain = "Captain Ruby"
print(captain.replace("Ruby", "Python"))

new_captain = "Captain Ruby"
new_captain = new_captain[0:8]
print(new_captain + "Python")

split_cap = "Captain Ruby"
list_cap = "Captain Ruby".split(" ")
list_cap.pop()
list_cap.append("Python")
print(" ".join(list_cap))

print('Captain Ruby'.split(' ')[0] + " Python")

def greet(lang):
    match lang:
        case 'en':
            return "Hi!"
        case 'fr':
            return "Salut!"
        case _:
            return "I'm sorry I don't speak that language."
        

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!

def extract_language(locale):
    return locale[0:2]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

def extract_region(locale):
    return (locale.split("_")[1])[0:2]

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR

def local_greet(locale):
    return greet(extract_language(locale))

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('fr_GB.UTF-8'))       # Hello!
print(local_greet('pt_AU.UTF-8'))       # Howdy!
