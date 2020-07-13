# approximating sqrt with percent difference (error) as the "Is close enough"
from numpy import mean
error = 0.01
n = 19

def sqrt(n):
    print(f'Approximate square root of: {n}')
    lastGuess = n
    nextGuess = (lastGuess + (n / lastGuess)) / 2
    pct_diff = abs(nextGuess - lastGuess) / mean([nextGuess, lastGuess])

    while pct_diff > error:
        lastGuess = nextGuess
        nextGuess = (lastGuess + (n / lastGuess)) / 2
        pct_diff = abs(nextGuess - lastGuess) / mean([nextGuess, lastGuess])
        print(f'Guess: {round(nextGuess, 4)}', f'Percent Difference: {round(pct_diff * 100, 2)}%')
        
    return nextGuess

sqrt(n)

# Converting area problem to function
def area(n, s):
    from math import tan, pi
    area = (n * s ** 2) / (4 * tan(pi / n))
    return area

area(5, 6.5)



# Simple password checker
def pw_validate(pw):
    if len(pw) < 8:
        return (False, 'preposed password has less than 8 characters')
    count_int = 0
    for char in pw:
        if not char.isalpha():
            try:
                int(char)
                count_int += 1
            except ValueError:
                return (False, 'preposed password contains something not a letter or number')
    if count_int < 2:
        return (False, 'preposed password must contain two numbers')
    return (True, pw)

def pw_set(pw):
    valid = pw_validate(pw)
    if valid[0]:
        return pw
    else:
        print(f'Cannot change password because {valid[1]}')
        return ''

pw = ''

pw_new = input('Set Password: ')
pw = pw_set(pw_new)
print(pw)
