def topKFrequent(nums, k):
    mp={}
    for n in nums:
        mp[n]=mp.get(n, 0)+1

    return sorted(mp, key=mp.get, reverse=True)[:k]

def main():
    nums=list(map(int, input("Enter numbers separated by space: ").split()))
    k=int(input("Enter k: "))

    print(topKFrequent(nums, k))


if __name__ == "__main__":
    main()