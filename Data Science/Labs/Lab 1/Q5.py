def intersection(lst1,lst2):
    return list(set(lst1) & set(lst2))


list1 =  [1,3,6,78,35,55]
list2 =  [12,24,35,24,88,120,155]
print(intersection(list1,list2))