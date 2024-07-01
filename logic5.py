s=input('Enter a letter')
a=s[::-1]
print(a)


nums=input('Enter the list(seperate with spaces)') 
nums=list(map(int,nums.split()))           
target=int(input('Enter a number'))
for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+ nums[j]==target:
             result=i,j
             print([int(d)for d in result])   
                 

