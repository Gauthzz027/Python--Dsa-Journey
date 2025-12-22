def is_palindrome(x):
    if x < 0:
        return False

    rev = 0
    dup = x

    while x != 0:
        last = x % 10
        rev = rev * 10 + last
        x = x // 10

    return rev == dup


x = int(input("Enter any number:"))
print(is_palindrome(x))

        