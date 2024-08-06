num = 113

for i in range(2, int(num/2)+1):
    if num%i == 0:
        print(f"{num} is not a prime number")
        break
    else:
        print(f"{num} is a prime number")
        break

