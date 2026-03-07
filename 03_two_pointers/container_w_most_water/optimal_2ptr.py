def maxArea(height):
    maxar=0
    left, right=0, len(height)-1

    while left<right:
        ar=(right-left)*min(height[left], height[right])
        maxar=max(ar, maxar)

        if height[left]<height[right]:
            left+=1
        else:
            right-=1

    return maxar


def main():
    height=list(map(int, input("Enter heights: ").split()))
    result=maxArea(height)
    print("Maximum area:", result)


if __name__=="__main__":
    main()