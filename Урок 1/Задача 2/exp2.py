def palindrome(str):
    return(str==str[::-1])
if __name__=='__main__':
    str=input()
    if palindrome(str)==True:
        print('it is palindrome')
    else:
        print('it is not palindrome')
