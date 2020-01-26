num = int(input("Enter the number :"))
def fact(num):
    i = 1
    while num>1:
        i = i * num
        num -= 1
    return i

print("Factorial of the given number is {} :".format(num), fact(num))
