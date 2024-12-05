# def max_num(lst):
#     x=0
#     for i in lst:
#         if(i>x):
#             x=i
#         else:
#             x=x
#     print(f'the Largest Number in the list is {x}')        

# max_num([3,5,8,9])        

# def rev(lst):
#     x=[]
#     num=len(lst)
#     print(len(lst))
#     for i in range(len(lst)):
#         x.append(i)
#     print(x)
# rev([1,2,3,4,5])
# write a program to get unique arrays from a sorted arrays 


num=[1,1,1,2,2,2,3,3,4,4,5,5,6,6]
unique_arr = list(set(num))
print(unique_arr)