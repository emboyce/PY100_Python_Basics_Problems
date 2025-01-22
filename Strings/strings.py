print(len(f"These aren't the droids you're looking for."))

str1 = "confetti floating everywhere"
str2 = str1.upper()
# str2 = str1.casefold()
# I was testing how this worked. It's for comparisons not coversion.
print(str2)

name = 'Roger'
str3 = "RoGeR"
str4 = "DAVE"
if str3 == name:
    print('true')
else:
    print('false')

if name.casefold() == str3.casefold():
    print('true')
else:
    print('false')

print(name.casefold() == 'RoGeR'.casefold())

long_rhyme = "A pirate I was meant to be!\nTrim the sails and roam the sea!"
long_rhyme = '''
A pirate I was meant to be!
Trim the sails and roam the sea!
'''
print(long_rhyme)

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
if "x" in char_sequence:
    print(True)
else:
    print(False)

print(True) if "x" in char_sequence else print(False)

def is_empty0(str):
    if len(str) == 0:
        return True
    else:
        return False

def is_empty1(s):
    return s == ''

def is_empty2(s):
    return len(s) == 0

def is_empty(s):
    return not s

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

def is_empty_or_blank(s):
    print(f"Spaces? {s.isspace()}")
    print(f"Empty? {not s}")
    return s.isspace() or not s

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

str = 'launch school tech & talk'
print(str.title())

def starts_with0(str, prefix):
    return str.startswith(prefix)


def starts_with(str, prefix):
    if str.find(prefix) >= 0:
        if str[:len(prefix)] == prefix:
            return True
        
    return False

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

def count_substrings0(str, sub_str):
    return str.count(sub_str)

def count_substrings(str, sub_str):
    count = 0
    while True:
        #print(str)
        location = str.find(sub_str)
        if location == -1:
            return count
        else:
            count += 1
            start = location
            end = location + len(sub_str)
            #print(start, end)
            if start > 0:
                str = str[0:start] + str[end:]
            else:
                str = str[len(sub_str):]
            #print(str)   

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0
print(count_substrings("launchylaunch", "launch")) # 0

def count_substrings3(string, pattern):
    index = 0
    count = 0
    while index < len(string):
        if string[index:index+len(pattern)] == pattern:
            count += 1
            index += len(pattern)
        else:
            index += 1
    return count

print(count_substrings3("lll", "ll")) # 3
