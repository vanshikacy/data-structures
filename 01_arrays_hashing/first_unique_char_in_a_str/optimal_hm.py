def firstUniqChar(s):
    mp={}
    for c in s:
        mp[c]=mp.get(c, 0)+1

    for i in range(len(s)):
        if mp[s[i]]==1:
            return i

    return -1

def main():
    s = input("Enter a string: ")
    result = firstUniqChar(s)
    print("Index of first unique character:", result)


if __name__ == "__main__":
    main()