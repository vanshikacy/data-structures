def lengthOfLongestSubstring(s):
    charset= set()
    ans=0
    left, right=0, 0

    while right<len(s):
        while s[right] in charset:
            charset.remove(s[left])
            left+=1
        charset.add(s[right])
        ans=max(ans, right-left+1)
        right+=1
        
    return ans

def main():
     s=input("Enter string:")
     ans=lengthOfLongestSubstring(s)
     print(ans)

if "__name__"=="__main__":
    main()

