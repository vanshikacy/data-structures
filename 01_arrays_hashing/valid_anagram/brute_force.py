def isAnagram(s, t):
    if len(s)!=len(t):
        return False
    
    s_sorted=sorted(s)
    t_sorted=sorted(t)
    
    return s_sorted==t_sorted

def main():
    s=input("Enter first string: ")
    t=input("Enter second string: ")

    sol=isAnagram(s, t)
    print(sol)


if __name__ == "__main__":
    main()