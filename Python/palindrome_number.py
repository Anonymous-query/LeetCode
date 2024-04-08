def is_palindrome(x:int) -> bool:
    orignal_number = x
    reversed_number = 0

    while x > 0:
        digit = x % 10
        reversed_number = reversed_number * 10 + digit
        x//=10

    if orignal_number == reversed_number:
        return True
    return False

if __name__ == "__main__":
    x = 121
    result = is_palindrome(x)
    print(f"{x} is palindrom {result}")