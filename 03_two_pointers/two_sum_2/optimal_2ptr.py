def twoSum(numbers, target):
    left, right=0, len(numbers)-1

    while left<right:
        currsum=numbers[left]+numbers[right]

        if currsum==target:
            return [left+1, right+1]
        elif currsum<target:
            left+=1
        elif currsum>target:
            right-=1

    return [-1, -1]

def main():
    numbers=list(map(int, input("Enter sorted numbers: ").split()))
    target=int(input("Enter target: "))

    result=twoSum(numbers, target)

    print(result)


if __name__=="__main__":
    main()