def twoSum(nums, target):
        #ts my brute force les go

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i, j]

        return None


def main():
    text=input("enter nums separated by spaces:")
    pieces=text.split()
    
    nums=[]
    for p in pieces:
          nums.append(int(p))
    
    target=int(input("enter target:"))

    res=two_Sum(nums, target)

    if res: 
         i, j=res
         print("indices:", i, j)
    else:
         print("no pair found")

if __name__=="__main__":
     main()




    


    