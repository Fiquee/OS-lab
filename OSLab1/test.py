def recurprint(n):
    if(n != 1):
        print("hello world")
        recurprint(n-1)
    else:
        return


def function2(n):
    if n == 1:
        print("manul")
        return 1
    else:
        return function2(int(n/2)) + function2(int(n/2))


n = int(5)
# print(int(n / 2))
print(function2(int(n)))
