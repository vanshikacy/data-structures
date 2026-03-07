def isPalindrome(s):
    s=s.lower() #returns new string
    left, right=0, len(s)-1
    while left<=right:
        while left<right and not s[left].isalnum():
            left+=1
        while left <right and not s[right].isalnum():
            right-=1
            
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

def main():
    s=input("Enter string: ")
    result=isPalindrome(s)
    print(result)


if __name__=="__main__":
    main()