def longestConsecutive(nums):
        if len(nums)<1:
            return 0
        nums.sort()
        ans=1

        count=1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]: #duplicates
                continue
            elif nums[i]-nums[i-1]==1: #streak update
                count+=1
            else: # ie if nums[i]-nums[i-1]> 1
                count=1 #reset
            ans=max(ans, count)
        return ans

def main():
    nums=list(map(int, input("Enter numbers separated by space: ").split()))
    print(longestConsecutive(nums))


if __name__ == "__main__":
    main()