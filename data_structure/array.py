
L=[1,"3",None,True,1.22,1,1]

#查找元素的序列
L.index('3')

#list遍历
for index,ele in enumerate(L):
    a=L[index]

L.reverse()
L.count(1)
L.extend([1,2,3])

#方法有：初始化、插入、删除、查找、修改、出现次数计算、排序、反转、复制、清空、合并


#iterable的区别：序列和键值对

d={1:2,3:4}.items()
ll=list(d)


#链式储存，插入和删除效率高，适合用于队列和栈
from collections import deque

#链式队列；入队、出队
class Queue:
    def __init__(self,iterable=()):
        self._queue=deque(iterable)

    def add(self,ele):
        return  self._queue.append(ele)

    def pop(self):
        return  self._queue.popleft()

    def __str__(self):
        return  self._queue.__str__()


q=Queue([7,5,4,9,0])
print(q.pop())
q.add(100)


#栈：入栈、出栈

class Stack:
    def __init__(self,iterable=()):
        self._queue=deque(iterable)

    def add(self,ele):
        return  self._queue.appendleft(ele)

    def pop(self):
        return  self._queue.popleft()

    def __str__(self):
        return  self._queue.__str__()

