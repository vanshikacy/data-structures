def twoSum(nums, target):
    seen={}

    for i, n in enumerate(nums):
        partner=target-n

        if partner in seen:
            return [seen[partner], i]
        
        seen[n]=i

    return None

def main():
    text=input("enter nums separated by spaces:")
    pieces=text.split()
    
    nums=[]
    for p in pieces:
          nums.append(int(p))
    
    target=int(input("enter target:"))

    res=twoSum(nums, target)

    if res: 
         i, j=res
         print("indices:", i, j)
    else:
         print("no pair found")

if __name__=="__main__":
     main()