def isAnagram(s, t):
    if len(s)!=len(t):
        return False

    mp={}

    for letter in s:
        mp[letter]=mp.get(letter, 0)+1

    for letter in t:
        if mp.get(letter, 0)==0:
            return False

    mp[letter]=mp.get(letter, 0)-1

    return True

def main():
    s=input("Enter first string: ")
    t=input("Enter second string: ")

    sol=isAnagram(s, t)
    print(sol)


if __name__ == "__main__":
    main()
