tree_pre = [] # 50 30 24 5 28 45 98 52 60
flag = 0
while True:
    try:
        tree_pre.append(int(input()))
    except:
        break
tree_first = tree_pre[0]
tree = {}
for i in range(len(tree_pre)):
    for j in range(i+1, len(tree_pre)):
        if tree_pre[i] > tree_pre[j]:
            tree[tree_pre[i]] = [tree_pre[j]]
            break
        
for i in range(len(tree_pre)):
    for j in range(i+1, len(tree_pre)):
        if flag == 0 and tree_pre[i] < tree_pre[j]:
            tree[tree_pre[i]] = [tree_pre[j]]
            flag = 1
        if tree_pre[i] < tree_pre[j] and tree_first > tree_pre[j]:
            tree[tree_pre[i]] = [tree_pre[j]]
            break

print(tree)
            




