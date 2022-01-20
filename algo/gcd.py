a = int(input("What's the first number? "))
b = int(input("What's the second number? ")) 
while 1:
    r=a%b
    if not r:
        break
    a=b
    b=r
print('GCD is:', b)