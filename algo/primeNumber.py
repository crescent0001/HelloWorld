# Python program to display all the prime numbers within an interval

lower = 1
upper = 100
count=0

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
        #    print(num)
           count +=1
print("nos of primes: " + str(count) + "%:" + str((count/upper)*100))