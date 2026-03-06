def containsDuplicate(nums):
    seen=set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

def main():
    nums=list(map(int, input("Enter numbers separated by space: ").split())) 
    result = containsDuplicate(nums)
    print(result)

if __name__ == "__main__":
    main()