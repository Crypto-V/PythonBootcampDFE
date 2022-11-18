def remainder(num1, num2):
    if num1 >= num2:
        return num1%num2
    else:
        return num2 % num1

final = remainder(2,5)
print("Your final remainder is : "+str(final))
