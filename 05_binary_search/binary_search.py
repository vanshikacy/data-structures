def search(nums, target):
    low, high=0, len(nums)-1

    while low<=high:
        mid=(low+high)//2

        if target==nums[mid]:
            return mid
        elif nums[mid]<target:
            low=mid+1
        elif nums[mid]>target:
            high=mid-1
            
    return -1

if __name__=="__main__":
    nums=list(map(int, input("Enter sorted numbers (space separated): ").split()))
    target=int(input("Enter target: "))

    result=search(nums, target)

    if result!=-1:
        print("Target found at index:", result)
    else:
        print("Target not found")