def productExceptSelf(nums):
        answer=[]
        leftprod=[1]*len(nums)
        rightprod=[1]*len(nums)
        prod=1

        for i in range(len(nums)):
            leftprod[i]=prod
            prod=leftprod[i]*nums[i]
        prod=1
        for i in range(len(nums)-1,-1,-1):
            rightprod[i]=prod
            prod=rightprod[i]*nums[i]

        for i in range(len(nums)):
            answer.append(leftprod[i]*rightprod[i])

        return answer

def main():
    nums=list(map(int, input("Enter numbers separated by space: ").split()))
    print(productExceptSelf(nums))


if __name__ == "__main__":
    main()