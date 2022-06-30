from collections import deque
import itertools
def moving_average(iterable,n=3):
    it = iter(iterable)
    d = deque(itertools.islice(it,n-1))  #迭代出前2个数据
    print(d)
    d.appendleft(0)  #防止第一次运行算法时候把第一个数据删除
    s = sum(d)
    print(d)
    print(s)
    for elem in it:
        s += elem-d.popleft()
        d.append(elem)
        yield s/float(n)

l = [10,20,18,27,15]
for average in moving_average(l):
  print(average)