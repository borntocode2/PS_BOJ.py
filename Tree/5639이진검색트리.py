tree_pre = [] # 50 30 24 5 28 45 98 52 60
while True:
    try:
        tree_pre.append(int(input()))
    except:
        break
tree = {}
for i in range(len(tree_pre)):
    Lcount = 0
    Rcount = 0
    for j in range(i+1, len(tree_pre)):
        if tree_pre[i] < tree_pre[j]:
            tree[i]




