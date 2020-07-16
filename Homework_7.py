# 14.18
my_dict = {}

#14.19
"""
d = {'john': 1, 'peter': 3}  
"""

#14.20
"""
dict = {'key': value}
"""

# 14.21
'''
(a) sets key 'susan' equal to 5
(b) sets key 'peter' equal to 5
(c) increments key 'peter' by 5
(d) deletes 'key' and 'value' of key 'peter' from dictionary
'''

# 14.22
'''
(a) Prints number of 'key-value' pairs in the dictionary
(b) Prints all 'keys' of the dictionary
(c) Prints all 'values' of the dictionary
(d) Prints all 'keys' and their 'value' of the dictionary
'''

# 14.23
def main_1():
    d = {'red': 4, 'blue': 1, 'green': 14, 'yellow': 2}
    print(d['red'])
    print(list(d.keys()))
    print(list(d.values()))
    print('blue' in d)
    print('purple' in d)
    d['blue'] += 10
    print(d['blue'])
main_1()

# 14.24
def main_2():
    d = {}
    d['susan'] = 50
    d['jim'] = 45
    d['joan'] = 54
    d['susan'] = 51
    d['john'] = 53
    print(len(d))
main_2()

# 14.25 
'''
    For a dictionary 'd', 
        d[key] returns the value for the key by address (meaning it can be changed) 
        and returns a KeyError if the key we want is missing from dictionary d
        d.get(key) returns the value for the key by function call (which cannot be assigned a value)
        and returns None if the key we want is missing from dictionary d
'''

d = {'red': 12}

print('key red is:', d['red'])
d['red'] = 15
print('key red is:', d['red'])
try:
    d['blue']
except KeyError:
    print('KeyError')

print('key red is:', d.get('red'))
print(type(d.get('blue')))


# 14.5 Dictionary to store value counts of words in a long text
def wordcount(f):
    lines = [line.replace('\n', '').lower().split() for line in f]
    words = [word for line in lines for word in line]
    counts = {}
    for each in set(words):
        counts[each] = words.count(each)
    return counts

f = open(r'C:\YOUR FILE PATH GOES HERE', 'r')
print(wordcount(f))
