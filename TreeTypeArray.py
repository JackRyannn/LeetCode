# 树状数组，其实是利用二进制来构成数组，这样频繁的单值变动会降低求和的效率，因此用树状数组可以维护一个效率更好的数组。
# 第一个点没有意义，设置为0
array = [0,1,2,3,4,5]
tree = [0] * 6
# 用来求出该点对应的二进制后面0的个数
def lowbit(t):
    return t&(-t)
# 更新单点值
def update(t,v):
    while t < len(tree):
        tree[t] += v
        t += lowbit(t)
# 求某一点之前所有数的和
def getSum(t):
    s = 0
    while t > 0:
        s += tree[t]
        t -= lowbit(t)
    return s

for i in range(1,len(array)):
    update(i,array[i])

print(array,tree)
print(getSum(5)-getSum(3))