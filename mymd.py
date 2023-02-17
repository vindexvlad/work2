def is_prime(x):
    if x<=0:
        return False
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True
def is_triangle(a, b, c):
    if a+b>c and b+c>a and a+c>b:
        return True
    else:
        return False

def is_palindrome(s):
    if len(s) <= 1:
        return True
    return (is_palindrome(str.lower(s[1:len(s)-1])) and str.lower(s[0]) == str(s[len(s)-1]))
