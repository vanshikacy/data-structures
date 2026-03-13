def majorityElement(nums):
    mp={}
    for n in nums:
        mp[n]=mp.get(n, 0)+1

    for n in nums:
        if mp[n]>len(nums)/2:
            return n

    return -1

def main():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    result = majorityElement(nums)
    print("Majority element:", result)


if __name__ == "__main__":
    main()