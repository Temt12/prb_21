strin=input()
s1 = strin
s2 = list(strin)
n = 0
h = 0
for i in range(len(s1) + 1):
    if i == (len(s1)):
        n = 1
        h += 1
        break
    if s1[i] == 'a' or s1[i] == 'A':
        s2[i] = '.-'
    elif s1[i] == 'b' or s1[i] == 'B':
        s2[i] = '-...'
    elif s1[i] == 'c' or s1[i] == 'C':
        s2[i] = '-.-.'
    elif s1[i] == 'd' or s1[i] == 'D':
        s2[i] = '-..'
    elif s1[i] == 'e' or s1[i] == 'E':
        s2[i] = '.'
    elif s1[i] == 'f' or s1[i] == 'F':
        s2[i] = '..-.'
    elif s1[i] == 'g' or s1[i] == 'G':
        s2[i] = '--.'
    elif s1[i] == 'h' or s1[i] == 'H':
        s2[i] = '....'
    elif s1[i] == 'i' or s1[i] == 'I':
        s2[i] = '..'
    elif s1[i] == 'j' or s1[i] == 'J':
        s2[i] = '.---'
    elif s1[i] == 'k' or s1[i] == 'K':
        s2[i] = '-.-'
    elif s1[i] == 'l' or s1[i] == 'L':
        s2[i] = '.-..'
    elif s1[i] == 'm' or s1[i] == 'M':
        s2[i] = '--'
    elif s1[i] == 'n' or s1[i] == 'N':
        s2[i] = '-.'
    elif s1[i] == 'o' or s1[i] == 'O':
        s2[i] = '---'
    elif s1[i] == 'p' or s1[i] == 'P':
        s2[i] = '.--.'
    elif s1[i] == 'q' or s1[i] == 'Q':
        s2[i] = '--.-'
    elif s1[i] == 'r' or s1[i] == 'R':
        s2[i] = '.-.'
    elif s1[i] == 's' or s1[i] == 'S':
        s2[i] = '...'
    elif s1[i] == 't' or s1[i] == 'T':
        s2[i] = '-'
    elif s1[i] == 'u' or s1[i] == 'U':
        s2[i] = '..-'
    elif s1[i] == 'v' or s1[i] == 'V':
        s2[i] = '...-'
    elif s1[i] == 'w' or s1[i] == 'W':
        s2[i] = '.--'
    elif s1[i] == 'x' or s1[i] == 'X':
        s2[i] = '-..-'
    elif s1[i] == 'y' or s1[i] == 'Y':
        s2[i] = '-.--'
    elif s1[i] == 'z' or s1[i] == 'Z':
        s2[i] = '--..'
    else:
        print('Вводите только латинские буквы')
        break
if h != 0:
    strin = ''.join(s2)
print(strin)
