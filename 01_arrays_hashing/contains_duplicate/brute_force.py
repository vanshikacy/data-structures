def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
             if nums[i]==nums[j]:
                 return True
    return False

def main():
    nums=list(map(int, input("Enter numbers separated by space: ").split())) 
    result = containsDuplicate(nums)
    print(result)

if __name__ == "__main__":
    main()

#TLE!!!!!!