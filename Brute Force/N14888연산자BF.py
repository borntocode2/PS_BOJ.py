N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))

def dfs(n, sm, add, sub, mul, div):
    global mn, mx
    if n == N:
        mn = min(mn, sm)
        mx = max(mx, sm)
        return
    if add > 0:
        dfs(n+1, sm+nums[n], add-1, sub, mul, div)
    if sub > 0:
        dfs(n+1, sm-nums[n], add, sub-1, mul, div)
    if mul > 0:
        dfs(n+1, sm*nums[n], add, sub, mul-1, div)
    if div > 0: #check
        dfs(n+1, sm//nums[n], add, sub, mul, div-1)
mn, mx = 1000000000, -1000000000

dfs(1, nums[0], add, sub, mul, div)

print(mx)
print(mn)