# YOUR CODE HERE
def summation(l1,l2):
    updated_list=[]
    for i in range(len(l1)) :
        updated_list.append(l1[i]+l2[i])
    return updated_list

def find_min_max(minmax):
    mmlist=[]
    mmlist.append(min(minmax))
    mmlist.append(max(minmax))
    return mmlist

n=int(input())
lst1=[]
lst2=[]
for i in range(n):
    lst1.append(int(input()))
for j in range(n):
    lst2.append(int(input()))
           
print(summation(lst1,lst2))
updated_list = summation(lst1,lst2)
print(find_min_max(updated_list))
