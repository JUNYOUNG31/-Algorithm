# 좋은 구간

L = int(input())
nums = list(map(int, input().split()))
n = int(input())
ans = 0
nums.append(0)
nums.sort()
for i in range(len(nums)-1) :
    if nums[i] == n or nums[i+1] == n:
        ans = 0
        break
    elif nums[i] < n and n < nums[i+1]:
        ans = (n-nums[i]) * (nums[i+1]-n) - 1
        break
print(ans)