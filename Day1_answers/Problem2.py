def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True


num = 6
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")

