def isPalindrome(s):
    cleaned=""

    for c in s:
        if s.isalnum():
            cleaned+=c

    return cleaned==cleaned[::-1]

def main():
    s=input("Enter string: ")
    result=isPalindrome(s)
    print(result)


if __name__=="__main__":
    main()