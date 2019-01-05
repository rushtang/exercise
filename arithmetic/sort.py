
#冒泡排序,从小到大
def sort_maopao(L):

    for ele in L:
        for index in range(len(L)-1):
            if L[index]>L[index+1]:

                tmp=L[index+1]
                L[index+1]=L[index]
                L[index]=tmp
    return L

# L=[10,4,2,6,7,32,45,1,3,18,9,55,5,8,0,4,6]
#
# print(sort_maopao(L))




#循环不变式分析，本质是归纳分析
#初始化：一个元素时为真
#保持：n个元素、n+1个元素时为真
#终止：循环正确终止，且终止后是否满足期望


#快速排序,从小到大

def sort_fast(L,head_index,tail_index):

    if head_index>=tail_index:
        return

    left=head_index
    right=tail_index

    #temp为比较基准数值
    temp=L[left]

    while(left<right):
        while(L[right]>temp and left<right):
            right-=1
        if left < right:
            L[left]=L[right]
            left+=1

        while(L[left]<=temp and left<right):
            left+=1
        if left < right:
            L[right]=L[left]
            right-=1

    L[left]=temp

    sort_fast(L,head_index,left-1)
    sort_fast(L,left+1,tail_index)


L=[10,4,2,6,7,32,45,1,3,18,9,55,5,8,0,4,6]
sort_fast(L,0,len(L)-1)
print(L)






