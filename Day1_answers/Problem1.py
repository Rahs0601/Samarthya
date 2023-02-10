def sumEvenNumbers(nums):
    sum = 0
    for i in range(5):
        if nums[i]%2 == 0:
            sum = sum + nums[i]
    return sum
nums = [1,2,3,4,5]
sum = sumEvenNumbers(nums)
print("\nSum of Even Numbers is :",sum)
