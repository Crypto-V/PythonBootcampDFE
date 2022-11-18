def narcissistic(value):
    length = len(str(value))
    total = 0
    for i in str(value):
        total = total + int(i) ** length
    if total == value:
        return True
    else:
        return False


print(narcissistic(122))
